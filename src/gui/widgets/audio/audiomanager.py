import configparser

from PIL import ImageQt

from analyse.image import ImageGenerator
from analyse.spectrogram import SpectrogramGenerator
from audio.recording import Recording
from gui.widgets.audio.ui.audiomanager_ui import Ui_AudioManager
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget


class AudioManager(QWidget, Ui_AudioManager):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.link_events()
        # self.treeView.setRootIsDecorated(False)
        # self.treeView.setUniformRowHeights(True)
        # self.treeView.setHeaderHidden(True)

    def link_events(self):
        self.tree_explorer.show_file_details.connect(self.show_details)

    def show_details(self, file_info):
        config = configparser.ConfigParser()
        config.read("ecosongs.conf")

        specgen = SpectrogramGenerator(config)
        imgen = ImageGenerator(config)
        recording = Recording(file_info)
        sample = recording.get_sample(0, 15)
        spec = sample.get_spectrogram(specgen, n_fft=512)
        im = imgen.spec2img(spec.spec, size=(int(299 * spec.duration / 1.5), 299))
        img = ImageQt.ImageQt(im)
        pixmap = QPixmap.fromImage(img)
        self.spectrogram.setPixmap(pixmap)
        # im.show()
