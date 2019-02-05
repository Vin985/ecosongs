import pandas as pd
from PIL import ImageQt
from PySide2.QtGui import QPixmap, qApp
from PySide2.QtWidgets import QMenu, QWidget

from analysis.indexes import ACI, ACITable
from audio.recording import Recording
from gui.threads.QIndexThread import QIndexThread
from gui.utils.settings import Settings
from gui.utils.tree.recordingsTreeModel import RecordingsTreeModel
from gui.widgets.audio.ui.audiomanager_ui import Ui_AudioManager

import utils.commons as utils


def get_ACI(rec):
    return ACI(recording=rec)


def update_path(path):
    new = path.replace("Seagate Backup Plus Drive", "Backup")
    return new


class AudioManager(QWidget, Ui_AudioManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_tree()
        self.index_thread = QIndexThread()
        self.link_events()
        self.add_actions()
        self.current_recording = None

        # aci_table = TableModel(ACI.COLUMNS, df=pd.DataFrame(),
        #                        dbmanager=qApp.dbmanager, table="ACI")
        aci_table = ACITable(dbmanager=qApp.dbmanager)
        print(aci_table.df)
        # aci_table.save()

        # recs = qApp.get_recordings()
        # recs = recs[recs.site != "2018"]
        # qApp.recordings.create(recs, save=True)
        # recs["path"] = recs["path"].map(update_path)
        # print(recs["path"])
        # qApp.recordings.create(recs, save=True)
        # aci_table.save()

        self.tree_view.setRootIsDecorated(True)
        # self.treeView.setUniformRowHeights(True)
        # self.treeView.setHeaderHidden(True)

    def init_tree(self):
        recordings = qApp.get_recordings()
        categories = ["year", "site", "plot"]

        model = RecordingsTreeModel(self, recordings, categories=categories)
        self.tree_view.setModel(model)
        self.tree_view.expand(model.item(0, 0).index())
        self.show_folder_details()

    def add_actions(self):
        self.tree_view.addAction(self.action_ACI)

    def link_events(self):
        self.tree_view.selectionModel().selectionChanged.connect(self.tree_selection_changed)
        self.action_ACI.triggered.connect(self.compute_ACI)
        self.index_thread.progression.connect(self.update_progression)
        self.index_thread.finished.connect(self.get_results)
        self.time_slider.valueChanged.connect(self.update_spectrogram)

    def get_results(self):
        print("finished")

        print(self.index_thread.res)
        acis = pd.DataFrame(self.index_thread.res)
        print(acis)
        # if not acis.empty:
        #     aci_table = TableModel(ACI.COLUMNS, dbmanager=qApp.dbmanager, table="ACI")
        #     aci_table.add(acis, save=True)
        # acis = pd.DataFrame([aci.to_dict() for aci in self.index_thread.res])
        # for item in self.index_thread.res:
        #     print(item)
        # print(self.index_thread.res)

    def update_progression(self, progress):
        print(progress)

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

    def show_recording_details(self, file_info):
        # TODO: setting to enable/disable display on each selection change
        # TODO: improve performance to avoid reloading everything.
        # TODO: add generators to qApp?

        # TODO: add recording object somewhere
        settings = Settings()
        self.current_recording = Recording(file_info,
                                           spec_opts=settings.spectrogram_settings())
        # TODO: add slider to select duration and see complete spectrogram
        # sample = self.current_recording.get_sample(0, 15)
        print("height:" + str(self.lbl_spectro.height()))
        print("width:" + str(self.lbl_spectro.width()))
        self.update_spectrogram()
        self.time_slider.setMaximum(self.current_recording.duration)
        # update the time label
        self.update_duration_lbl()
        # im.show()

    def update_spectrogram(self):
        # TODO: add spectrogram options
        max_duration = self.lbl_spectro.width() * 1.5 / 299
        spec = self.current_recording.spectrogram.get_subspec(self.time_slider.value(), max_duration)
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

        # total_duration = str(datetime.timedelta(seconds=total_secs))
        self.lbl_spectro.setText(
            "{} recordings representing {}of audio found!".format(res.shape[0], duration))

    def folder_query(self, folder_info):
        return(' & '.join(['{} == "{}"'.format(k, v) for k, v in folder_info.items()]))

    def recording_query(self):
        return()

    def compute_ACI(self):
        # default value for result containers
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

        # Get list of all loaded recordings
        # Compute ACIs
        # TODO: clean up!
        settings = Settings()
        spec_opts = settings.spectrogram_settings()
        spec_opts.update({'to_db': False, 'remove_noise': False})
        self.index_thread.spec_opts = spec_opts
        self.index_thread.recordings = recs
        self.index_thread.start()
        # pool = Pool(5)
        # acis = pool.map(ACI, recs)
        # pool.close()
        # print(acis)

        # folder_query = {key: [] for key in idx.model().categories}
        # for dic in sel_folders:
        #     for k, v in dic.items():
        #         if v not in folder_query[k]:
        #             folder_query[k].append(v)
        # print(folder_query)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.action_ACI)
        menu.exec_(event.globalPos())
