import traceback

import pandas as pd
from PySide2.QtCore import Slot
from PySide2.QtGui import qApp
from PySide2.QtWidgets import QMenu, QMessageBox, QWidget

import utils.commons as utils
from analysis.indexes import ACI
from audio.recording import Recording
from gui.utils.settings import Settings
from gui.utils.tree.recordingsTreeModel import RecordingsTreeModel
from gui.widgets.dialogs.acidialog import AciDialog
from gui.widgets.dialogs.detector_dialog import DetectorDialog
from gui.widgets.dialogs.tag_import_dialog import TagImportDialog
from gui.widgets.audio.ui.audiomanager_ui import Ui_AudioManager
from pysoundplayer.gui.settings import SoundPlayerSettings


def get_ACI(rec):
    return ACI(recording=rec)


def update_path(path):
    new = path.replace("Seagate Backup Plus Drive", "Backup")
    return new


class AudioManager(QWidget, Ui_AudioManager):

    EVENT_DETECTION_METHODS = ["standard", "subsampling"]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_recording = None
        self.song_classifier = None
        self.action_dialog = None

        self.settings = SoundPlayerSettings()
        self.share_settings()

        self.init_tree()
        self.link_events()

        # aci_table = TableModel(ACI.COLUMNS, df=pd.DataFrame(),
        #                        dbmanager=qApp.dbmanager, table="ACI")
        # aci_table = ACITable(dbmanager=qApp.dbmanager)
        # print(aci_table.df)
        # aci_table.save()

        # recs = qApp.get_recordings()
        # recs = recs[recs.site != "2018"]
        # qApp.recordings.create(recs, save=True)
        # recs["path"] = recs["path"].map(update_path)
        # print(recs["path"])
        # qApp.recordings.create(recs, save=True)
        # aci_table.save()

        self.tree_view.setRootIsDecorated(True)

    def share_settings(self):
        self.spectrogram_viewer.settings = self.settings
        self.spectrogram_options.options = self.settings.spectrogram_options
        self.image_options.options = self.settings.image_options

    def init_tree(self):
        recordings = qApp.get_recordings()
        categories = ["year", "site", "plot"]

        model = RecordingsTreeModel(self, recordings, categories=categories)
        self.tree_view.setModel(model)
        self.tree_view.expand(model.item(0, 0).index())
        self.add_actions()
        self.show_folder_details()

    def add_actions(self):
        self.tree_view.addAction(self.action_ACI)
        self.tree_view.addAction(self.action_detect_songs)

    def link_events(self):
        self.tree_view.selectionModel().selectionChanged.connect(self.tree_selection_changed)

        self.action_ACI.triggered.connect(self.compute_ACI)
        self.action_detect_songs.triggered.connect(self.detect_songs)
        self.action_delete.triggered.connect(self.show_delete_msg)
        self.action_create_links.triggered.connect(self.show_create_links_msg)
        self.action_check_labels.triggered.connect(self.check_labels)

        # self.time_slider.valueChanged.connect(self.update_spectrogram)

        self.btn_export_pdf.clicked.connect(self.export_pdf)
        # self.checkbox_draw_events.toggled.connect(self.draw_events)

        self.group_draw_events.toggled.connect(self.draw_events)
        self.spin_activity.valueChanged.connect(self.draw_events)
        self.spin_end_threshold.valueChanged.connect(self.draw_events)
        self.spin_min_duration.valueChanged.connect(self.draw_events)
        self.combo_method.currentIndexChanged.connect(self.draw_events)

        self.sound_player.update_position.connect(
            self.spectrogram_viewer.update_sound_marker)
        self.spectrogram_viewer.seek.connect(self.sound_player.seek)
        self.spectrogram_viewer.spectrogram_drawn.connect(self.draw_events)
        self.image_options.option_updated.connect(
            self.spectrogram_viewer.update_image)
        self.spectrogram_options.option_updated.connect(
            self.spectrogram_viewer.update_spectrogram)

        # self.audio_analyzer.logging.connect(self.log, type=Qt.BlockingQueuedConnection)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.action_delete)
        menu.addAction(self.action_create_links)
        menu.addAction(self.action_check_labels)
        menu.addSeparator()
        menu.addAction(self.action_ACI)
        menu.addAction(self.action_detect_songs)
        menu.exec_(event.globalPos())

    @Slot()
    def tree_selection_changed(self, new, old):
        # TODO: handle multiple selection
        if not new.indexes() or len(new.indexes()) == 0:
            self.show_folder_details()
            return
        # TODO: handle multiple selection
        index = new.indexes()[0]
        item = index.model().itemFromIndex(index)
        if item.is_folder:
            # item is folder
            self.show_folder_details(item.data())
        else:
            # item is recording
            self.show_recording_details(item.data())

    @Slot()
    def draw_events(self):
        self.spectrogram_viewer.clear_rects()
        if self.group_draw_events.isChecked():
            predictions_table = qApp.tables.activity_predictions
            if not predictions_table.empty:
                event_options = {"method": self.EVENT_DETECTION_METHODS[self.combo_method.currentIndex()],
                                 "min_activity": self.spin_activity.value(),
                                 "end_threshold": self.spin_end_threshold.value(),
                                 "min_duration": self.spin_min_duration.value() / 1000,
                                 "isolate_events": True}
                events = predictions_table.get_events_by_id(
                    self.current_recording.id, event_options)
                if not events.empty:
                    for event in events.itertuples():
                        # # TODO: externalize color
                        self.spectrogram_viewer.draw_rect(
                            event.start, event.end, color="#99ebef00")
            self.draw_silences()

    def draw_silences(self, draw=True):
        silences = self.sound_player.audio.get_silences(top_db=80)
        if silences and draw:
            for start, end in silences:
                self.spectrogram_viewer.draw_rect(
                    start/self.sound_player.audio.sr,
                    end/self.sound_player.audio.sr,
                    color="#99ff0000")

    @Slot()
    def compute_ACI(self):
        # Get list of all selected recordings
        recs = self.get_selected_recordings()
        self.action_dialog = AciDialog(recs, parent=self)
        self.action_dialog.show()

    @Slot()
    def export_pdf(self):
        self.detect_songs(export_pdf=True)

    @Slot()
    def detect_songs(self, export_pdf=False):
        recs = self.get_selected_recordings()
        self.action_dialog = DetectorDialog(recs, export_pdf, parent=self)
        self.action_dialog.setModal(True)
        self.action_dialog.show()

    @Slot()
    def show_delete_msg(self):
        msgbox = QMessageBox(parent=self)
        # TODO: change text based on number/selection
        msgbox.setText("Do you want to delete these recordings?")
        msgbox.setInformativeText(('All data related to these recordings'
                                   ' (indexes, song detection) will also be deleted'))
        msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgbox.setDefaultButton(QMessageBox.Cancel)
        msgbox.setIcon(QMessageBox.Warning)
        ret = msgbox.exec()
        if ret == QMessageBox.Ok:
            self.delete_recordings()
        else:
            print("not deleting")

    @Slot()
    def show_create_links_msg(self):
        msgbox = QMessageBox(parent=self)
        # TODO: change text based on number/selection
        msgbox.setText("Do you want to create virtual links for these files?")
        msgbox.setInformativeText('Existing links will be overwritten')
        msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgbox.setDefaultButton(QMessageBox.Cancel)
        msgbox.setIcon(QMessageBox.Warning)
        ret = msgbox.exec()
        if ret == QMessageBox.Ok:
            self.create_links()
        else:
            print("not deleting")

    # @Slot()
    # def show_check_labels_msg(self):
    #     msgbox = QMessageBox(parent=self)
    #     # TODO: change text based on number/selection
    #     msgbox.setText(
    #         "Do you want to check and import labels for these files?")
    #     msgbox.setInformativeText('Existing labels will be removed')
    #     msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     msgbox.setDefaultButton(QMessageBox.Cancel)
    #     msgbox.setIcon(QMessageBox.Warning)
    #     ret = msgbox.exec()
    #     if ret == QMessageBox.Ok:
    #         self.check_labels()
    #     else:
    #         print("not checking labels")

    def create_links(self):
        print("creating virtual links...")
        recs = self.get_selected_recordings()
        print(recs)

    @Slot()
    def check_labels(self):
        print("Importing labels...")
        recs = self.get_selected_recordings(type="table")
        self.action_dialog = TagImportDialog(recs, parent=self)
        self.action_dialog.setModal(True)
        self.action_dialog.show()

    def delete_recordings(self):
        print("deleting...")
        recs = self.get_selected_recordings(type="index")
        idxs = self.tree_view.selectedIndexes()
        idx = idxs[0]
        self.tree_view.clearSelection()
        self.tree_view.model().removeRow(idx.row(), idx.parent())
        qApp.tables.recordings.delete(recs, save=True)
        values_dict = {"recording_id": recs}
        qApp.tables.song_events.delete(
            values_dict, columns=["recording_id"], save=True)
        print(qApp.tables.activity_predictions)
        qApp.tables.activity_predictions.delete(
            values_dict, columns=["recording_id"], save=True)
        print(qApp.tables.activity_predictions)
        # TODO : delete other dependencies

    def get_selected_recordings(self, type=None):
        res = None
        sel_recs = []
        sel_folders = []
        # get selected indexes
        idxs = self.tree_view.selectedIndexes()
        for idx in idxs:
            item = idx.model().itemFromIndex(idx)
            data = item.data()
            if item.is_folder:
                sel_folders.append(data)
            else:
                sel_recs.append(data["Index"])
        # If folders are selected, selected all recordings inside
        recordings = qApp.get_recordings()
        tmp = [recordings.query(self.folder_query(folder))
               for folder in sel_folders]
        # Get individually selected recordings
        tmp.append(recordings.loc[sel_recs])
        # Get one list of unique selected files
        res = pd.concat(tmp).drop_duplicates()
        # Load files if not already in memory
        if type == "index":
            return res.index.values
        elif type == "table":
            return res
        else:
            return qApp.load_recordings(res.index.values)

    def show_folder_details(self, folder_info=None):
        if folder_info is not None:
            query = self.folder_query(folder_info)
            res = qApp.tables.recordings.query(query)
        else:
            res = qApp.tables.recordings.df
        if not res.empty:
            total_secs = int(res["duration"].sum())
            time = utils.time_from_secs(total_secs)
            duration = ""
            if time.days > 0:
                duration += "{} days ".format(time.days)
            if time.hours > 0:
                duration += "{} hours ".format(time.hours)
            if time.minutes > 0:
                duration += "{} minutes ".format(time.minutes)
            if time.seconds > 0:
                duration += "{} seconds ".format(time.seconds)
        else:
            duration = "0 seconds "

        details = "{} recordings representing {}of audio found!".format(
            res.shape[0], duration)
        self.spectrogram_viewer.display_text(details)
        # self.lbl_spectro.setText(details)

    def show_recording_info(self, infos):
        for info in infos:
            try:
                label = getattr(self, "lbl_" + info)
                value = getattr(self.current_recording, info)
                label.setText(str(value))
            except AttributeError as err:
                print(traceback.format_exc())

    def show_recording_details(self, file_info):
        # TODO: setting to enable/disable display on each selection change
        # TODO: improve performance to avoid reloading everything.
        # TODO: add generators to qApp?
        settings = Settings()
        print(file_info)
        self.current_recording = Recording(file_info)
        self.show_recording_info(["id", "name", "path", "year"])
        self.load_file(self.current_recording.path)
        # self.draw_events()
        # self.update_spectrogram()
        # self.update_spectrogram2()
        # self.time_slider.setMaximum(self.current_recording.duration)
        # self.update_duration_lbl()

    def load_file(self, path):
        audio = self.sound_player.load_file(file_path=path)
        self.spectrogram_viewer.audio = audio
        return audio

    def folder_query(self, folder_info):
        return ' & '.join(['{} == "{}"'.format(k, v) for k, v in folder_info.items()])

    # Scene utils
