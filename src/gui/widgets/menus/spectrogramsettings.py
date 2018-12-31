from gui.widgets.menus.ui.spectrogramsettings_ui import Ui_SpectrogramSettings
from PySide2.QtWidgets import QWidget


class SpectrogramSettings(QWidget, Ui_SpectrogramSettings):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
