import pandas as pd
import yaml
from PIL import ImageQt
from PySide2.QtCore import QThread, Slot
from PySide2.QtGui import QPixmap, qApp
from PySide2.QtWidgets import QMenu, QWidget

import utils.commons as utils
from analysis.indexes import ACI, ACITable
from audio.recording import Recording
from gui.utils.settings import Settings
from gui.utils.tree.recordingsTreeModel import RecordingsTreeModel
from gui.widgets.audio.QAudioAnalyzer import QAudioAnalyzer
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
        self.audio_analyzer = QAudioAnalyzer()
        self.current_recording = None
        self.song_classifier = None

        self.init_tree()
        self.link_events()
        self.init_thread()

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

        self.audio_analyzer.progressed.connect(self.update_progress)
        # self.audio_analyzer.logging.connect(self.log, type=Qt.BlockingQueuedConnection)

    def init_thread(self):
        self.worker_thread = QThread()
        self.audio_analyzer.moveToThread(self.worker_thread)
        self.worker_thread.finished.connect(self.audio_analyzer.deleteLater)
        self.destroyed.connect(self.worker_thread.quit)
        self.worker_thread.start()

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.action_ACI)
        menu.addAction(self.action_detect_songs)
        menu.exec_(event.globalPos())

    @Slot()
    def update_progress(self, progress):
        print("progress" + str(progress))

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

    @Slot()
    def update_spectrogram(self):
        # TODO: add spectrogram options
        max_duration = self.lbl_spectro.width() * 1.5 / 299
        spectro = self.current_recording.spectrogram
        spec = spectro.get_subspec(self.time_slider.value(), max_duration)
        # TODO: externalize ratio pixel/duration
        # TODO: save image somewhere
        im = qApp.imgen.spec2img(spec, size=(
            int(299 * max_duration / 1.5), 299))
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
        settings = Settings()
        spec_opts = settings.spectrogram_settings()
        spec_opts.update({'to_db': False, 'remove_noise': False})

        # Compute ACIs
        # acis = self.audio_analyzer.compute_index(recs, "ACI", spec_opts=spec_opts)
        # acis = pd.DataFrame(acis)
        # print(acis)

        acis = self.audio_analyzer.compute_index(recs, "ACI", spec_opts=spec_opts)
        acis = pd.DataFrame(acis)
        print(acis)
        # if not acis.empty:
        #     aci_table = TableModel(ACI.COLUMNS, dbmanager=qApp.dbmanager, table="ACI")
        #     aci_table.add(acis, save=True)
        # acis = pd.DataFrame([aci.to_dict() for aci in self.analysis_thread.res])
        # for item in self.analysis_thread.res:
        #     print(item)
        # print(self.analysis_thread.res)

    @Slot()
    def detect_songs(self):
        print("detecting songs")
        recs = self.get_selected_recordings()
        # TODO: add detection options in UI
        model_opts = {"model_root_dir": "analysis/detection/models",
                      "classifier": "biotic",
                      "options_file": "analysis/detection/models/biotic/network_opts.yaml",
                      "weights_file": "analysis/detection/models/biotic/weights_99.pkl-1"}
        with open(model_opts["options_file"]) as f:
            options = yaml.load(f)
        detection_options = {'min_activity': 0.85, 'min_duration': 0.01}  # {'min_activity' : 0.6, 'min_duration' : 0}
        print(recs[0])
        events = self.audio_analyzer.detect_songs(recs,
                                                  options=options,
                                                  weight_file=model_opts["weights_file"],
                                                  detection_options=detection_options)
        events = pd.DataFrame(events)
        print(events)

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

    def show_recording_details(self, file_info):
        # TODO: setting to enable/disable display on each selection change
        # TODO: improve performance to avoid reloading everything.
        # TODO: add generators to qApp?
        settings = Settings()
        self.current_recording = Recording(file_info,
                                           spec_opts=settings.spectrogram_settings())
        print("height:" + str(self.lbl_spectro.height()))
        print("width:" + str(self.lbl_spectro.width()))
        self.update_spectrogram()
        self.time_slider.setMaximum(self.current_recording.duration)
        self.update_duration_lbl()

    def folder_query(self, folder_info):
        return ' & '.join(['{} == "{}"'.format(k, v) for k, v in folder_info.items()])
