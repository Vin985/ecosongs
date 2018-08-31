import configparser

from PIL import ImageQt

from analyse.image import ImageGenerator
from analyse.spectrogram import SpectrogramGenerator
from audio.recording import Recording
from gui.utils.settings import Settings
from gui.widgets.audio.ui.audiomanager_ui import Ui_AudioManager
from PySide2.QtGui import QPixmap, qApp
from PySide2.QtWidgets import QWidget


class AudioManager(QWidget, Ui_AudioManager):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.link_events()
        settings = Settings()
        self.specgen = SpectrogramGenerator(settings.spectrogram_settings())
        self.imgen = ImageGenerator(settings.image_settings())
        # self.treeView.setRootIsDecorated(False)
        # self.treeView.setUniformRowHeights(True)
        # self.treeView.setHeaderHidden(True)

    def link_events(self):
        self.tree_explorer.show_recording_details.connect(self.show_recording_details)
        self.tree_explorer.show_folder_details.connect(self.show_folder_details)
        self.tree_explorer.compute_ACI.connect(self.compute_ACI)

    def show_recording_details(self, file_info):
        # TODO: improve performance to avoid reloading everything.
        # TODO: add generators to qApp?

        # TODO: add recording object somewhere
        recording = Recording(file_info)
        # TODO: add slider to select duration and see complete spectrogram
        sample = recording.get_sample(0, 15)
        spec = sample.get_spectrogram(self.specgen, n_fft=512)
        # TODO: externalize ratio pixel/duration
        # TODO: save image somewhere
        im = self.imgen.spec2img(spec.spec, size=(int(299 * spec.duration / 1.5), 299))
        img = ImageQt.ImageQt(im)
        pixmap = QPixmap.fromImage(img)
        # TODO: add multiple spectrograms?
        self.spectrogram.setPixmap(pixmap)
        # im.show()

    def show_folder_details(self, folder_info):
        query = ' & '.join(['{} == "{}"'.format(k, v) for k, v in folder_info.items()])
        res = qApp.recordings.query(query)
        self.spectrogram.setText("{} recordings found!".format(res.shape[0]))

    def compute_ACI(self):
