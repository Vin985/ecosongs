from gui.widgets.audio.ui.audiomanager_ui import Ui_AudioManager
from PySide2.QtWidgets import QWidget


class AudioManager(QWidget, Ui_AudioManager):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        # self.treeView.setRootIsDecorated(False)
        # self.treeView.setUniformRowHeights(True)
        # self.treeView.setHeaderHidden(True)
