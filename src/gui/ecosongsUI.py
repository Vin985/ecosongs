from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMainWindow
from gui.ecosongs_ui import Ui_Ecosongs


class EcosongsUI(QMainWindow, Ui_Ecosongs):
    def __init__(self):
        super().__init__()
        self.settingsDialog = None
        self.setupUi(self)
        self.loadConfig()
        self.linkEvents()
        self.current_page = 0
        self.change_page(self.sidebar.currentRow())

    def loadConfig(self):
        # TODO: load config
        pass

    # Define callbacks when events happen
    def linkEvents(self):
        # Link menu actions
        self.linkActions()

        # Navigation: change page when icon is clicked
        self.sidebar.currentRowChanged.connect(self.change_page)

    def linkActions(self):
        self.aExit.triggered.connect(self.exit)
        self.aSettings.triggered.connect(self.show_settings)
        self.action_import_files.triggered.connect(self.show_import_dialog)

    def initProgressBar(self, maxValue):
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximum(maxValue)
        # self.progressBar.setValue(0)

    @Slot()
    def show_settings(self):
        print("show settings menu")
        from gui.widgets.dialogs.settingsdialog import SettingsDialog
        self.settingsDialog = SettingsDialog()
        self.settingsDialog.show()

    @Slot()
    def exit(self):
        QApplication.quit()

    def init_page_display(self, index):
        page = self.pages.widget(index)
        page.enter_page()

    def clear_page_display(self, index):
        page = self.pages.widget(index)
        page.leave_page()

    def change_page(self, index):
        self.clear_page_display(self.current_page)
        self.init_page_display(index)
        self.pages.setCurrentIndex(index)
        self.current_page = index

    def refresh_page(self):
        # TODO: refresh current page if needed
        pass

    def show_import_dialog(self):
        from gui.widgets.dialogs.file_import_wizard import FileImportWizard
        self.file_import = FileImportWizard()
        self.file_import.finished.connect(self.refresh_page)
        self.file_import.show()
