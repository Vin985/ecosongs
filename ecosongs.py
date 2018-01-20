#!/usr/bin/env python

import os

import utils.files as files
from utils.wacconverter import WacConverter

from gui.gui import Ui_Ecosongs
from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox)

FILE_EXT = ".wac"
DEST_DIR = "wav"


class Ecosongs(QMainWindow, Ui_Ecosongs):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.linkEvents()
        self.wacConverter = WacConverter()

    # Define callbacks when events happen
    def linkEvents(self):
        # Button pushed
        self.srcBrowseBtn.clicked.connect(self.browseSrc)
        self.destBrowseBtn.clicked.connect(self.browseDest)
        self.convertBtn.clicked.connect(self.convert)
        # ComboBox
        self.srcPathInput.textChanged.connect(self.setRoot)
        self.destPathInput.textChanged.connect(self.setDest)
        # Checkbox
        self.isFolder.toggled.connect(self.folder_opt)
        #self.keepStruct.toggled.connect(self.struct_opt)

    # Update ui based on selected options
    def folder_opt(self):
        self.isRecursive.setEnabled(self.isFolder.isChecked())
        #self.keepStruct.setEnabled(self.isFolder.isChecked())

    def struct_opt(self):
        self.wacConverter.keepStruct = self.keepStruct.isChecked()

    def setRoot(self, text):
        self.wacConverter.rootDir = text  #self.srcPathInput.text()

    def setDest(self, text):
        self.wacConverter.destDir = text  #self.destPathInput.text()

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
        self.wacConverter.rootDir = self.srcPathInput.text()
        self.wacConverter.files = files.get_all_files(
            self.wacConverter.rootDir, FILE_EXT, self.isRecursive)

    def showFiles(self):
        [self.logConsole.append(fn) for fn in self.wacConverter.files]
        self.statusbar.showMessage(
            "%d file(s) found" % len(self.wacConverter.files))

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
                self.logConsole.clear()
                self.wacConverter.files_to_wav(self.logConsole)
        except AttributeError:
            self.showAlert(
                "No files are selected, please select at least one file")

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


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    converter = Ecosongs()  # We set the form to be our ExampleApp (design)
    converter.show()
    sys.exit(app.exec_())
