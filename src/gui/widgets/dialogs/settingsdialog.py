from PySide2.QtWidgets import QDialog

from gui.widgets.dialogs.ui.settingsdialog_ui import Ui_SettingsDialog


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.link_events()

    def link_events(self):
        # Navigation: change page when icon is clicked
        self.menu_categories.currentRowChanged.connect(
            self.menu_pages.setCurrentIndex)
