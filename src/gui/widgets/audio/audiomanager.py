import pandas as pd
from PIL import ImageQt

from audio.recording import Recording
from gui.utils.settings import Settings
from gui.utils.tree.recordingsTreeModel import RecordingsTreeModel
from gui.widgets.audio.ui.audiomanager_ui import Ui_AudioManager
from PySide2.QtGui import QPixmap, qApp
from PySide2.QtWidgets import QMenu, QWidget


class AudioManager(QWidget, Ui_AudioManager):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.init_tree()
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
        recording = Recording(file_info)
        # TODO: add slider to select duration and see complete spectrogram
        sample = recording.get_sample(0, 15)
        spec = sample.get_spectrogram(qApp.specgen, n_fft=512)
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
        idxs = self.tree_view.selectedIndexes()
        sel_folders = []
        sel_recs = []
        res = None
        for idx in idxs:
            item = idx.model().itemFromIndex(idx)
            data = item.data()
            if item.is_folder:
                sel_folders.append(data)
            else:
                sel_recs.append(data["Index"])
        tmp = [qApp.recordings.query(self.folder_query(folder)) for folder in sel_folders]
        tmp.append(qApp.get_recordings().iloc[sel_recs])
        res = pd.concat(tmp).drop_duplicates()
        qApp.recordings.compute_ACI(res.index.values, qApp.specgen)

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
