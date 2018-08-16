import os

import utils.files as files

from gui.threads.QWCThread import QWCThread
from gui.widgets.dbmanager.ui.fileimport_ui import Ui_FileImport
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QFileDialog, QMessageBox, QWizard

# TODO: put files in config
FILE_EXT = (".wac", ".wav", ".WAV")
DEST_DIR = "wav"


class FileImport(QWizard, Ui_FileImport):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.site_opt.setVisible(not self.radio_folder.isChecked())
        self.wacConverter = QWCThread(self.logConsole)
        self.linkEvents()

    # Define callbacks when events happen
    def linkEvents(self):
        # Button pushed
        self.btn_browse_src.clicked.connect(self.browse_src)
        # self.btn_browse_dest.clicked.connect(self.browse_dest)
        # self.btn_import.clicked.connect(self.import_files)
        # self.btn_cancel.clicked.connect(self.wacConverter.requestInterruption)
        # # Input fields
        self.input_src_path.textChanged.connect(self.set_root)
        # self.input_dest_path.textChanged.connect(self.set_dest)
        # # Checkbox
        self.radio_is_folder.buttonToggled.connect(self.folder_opt)
        #self.checkbox_overwrite.toggled.connect(self.set_overwrite)
        # #Thread
        # self.wacConverter.started.connect(self.start_thread)
        # self.wacConverter.converting.connect(self.log)
        # self.wacConverter.finished.connect(self.end_conversion)

    def start_thread(self):
        self.logConsole.clear()

    # Update ui based on selected options
    def folder_opt(self):
        self.checkbox_subfolders.setEnabled(self.radio_folder.isChecked())
        self.site_opt.setVisible(not self.radio_folder.isChecked())

    def set_overwrite(self):
        self.wacConverter.overwrite = self.checkbox_overwrite.isChecked()

    def set_root(self, text):
        self.wacConverter.setRootDir(text)

    def set_dest(self, text):
        self.wacConverter.destDir = text

    def log(self, text, progress=False):
        self.logConsole.append(text)
        if progress:
            self.progressBar.setValue(self.progressBar.value() + 1)

    # Browse source directory
    def browse_src(self):
        self.browse(self.input_src_path, self.radio_folder.isChecked())

        if self.radio_folder.isChecked() and self.input_src_path.text():
            # Create automatically a default path to dest dir if src is a folder
            # if not self.input_dest_path.text():
            #     self.input_dest_path.setText(self.input_src_path.text())
            # List all files to display
            self.getSourceFiles()
        self.showFiles()

    # Browse destination directory
    def browse_dest(self):
        self.browse(self.input_dest_path, True)

    # Generic method to browse for files
    def browse(self, textInput, isFolder):
        default = os.getcwd()
        if isFolder:
            # We want to select a folder
            if textInput.text():
                default = textInput.text()
            text = QFileDialog.getExistingDirectory(self, "Choose directory",
                                                    default)
            if text:
                rootDir = text
        else:
            # We want to select files
            # TODO : add formats in config
            (self.wacConverter.files, pattern) = QFileDialog.getOpenFileNames(
                self, "Choose files", default, "Audio files (*.wav, *.wac);;WAV files (*.wav);;WAC files (*.wac)")
            if self.wacConverter.files:
                rootDir = os.path.dirname(self.wacConverter.files[0])

        # Update gui input
        textInput.setText(rootDir)

    def getSourceFiles(self):
        self.wacConverter.files = files.get_all_files(
            self.wacConverter.rootDir, FILE_EXT, self.checkbox_subfolders)

    def showFiles(self):
        self.logConsole.clear()
        [self.logConsole.append(fn) for fn in self.wacConverter.files]
        self.lbl_status.setText(
            "%d file(s) found" % len(self.wacConverter.files))

    @Slot()
    def import_files(self):
        try:
            if not self.wacConverter.files:
                self.showAlert(
                    "No files are selected, please select at least one file")
                return ()
            if not self.wacConverter.destDir:
                self.showAlert(
                    "No destination folder has been selected, please select one"
                )
                return ()
            ret = self.showConfirmBox(
                "Convert selected files to wav?",
                "{0} file(s) will be converted and saved in {1}".format(
                    len(self.wacConverter.files), self.wacConverter.destDir))
            if ret == QMessageBox.Ok:
                self.startConversion()

        except AttributeError:
            self.showAlert(
                "No files are selected, please select at least one file")

    def start_conversion(self):
        print("start")
        self.initProgressBar(len(self.wacConverter.files))
        self.wacConverter.start()
        self.btn_cancel.setEnabled(True)
        self.btn_import.setEnabled(False)

    @Slot()
    def end_conversion(self):
        print("cancel")
        self.progressBar.setEnabled(False)
        self.progressBar.setValue(0)
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
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximum(maxValue)
        #self.progressBar.setValue(0)
