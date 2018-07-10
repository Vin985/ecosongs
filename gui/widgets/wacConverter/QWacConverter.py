#!/usr/bin/env python

import os

import utils.files as files

from gui.tools.QWCThread import QWCThread
from gui.widgets.gui import Ui_Ecosongs
from PySide2.QtCore import Slot
from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox)

FILE_EXT = ".wac"
DEST_DIR = "wav"


class Ecosongs(QMainWindow, Ui_Ecosongs):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.wacConverter = QWCThread(self.logConsole)
        self.linkEvents()

    # Define callbacks when events happen
    def linkEvents(self):
        # Button pushed
        self.srcBrowseBtn.clicked.connect(self.browseSrc)
        self.destBrowseBtn.clicked.connect(self.browseDest)
        self.convertBtn.clicked.connect(self.convert)
        self.cancelBtn.clicked.connect(self.wacConverter.requestInterruption)
        # ComboBox
        self.srcPathInput.textChanged.connect(self.setRoot)
        self.destPathInput.textChanged.connect(self.setDest)
        # Checkbox
        self.isFolder.toggled.connect(self.folder_opt)
        self.overwrite.toggled.connect(self.setOverwrite)
        #Thread
        self.wacConverter.started.connect(self.start_thread)
        self.wacConverter.converting.connect(self.log)
        self.wacConverter.finished.connect(self.endConversion)

    def start_thread(self):
        self.logConsole.clear()

    # Update ui based on selected options
    def folder_opt(self):
        self.isRecursive.setEnabled(self.isFolder.isChecked())

    def setOverwrite(self):
        self.wacConverter.overwrite = self.overwrite.isChecked()

    def setRoot(self, text):
        self.wacConverter.setRootDir(text)

    def setDest(self, text):
        self.wacConverter.destDir = text

    def log(self, text, progress=False):
        self.logConsole.append(text)
        if progress:
            self.progressBar.setValue(self.progressBar.value() + 1)

    # Browse source directory
    def browseSrc(self):
        self.browse(self.srcPathInput, self.isFolder.isChecked())

        if self.isFolder.isChecked() and self.srcPathInput.text():
            # Create automatically a default path to dest dir if src is a folder
            if not self.destPathInput.text():
                self.destPathInput.setText(self.srcPathInput.text())
            # List all files to display
            self.getSourceFiles()
        self.showFiles()

    # Browse destination directory
    def browseDest(self):
        self.browse(self.destPathInput, True)

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
            (self.wacConverter.files, pattern) = QFileDialog.getOpenFileNames(
                self, "Choose files", default, "WAC files (*.wac)")
            if self.wacConverter.files:
                rootDir = os.path.dirname(self.wacConverter.files[0])

        # Update gui input
        textInput.setText(rootDir)

    def getSourceFiles(self):
        self.wacConverter.files = files.get_all_files(
            self.wacConverter.rootDir, FILE_EXT, self.isRecursive)

    def showFiles(self):
        [self.logConsole.append(fn) for fn in self.wacConverter.files]
        self.statusbar.showMessage(
            "%d file(s) found" % len(self.wacConverter.files))

    @Slot()
    def convert(self):
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

    def startConversion(self):
        print("start")
        self.initProgressBar(len(self.wacConverter.files))
        self.wacConverter.start()
        self.cancelBtn.setEnabled(True)
        self.convertBtn.setEnabled(False)

    @Slot()
    def endConversion(self):
        print("cancel")
        self.progressBar.setEnabled(False)
        self.progressBar.setValue(0)
        self.convertBtn.setEnabled(True)
        self.cancelBtn.setEnabled(False)

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


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    converter = Ecosongs()  # We set the form to be our ExampleApp (design)
    converter.show()
    sys.exit(app.exec_())
