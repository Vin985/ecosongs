import traceback

import pandas as pd
from PIL import ImageDraw, ImageQt
from PySide2.QtCore import Slot
from PySide2.QtGui import QPixmap, qApp
from PySide2.QtWidgets import QMenu, QWidget

import utils.commons as utils
from analysis.detection.song_detector import SongEventsTable
from analysis.indexes import ACI, ACITable
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

        self.time_slider.valueChanged.connect(self.update_spectrogram)

        # self.audio_analyzer.logging.connect(self.log, type=Qt.BlockingQueuedConnection)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.action_ACI)
        menu.addAction(self.action_detect_songs)
        menu.exec_(event.globalPos())

    @Slot()
    def tree_selection_changed(self, new, old):
        # TODO: handle multiple selection
        if not new.indexes():
            self.show_folder_details()
        index = new.indexes()[0]
        item = index.model().itemFromIndex(index)
        if item.is_folder:
            # item is folder
            self.show_folder_details(item.data())
        else:
            # item is recording
            self.show_recording_details(item.data())

    def draw_events(self, img, duration):
        #TODO: add events table to qApp
        events_table = SongEventsTable(dbmanager=qApp.feather_manager)
        events = events_table.get_events(self.current_recording.id)
        im_start = self.time_slider.value()
        im_end = self.time_slider.value() + duration
        current_events = events[(events.start >= im_start) & (events.start < im_end)]
        if len(current_events.index):
            #  img = img.convert("RGB")
            for event in current_events.itertuples():
                print(event)
                # TODO: externalize color
                draw = ImageDraw.Draw(img, "RGBA")
                start = self.sec2pixels(event.start - self.time_slider.value())
                end = self.sec2pixels(min(event.end, im_end) - self.time_slider.value())
                print(start)
                print(end)
                draw.rectangle(((start, 0), (end, 299)), fill=(255, 255, 0, 128))

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
        im = qApp.imgen.spec2img(spec, size=(self.sec2pixels(max_duration), 299))
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
        # Get spectrogram settings for computing ACIs
        # TODO: add menu for this
        self.action_dialog = AciDialog(recs)
        self.action_dialog.show()

        # if not acis.empty:
        #     aci_table = TableModel(ACI.COLUMNS, dbmanager=qApp.dbmanager, table="ACI")
        #     aci_table.add(acis, save=True)
        # acis = pd.DataFrame([aci.to_dict() for aci in self.analysis_thread.res])

    @Slot()
    def detect_songs(self):
        recs = self.get_selected_recordings()
        self.action_dialog = DetectorDialog(recs)
        self.action_dialog.show()

    def get_selected_recordings(self):
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
        tmp = [qApp.recordings.query(self.folder_query(folder))
               for folder in sel_folders]
        # Get individually selected recordings
        tmp.append(qApp.get_recordings().iloc[sel_recs])
        # Get one list of unique selected files
        res = pd.concat(tmp).drop_duplicates()
        res = res[res["duration"] > 0]
        # Load files if not already in memory
        recs = qApp.load_recordings(res.index.values)
        return recs

    def show_folder_details(self, folder_info=None):
        if folder_info is not None:
            query = self.folder_query(folder_info)
            res = qApp.recordings.query(query)
        else:
            res = qApp.recordings.df
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
