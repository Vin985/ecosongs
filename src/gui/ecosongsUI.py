from gui.ecosongs_ui import Ui_Ecosongs
from gui.widgets.menus.settingsmenu import SettingsMenu
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMainWindow


class EcosongsUI(QMainWindow, Ui_Ecosongs):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.loadConfig()
        self.linkEvents()

    def loadConfig(self):
        # TODO: load config
        pass

    # Define callbacks when events happen
    def linkEvents(self):
        # Link menu actions
        self.linkActions()

        # Navigation: change page when icon is clicked
        self.sidebar.currentRowChanged.connect(self.pages.setCurrentIndex)

    def linkActions(self):
        self.aExit.triggered.connect(self.exit)
        self.aSettings.triggered.connect(self.show_settings)

    def initProgressBar(self, maxValue):
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximum(maxValue)
        # self.progressBar.setValue(0)

    @Slot()
    def show_settings(self):
        print("show settings menu")
        self.settingsMenu = SettingsMenu()
        self.settingsMenu.show()

    @Slot()
    def exit(self):
        QApplication.quit()
