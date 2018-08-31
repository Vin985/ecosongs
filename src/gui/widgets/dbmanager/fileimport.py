import os

from utils.filemanager import FileManager

from gui.utils.dataframeTableModel import DataFrameTableModel
from gui.utils.settings import Settings
from gui.widgets.dbmanager.ui.fileimport_ui import Ui_FileImport
from PySide2.QtCore import QObject, QSortFilterProxyModel, Signal, Slot
from PySide2.QtGui import qApp
from PySide2.QtWidgets import QFileDialog, QMessageBox, QWizard

# TODO: put files in config

DEST_DIR = "wav"


class QFileManager(QObject, FileManager):
    logging = Signal(str, bool)
    filesLoaded = Signal()

    def __init__(self):
        QObject.__init__(self)
        settings = Settings()
        FileManager.__init__(self, sites=settings.sites_path)

    def log(self, text):
        self.logging.emit(text, False)

    def files_loaded(self):
        # TODO: change to use persistence model
        qApp.save_data("recordings", self.file_infos, format="t")
        self.filesLoaded.emit()


class FileImport(QWizard, Ui_FileImport):

    def __init__(self):
        super(self.__class__, self).__init__()
        # Initialize UI
        self.setupUi(self)
        self.site_manual.setVisible(not self.radio_site_auto.isChecked())
        self.file_manager = QFileManager()
        # self.wacConverter = QWCThread(self.logConsole)
        self.registerFields()
        self.linkEvents()

    def registerFields(self):
        self.page1.registerField("src_path*", self.input_src_path)

    # Define callbacks when events happen
    def linkEvents(self):
        # Buttons
        self.btn_browse_src.clicked.connect(self.browse_src)
        # self.btn_browse_dest.clicked.connect(self.browse_dest)
        # self.btn_import.clicked.connect(self.import_files)
        # self.btn_cancel.clicked.connect(self.wacConverter.requestInterruption)
        # Input fields
        # self.input_src_path.textChanged.connect(self.set_root)
        # self.input_dest_path.textChanged.connect(self.set_dest)
        # Radio
        self.radio_is_folder.buttonToggled.connect(self.folder_options)
        self.radio_site_info.buttonToggled.connect(self.site_info_options)
        # Checkbox
        self.checkbox_subfolders.toggled.connect(self.subfolders_options)
        # #Thread
        self.file_manager.logging.connect(self.log)
        self.file_manager.filesLoaded.connect(self.show_files)
        # self.wacConverter.started.connect(self.start_thread)
        # self.wacConverter.converting.connect(self.log)
        # self.wacConverter.finished.connect(self.end_conversion)

    def initializePage(self, id):
        if id == 1:
            self.initialize_page1()
            # getattr(self, "initialize_page" + str(id))()

    # TODO : Validate manual entries

    def initialize_page1(self):
        site_info = {}
        if (self.radio_site_auto.isChecked()):
            for i in range(1, 4):
                tmp = getattr(self, "idx_" + str(i)).currentText().lower()
                site_info[tmp] = i
        else:
            site_info["site"] = self.input_site
            site_info["year"] = self.input_year
            site_info["plot"] = self.input_plot

        self.file_manager.options = {"folder": self.radio_folder.isChecked(),
                                     "recursive": self.checkbox_subfolders.isChecked(),
                                     "recorder": self.radio_recorders.button(self.radio_recorders.checkedId()).text(),
                                     "folder_hierarchy": self.radio_site_auto.isChecked(),
                                     "site_info": site_info}
        self.file_manager.get_files()

    # Called when any radio button for folder or file is selected

    def folder_options(self):
        # Only enable subfolder option if import folder is selected
        self.checkbox_subfolders.setEnabled(self.radio_folder.isChecked())
        # If import files
        if self.radio_file.isChecked():
            # Allow user to enter site info manually
            self.radio_site_manual.setEnabled(True)
            # else if subfolders are checked
        elif self.checkbox_subfolders.isChecked():
            # Disable manual info and force automatic detection
            # This is because multiple site can be imported
            self.radio_site_manual.setEnabled(False)
            self.radio_site_auto.setChecked(True)
            self.site_auto.setVisible(True)
            self.site_manual.setVisible(False)

    def site_info_options(self):
        self.site_auto.setVisible(self.radio_site_auto.isChecked())
        self.site_manual.setVisible(not self.radio_site_auto.isChecked())

    def subfolders_options(self):
        self.radio_site_manual.setEnabled(not self.checkbox_subfolders.isChecked())
        if self.radio_folder.isChecked():
            self.radio_site_auto.setChecked(True)
            self.site_auto.setVisible(True)
            self.site_manual.setVisible(False)

    def log(self, text, progress=False):
        # self.log_console.append(text)
        print(text)
        if progress:
            self.progress_bar.setValue(self.progress_bar.value() + 1)

    # Browse source directory

    def browse_src(self):
        self.browse(self.input_src_path, self.radio_folder.isChecked())
        # if self.radio_folder.isChecked() and self.input_src_path.text():
        # Create automatically a default path to dest dir if src is a folder
        # if not self.input_dest_path.text():
        #     self.input_dest_path.setText(self.input_src_path.text())
        # List all files to display
        # self.file_manager.get_all_files(self.checkbox_subfolders)
        # TODO: extract metadata
        # self.show_files()

        # Browse destination directory
    def browse_dest(self):
        self.browse(self.input_dest_path, True)

    # Generic method to browse for files
    def browse(self, text_input, is_folder):
        default = os.getcwd()
        if is_folder:
            # We want to select a folder
            if text_input.text():
                default = text_input.text()
            text = QFileDialog.getExistingDirectory(self, "Choose directory",
                                                    default)
            self.file_manager.root_dir = text
        else:
            # We want to select files
            # TODO : add formats in config
            (files, pattern) = QFileDialog.getOpenFileNames(
                self, "Choose files", default,
                "Audio files (*.wav, *.WAV, *.wac);;WAV files (*.wav, *.WAV);;WAC files (*.wac)")
            text = "; ".join(files)
            self.file_manager.file_paths = files

        # Update gui input
        text_input.setText(text)

    def show_files(self):
        if self.file_manager.file_infos.empty:
            self.table_files.setEnabled(False)
        else:
            model = self.file_manager.file_infos
            # TODO: date format in config/options
            model["date"] = model["date"].dt.strftime("%Y-%m-%d %H:%M:%S")
            model = DataFrameTableModel(model)
            proxyModel = QSortFilterProxyModel()
            proxyModel.setSourceModel(model)
            self.table_files.setModel(proxyModel)
            self.table_files.resizeColumnsToContents()
        # self.log_console.clear()
        # self.log_console.append("\n".join(self.file_manager.file_paths))
        self.lbl_status.setText("%d file(s) found" % len(self.file_manager.file_paths))

    @Slot()
    def import_files(self):
        try:
            if not self.file_manager.files:
                self.showAlert(
                    "No files are selected, please select at least one file")
                return ()
            if not self.file_manager.destDir:
                self.showAlert(
                    "No destination folder has been selected, please select one"
                )
                return ()
            ret = self.showConfirmBox(
                "Convert selected files to wav?",
                "{0} file(s) will be converted and saved in {1}".format(
                    len(self.file_manager.files), self.file_manager.dest_dir))
            if ret == QMessageBox.Ok:
                self.startConversion()

        except AttributeError:
            self.showAlert(
                "No files are selected, please select at least one file")

    def start_thread(self):
        self.logConsole.clear()

    def start_conversion(self):
        print("start")
        self.initProgressBar(len(self.file_manager.files))
        self.file_manager.start()
        self.btn_cancel.setEnabled(True)
        self.btn_import.setEnabled(False)

    @Slot()
    def end_conversion(self):
        print("cancel")
        self.progress_bar.setEnabled(False)
        self.progress_bar.setValue(0)
        self.btn_cancel.setEnabled(False)
        self.btn_import.setEnabled(True)

    def showAlert(self, text):
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.setIcon(QMessageBox.Critical)
        return (msgBox.exec_())

    def showConfirmBox(self, text, info):
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.setInformativeText(info)
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Ok)
        return (msgBox.exec_())

    def initProgressBar(self, maxValue):
        self.progress_bar.setEnabled(True)
        self.progress_bar.setMaximum(maxValue)
        # self.progressBar.setValue(0)
