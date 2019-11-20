import traceback

import pandas as pd
from PIL import ImageDraw, ImageQt
from PySide2.QtCore import Slot
from PySide2.QtGui import QPixmap, qApp
from PySide2.QtWidgets import QMenu, QMessageBox, QWidget

import utils.commons as utils
from analysis.indexes import ACI
from audio.recording import Recording
from gui.utils.settings import Settings
from gui.utils.tree.recordingsTreeModel import RecordingsTreeModel
from gui.widgets.audio.acidialog import AciDialog
from gui.widgets.audio.detectordialog import DetectorDialog
from gui.widgets.audio.ui.audiomanager_ui import Ui_AudioManager


def get_ACI(rec):
    return ACI(recording=rec)


def update_path(path):
    new = path.replace("Seagate Backup Plus Drive", "Backup")
    return new


class AudioManager(QWidget, Ui_AudioManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.audio_analyzer = QAudioAnalyzer()
        self.current_recording = None
        self.song_classifier = None
        self.action_dialog = None

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

        self.time_slider.valueChanged.connect(self.update_spectrogram)

        self.btn_export_pdf.clicked.connect(self.export_pdf)

        # self.audio_analyzer.logging.connect(self.log, type=Qt.BlockingQueuedConnection)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.action_delete)
        menu.addAction(self.action_create_links)
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

    def draw_events(self, img, duration):
        events_table = qApp.tables.song_events
        if not events_table.empty:
            events = events_table.get_events(self.current_recording.id)
            im_start = self.time_slider.value()
            im_end = self.time_slider.value() + duration
            current_events = events[(events.start >= im_start) & (
                events.start < im_end)]
            if len(current_events.index):
                #  img = img.convert("RGB")
                for event in current_events.itertuples():
                    # TODO: externalize color
                    draw = ImageDraw.Draw(img, "RGBA")
                    start = self.sec2pixels(
                        event.start - self.time_slider.value())
                    end = self.sec2pixels(
                        min(event.end, im_end) - self.time_slider.value())
                    draw.rectangle(((start, 0), (end, 299)),
                                   fill=(255, 255, 0, 100))

        return img

    def sec2pixels(self, sec, to_int=True):
        pix = 299 * sec / 1.5
        if to_int:
            return int(pix)
        return pix

    @Slot()
    def update_spectrogram(self):
        # TODO: add spectrogram options
        max_duration = self.lbl_spectro.width() * 1.5 / 299
        spectro = self.current_recording.spectrogram
        spec = spectro.get_subspec(self.time_slider.value(), max_duration)
        # TODO: externalize ratio pixel/duration
        # TODO: save image somewhere
        im = qApp.imgen.spec2img(spec, size=(
            self.sec2pixels(max_duration), 299))
        # TODO: change events when checkbox is checked
        if self.checkbox_draw_events.isChecked():
            im = self.draw_events(im, max_duration)
        img = ImageQt.ImageQt(im)
        pixmap = QPixmap.fromImage(img)
        # TODO: add multiple spectrograms?
        self.lbl_spectro.setPixmap(pixmap)
        self.update_duration_lbl()

    def update_duration_lbl(self):
        duration = utils.format_s2hms(self.current_recording.duration)
        current = utils.format_s2hms(self.time_slider.value())
        lbl = current + "/" + duration
        self.lbl_duration.setText(lbl)

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

    def create_links(self):
        print("creating virtual links...")
        recs = self.get_selected_recordings()
        print(recs)

    def delete_recordings(self):
        print("deleting...")
        recs = self.get_selected_recordings(type="index")
        idxs = self.tree_view.selectedIndexes()
        idx = idxs[0]
        self.tree_view.clearSelection()
        self.tree_view.model().removeRow(idx.row(), idx.parent())
        qApp.tables.recordings.delete(recs, save=True)
        values_dict = {"recording_id": recs}
        qApp.tables.song_events.delete(values_dict, columns=["recording_id"])
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

        self.lbl_spectro.setText(
            "{} recordings representing {}of audio found!".format(res.shape[0], duration))

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
        self.current_recording = Recording(file_info,
                                           spec_opts=settings.spectrogram_settings())
        self.show_recording_info(["id", "name", "path", "year"])
        self.update_spectrogram()
        self.time_slider.setMaximum(self.current_recording.duration)
        self.update_duration_lbl()

    def folder_query(self, folder_info):
        return ' & '.join(['{} == "{}"'.format(k, v) for k, v in folder_info.items()])
