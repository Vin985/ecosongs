from gui.widgets.menus.ui.settingsmenu_ui import Ui_SettingsMenu
from PySide2.QtWidgets import QDialog


class SettingsMenu(QDialog, Ui_SettingsMenu):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.linkEvents()

    # Define callbacks when events happen

    def linkEvents(self):
        # Navigation: change page when icon is clicked
        self.menu_categories.currentRowChanged.connect(self.menu_pages.setCurrentIndex)
