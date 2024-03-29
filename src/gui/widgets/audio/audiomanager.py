import os
import resource
import traceback

import pandas as pd
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMenu, QMessageBox

import utils.commons as utils
from gui.widgets.audio.ui.audiomanager_ui import Ui_AudioManager
from gui.widgets.common.page_widget import PageWidget
from gui.widgets.common.tree.recordings_tree_model import RecordingsTreeModel
from pysoundviewer.gui.settings import SoundPlayerSettings


def update_path(path):
    new = path.replace("Seagate Backup Plus Drive", "Backup")
    return new


class AudioManager(PageWidget, Ui_AudioManager):
    def __init__(self):
        super().__init__()
        print(
            "Audiomanager1: Memory usage: %s (kb)"
            % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        )
        self.setupUi(self)
        self.current_recording = None
        self.action_dialog = None
        self.settings = SoundPlayerSettings()
        self.share_settings()
        self.link_events()
        self.init_tree()
        self.tree_view.setRootIsDecorated(True)

    # def enter_page(self):
    # self.init_tree()
    # print('Audiomanager4: Memory usage: %s (kb)' %
    #       resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    # self.tree_view.setRootIsDecorated(True)

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
        self.tree_view.selectionModel().selectionChanged.connect(
            self.tree_selection_changed
        )
        # self.add_actions()
        self.show_multiple_details()

    # def add_actions(self):
    #     self.tree_view.addAction(self.action_ACI)
    #     self.tree_view.addAction(self.action_detect_songs)

    def link_events(self):
        self.action_ACI.triggered.connect(self.compute_ACI)
        self.action_calculate_activity.triggered.connect(self.detect_songs)
        self.action_delete.triggered.connect(self.show_delete_msg)
        self.action_create_links.triggered.connect(self.show_create_links_msg)
        self.action_import_tags.triggered.connect(self.import_tags)
        self.action_export_song_events.triggered.connect(self.export_song_events)
        self.action_evaluate_detector.triggered.connect(self.evaluate_detector)

        # self.time_slider.valueChanged.connect(self.update_spectrogram)

        self.btn_export_pdf.clicked.connect(self.export_pdf)

        self.checkbox_draw_events.clicked.connect(self.draw_annotations)
        self.checkbox_draw_tags.clicked.connect(self.draw_annotations)
        self.checkbox_show_overlaps.clicked.connect(self.draw_annotations)
        self.song_events_options.option_changed.connect(self.draw_annotations)

        self.sound_player.update_position.connect(
            self.spectrogram_viewer.update_sound_marker
        )
        self.spectrogram_viewer.seek.connect(self.sound_player.seek)
        self.spectrogram_viewer.spectrogram_drawn.connect(self.draw_annotations)
        self.image_options.option_updated.connect(self.spectrogram_viewer.update_image)
        self.spectrogram_options.option_updated.connect(
            self.spectrogram_viewer.update_spectrogram
        )

        # self.audio_analyzer.logging.connect(self.log, type=Qt.BlockingQueuedConnection)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.action_delete)
        menu.addAction(self.action_create_links)
        menu.addAction(self.action_import_tags)
        menu.addSeparator()
        menu.addAction(self.action_ACI)
        menu.addAction(self.action_calculate_activity)
        menu.addAction(self.action_export_song_events)
        menu.addAction(self.action_evaluate_detector)
        menu.exec_(event.globalPos())

    @Slot()
    def tree_selection_changed(self, new, old):
        if len(self.tree_view.selectedIndexes()) == 1:
            index = new.indexes()[0]
            item = index.model().itemFromIndex(index)
            if not item.is_folder:
                self.show_recording_details(item.data())
                return
        self.show_multiple_details()

    def draw_events(self):
        event_options = self.song_events_options.get_options()
        events = self.current_recording.get_events(event_options)
        if events is not None and not events.empty:
            for event in events.itertuples():
                # # TODO: externalize color
                fill_color = "#99ebef00"
                text = ""
                if self.checkbox_show_overlaps.isChecked():
                    if hasattr(event, "matched"):
                        text = "event overlap: " + str(
                            round(
                                self.current_recording.get_event_overlap(
                                    event.event_id
                                ),
                                2,
                            )
                        )
                        if event.matched:
                            fill_color = "#34d300"  # "#ff1c8f6a"
                # color = "#991c8f6a"  else "#99ebef00"
                self.spectrogram_viewer.draw_annotation(
                    {
                        "start": event.event_start,
                        "end": event.event_end,
                        "color": "#99ebef00",
                        "fill_color": fill_color,
                        "text": text,
                    }
                )
        return None
        # self.draw_silences()

    def draw_tags(self):
        if self.current_recording.tag_status():
            event_options = self.song_events_options.get_options()
            tags = self.current_recording.get_tags(event_options)
            for tag in tags.itertuples():
                fill_color = "#99a4cafd"
                text = ""
                top_offset = 0
                if self.checkbox_show_overlaps.isChecked():
                    if hasattr(tag, "matched"):
                        text = (
                            " (overlap: "
                            + str(
                                round(self.current_recording.get_tag_overlap(tag.id), 2)
                            )
                            + ")"
                        )
                        if tag.matched:
                            fill_color = "#34d300"
                        top_offset = 30
                self.spectrogram_viewer.draw_annotation(
                    {
                        "start": tag.tag_start,
                        "end": tag.tag_end,
                        "text": ".".join([str(tag.tag_index), tag.tag]) + text,
                        "text_color": None,
                        "top_offset": top_offset,
                        "color": "#99a4cafd",
                        "fill_color": fill_color,
                    }
                )

    @Slot()
    def draw_annotations(self):
        if self.current_recording:
            self.spectrogram_viewer.clear_rects()
            if self.checkbox_draw_events.isChecked():
                self.draw_events()
            if self.checkbox_draw_tags.isChecked():
                self.draw_tags()

    def draw_silences(self, draw=True):
        silences = self.sound_player.audio.get_silences(top_db=80)
        if silences and draw:
            for start, end in silences:
                self.spectrogram_viewer.draw_rect(
                    start / self.sound_player.audio.sr,
                    end / self.sound_player.audio.sr,
                    color="#99ff0000",
                )

    @Slot()
    def compute_ACI(self):
        # Get list of all selected recordings
        recs = self.get_selected_recordings()
        from gui.widgets.dialogs.acidialog import AciDialog

        self.action_dialog = AciDialog(recs, parent=self)
        self.action_dialog.show()

    @Slot()
    def export_pdf(self):
        self.detect_songs(export_pdf=True)

    @Slot()
    def detect_songs(self, export_pdf=False):
        recs = self.get_selected_recordings()
        from gui.widgets.dialogs.detector_dialog import DetectorDialog

        self.action_dialog = DetectorDialog(recs, export_pdf, parent=self)
        self.action_dialog.setModal(True)
        self.action_dialog.show()

    @Slot()
    def show_delete_msg(self):
        msgbox = QMessageBox(parent=self)
        # TODO: change text based on number/selection
        msgbox.setText("Do you want to delete these recordings?")
        msgbox.setInformativeText(
            (
                "All data related to these recordings"
                " (indexes, song detection) will also be deleted"
            )
        )
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
        msgbox.setInformativeText("Existing links will be overwritten")
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

    @Slot()
    def import_tags(self):
        print("Importing labels...")
        recs = self.get_selected_recordings(selection_type="table")
        from gui.widgets.dialogs.import_tags_dialog import ImportTagsDialog

        self.action_dialog = ImportTagsDialog(recs, parent=self)
        self.action_dialog.setModal(True)
        self.action_dialog.show()

    @Slot()
    def export_song_events(self):
        print("Exporting song events")
        recs = self.get_selected_recordings(selection_type="table")
        from gui.widgets.dialogs.export_song_events_dialog import ExportSongEventsDialog

        self.action_dialog = ExportSongEventsDialog(recs, parent=self)
        self.action_dialog.setModal(True)
        self.action_dialog.show()

    def delete_recordings(self):
        print("deleting...")
        recs = self.get_selected_recordings(selection_type="index")
        idxs = self.tree_view.selectedIndexes()
        idx = idxs[0]
        self.tree_view.clearSelection()
        self.tree_view.model().removeRow(idx.row(), idx.parent())
        qApp.tables.recordings.delete(recs, save=True)
        values_dict = {"recording_id": recs}
        qApp.tables.song_events.delete(values_dict, columns=["recording_id"], save=True)
        qApp.tables.activity_predictions.delete(
            values_dict, columns=["recording_id"], save=True
        )
        # TODO : delete other dependencies

    def evaluate_detector(self):
        opts = {
            "selected_recordings": self.get_selected_recordings("table")[
                ["id", "has_tags"]
            ]
        }
        self.change_page.emit("analysis", opts)

    def get_selected_recordings(self, selection_type=None):
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
        tmp = [recordings.query(self.folder_query(folder)) for folder in sel_folders]
        # Get individually selected recordings
        tmp.append(recordings.loc[sel_recs])
        # Get one list of unique selected files
        res = pd.concat(tmp).drop_duplicates()
        # Load files if not already in memory
        if selection_type == "index":
            return res.index.values
        elif selection_type == "table":
            return res
        elif selection_type == "id":
            return list(res.id.unique())
        else:
            return qApp.load_recordings(res.index.values)

    def show_multiple_details(self):
        self.current_recording = None
        if self.tree_view.selectedIndexes():
            res = self.get_selected_recordings("table")
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
            res.shape[0], duration
        )
        self.spectrogram_viewer.display_text(details)
        # self.lbl_spectro.setText(details)

    def show_recording_info(self, infos):
        for info in infos:
            try:
                label = getattr(self, "lbl_" + info)
                value = getattr(self.current_recording, info)
                label.setText(str(value))
            except AttributeError:
                print(traceback.format_exc())

    def get_recording(self, index):
        self.current_recording = qApp.tables.recordings.get_recording(index)
        # Load predictions
        if self.current_recording.predictions is None:
            self.current_recording.predictions = qApp.tables.activity_predictions.get_predictions_by_id(
                self.current_recording.id
            ).copy()
        # Load tags
        if self.current_recording.has_tags and self.current_recording.tags is None:
            self.current_recording.tags = qApp.tables.tags.get_recording_tags(
                self.current_recording.id
            ).copy()

    def show_recording_details(self, file_info):
        # TODO: setting to enable/disable display on each selection change
        # TODO: improve performance to avoid reloading everything.
        self.get_recording(file_info["Index"])
        # self.current_recording = (
        #     qApp.tables.recordings.get_recording()
        # )  # Recording(file_info)
        self.show_recording_info(["id", "name", "path", "year"])
        self.load_file(self.current_recording.path)

    def load_file(self, path):
        if os.path.exists(path):
            audio = self.sound_player.load_file(file_path=path)
            self.spectrogram_viewer.audio = audio
        else:
            self.spectrogram_viewer.display_text(
                "File not found. Please make sure the path has not changed"
            )

    def folder_query(self, folder_info):
        return " & ".join(['{} == "{}"'.format(k, v) for k, v in folder_info.items()])

    def option_changed(self, option):
        opt, value = option
        if opt == "highlight_predictions":
            if value:
                recs = qApp.tables.activity_predictions.df.recording_id.unique()
            else:
                recs = []
            self.tree_view.model().check_predictions(recs)
