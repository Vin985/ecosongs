import copy
import itertools
from multiprocessing import Pool, Queue

import pandas as pd
from PIL import ImageQt

from analyse.indexes import ACI
from audio.recording import Recording
from gui.threads.QIndexThread import QIndexThread
from gui.utils.tree.recordingsTreeModel import RecordingsTreeModel
from gui.widgets.audio.ui.audiomanager_ui import Ui_AudioManager
from PySide2.QtConcurrent import QtConcurrent
from PySide2.QtGui import QPixmap, qApp
from PySide2.QtWidgets import QMenu, QWidget


def get_ACI(self, rec):
    return ACI(recording=rec)


class AudioManager(QWidget, Ui_AudioManager):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.init_tree()
        self.index_thread = QIndexThread()
        self.link_events()
        self.add_actions()

        # self.treeView.setRootIsDecorated(False)
        # self.treeView.setUniformRowHeights(True)
        # self.treeView.setHeaderHidden(True)

    def init_tree(self):
        recordings = qApp.get_recordings()
        self.tree_view.setModel(RecordingsTreeModel(self, recordings))

    def add_actions(self):
        self.tree_view.addAction(self.action_ACI)

    def link_events(self):
        self.tree_view.selectionModel().selectionChanged.connect(self.tree_selection_changed)
        self.action_ACI.triggered.connect(self.compute_ACI)
        self.index_thread.progression.connect(self.update_progression)
        self.index_thread.finished.connect(self.get_results)

    def get_results(self):
        print("finished")
        for item in self.index_thread.res:
            print(item)
        print(self.index_thread.res)

    def update_progression(self, progress):
        print(progress)

    def tree_selection_changed(self, new, old):
        # TODO: handle multiple selection
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
        recording = Recording(file_info, specgen=qApp.specgen)
        # TODO: add slider to select duration and see complete spectrogram
        sample = recording.get_sample(0, 15)
        spec = sample.get_spectrogram()
        # TODO: externalize ratio pixel/duration
        # TODO: save image somewhere
        im = qApp.imgen.spec2img(spec.spec, size=(int(299 * spec.duration / 1.5), 299))
        img = ImageQt.ImageQt(im)
        pixmap = QPixmap.fromImage(img)
        # TODO: add multiple spectrograms?
        self.spectrogram.setPixmap(pixmap)
        # im.show()

    def show_folder_details(self, folder_info):
        query = self.folder_query(folder_info)
        res = qApp.recordings.query(query)
        self.spectrogram.setText("{} recordings found!".format(res.shape[0]))

    def folder_query(self, folder_info):
        return(' & '.join(['{} == "{}"'.format(k, v) for k, v in folder_info.items()]))

    def recording_query():
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
        tmp = [qApp.recordings.query(self.folder_query(folder)) for folder in sel_folders]
        # Get individually selected recordings
        tmp.append(qApp.get_recordings().iloc[sel_recs])
        # Get one list of unique selected files
        res = pd.concat(tmp).drop_duplicates()
        # Load files if not already in memory
        recs = qApp.load_recordings(res.index.values)
        # Get list of all loaded recordings
        print(recs)
        # Compute ACIs
        # TODO: clean up!
        self.index_thread.spec_opts = {'to_db': False, 'remove_noise': False}
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
