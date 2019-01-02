from gui.utils.settings import Settings
from gui.widgets.menus.ui.settingsdialog_ui import Ui_SettingsDialog
from PySide2.QtWidgets import QDialog, QWidget


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.linkEvents()

    def linkEvents(self):
        # Navigation: change page when icon is clicked
        self.menu_categories.currentRowChanged.connect(self.menu_pages.setCurrentIndex)
