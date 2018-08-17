import os

from utils.filemanager import FileManager

from gui.widgets.dbmanager.ui.fileimport_ui import Ui_FileImport
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QFileDialog, QMessageBox, QWizard

# TODO: put files in config

DEST_DIR = "wav"


class FileImport(QWizard, Ui_FileImport):

    def __init__(self):
        super(self.__class__, self).__init__()
        # Initialize UI
        self.setupUi(self)
        self.site_manual.setVisible(not self.radio_site_auto.isChecked())
        self.file_manager = FileManager()
        # self.wacConverter = QWCThread(self.logConsole)
        self.registerFields()
        self.linkEvents()

    def registerFields(self):
        self.page1.registerField("src_path*", self.input_src_path)

    # Define callbacks when events happen

    def linkEvents(self):
        # Button pushed
        self.btn_browse_src.clicked.connect(self.browse_src)
        self.currentIdChanged.connect(self.change_page)
        # self.btn_browse_dest.clicked.connect(self.browse_dest)
        # self.btn_import.clicked.connect(self.import_files)
        # self.btn_cancel.clicked.connect(self.wacConverter.requestInterruption)
        # # Input fields
        self.input_src_path.textChanged.connect(self.set_root)
        # self.input_dest_path.textChanged.connect(self.set_dest)
        # # Checkbox
        self.radio_is_folder.buttonToggled.connect(self.folder_opt)
        self.radio_site_info.buttonToggled.connect(self.site_opt)
        self.checkbox_subfolders.toggled.connect(self.set_subfolders)
        # #Thread
        # self.wacConverter.started.connect(self.start_thread)
        # self.wacConverter.converting.connect(self.log)
        # self.wacConverter.finished.connect(self.end_conversion)

    def change_page(self):
        print("page changed:" + str(self.currentId()))

    def start_thread(self):
        self.logConsole.clear()

    # Called when any radio button for folder or file is selected
    def folder_opt(self):
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

    def site_opt(self):
        self.site_auto.setVisible(self.radio_site_auto.isChecked())
        self.site_manual.setVisible(not self.radio_site_auto.isChecked())

    def set_subfolders(self):
        self.recursive = self.checkbox_subfolders.isChecked()
        self.radio_site_manual.setEnabled(not self.checkbox_subfolders.isChecked())
        if self.radio_folder.isChecked():
            self.radio_site_auto.setChecked(True)
            self.site_auto.setVisible(True)
            self.site_manual.setVisible(False)

    def set_overwrite(self):
        self.file_manager.overwrite = self.checkbox_overwrite.isChecked()

    def set_root(self, path):
        self.file_manager.root_dir = path

    def set_dest(self, path):
        self.file_manager.dest_dir = path

    def log(self, text, progress=False):
        self.log_console.append(text)
        if progress:
            self.progress_bar.setValue(self.progress_bar.value() + 1)

    # Browse source directory
    def browse_src(self):
        self.browse(self.input_src_path, self.radio_folder.isChecked())
        if self.radio_folder.isChecked() and self.input_src_path.text():
            # Create automatically a default path to dest dir if src is a folder
            # if not self.input_dest_path.text():
            #     self.input_dest_path.setText(self.input_src_path.text())
            # List all files to display
            self.file_manager.get_all_files(self.checkbox_subfolders)
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
            if text:
                root_dir = text
        else:
            # We want to select files
            # TODO : add formats in config
            (files, pattern) = QFileDialog.getOpenFileNames(
                self, "Choose files", default,
                "Audio files (*.wav, *.wac);;WAV files (*.wav);;WAC files (*.wac)")
            self.file_manager.setFiles(files)

        # Update gui input
        text_input.setText(root_dir)

    def show_files(self):
        self.log_console.clear()
        [self.log_console.append(fn) for fn in self.file_manager.files]
        self.lbl_status.setText(
            "%d file(s) found" % len(self.file_manager.files))

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
