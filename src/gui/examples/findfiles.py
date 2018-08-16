#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the PySide examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################
"""PySide2 port of the widgets/dialogs/findfiles example from Qt v5.x"""

from PySide2 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.browseSrcButton = self.createButton("&Browse...", self.browseSrc)
        self.browseDestButton = self.createButton("&Browse...",
                                                  self.browseDest)
        self.convertButton = self.createButton("&Convert", self.convert)

        self.logConsole = QtWidgets.QTextEdit()

        self.srcComboBox = self.createComboBox("Source",
                                               QtCore.QDir.currentPath())
        self.destComboBox = self.createComboBox("Destination",
                                                QtCore.QDir.currentPath())

        srcLabel = QtWidgets.QLabel("Source:")
        destLabel = QtWidgets.QLabel("Destination:")
        self.logLabel = QtWidgets.QLabel()

        buttonsLayout = QtWidgets.QHBoxLayout()
        buttonsLayout.addStretch()
        buttonsLayout.addWidget(self.convertButton)

        mainLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(srcLabel, 0, 0)
        mainLayout.addWidget(self.srcComboBox, 0, 1)
        mainLayout.addWidget(self.browseSrcButton, 0, 2)
        mainLayout.addWidget(destLabel, 1, 0)
        mainLayout.addWidget(self.destComboBox, 1, 1)
        mainLayout.addWidget(self.browseDestButton, 1, 2)
        mainLayout.addWidget(self.logConsole, 3, 0, 1, 3)
        mainLayout.addLayout(buttonsLayout, 4, 0, 1, 3)
        self.setLayout(mainLayout)

        self.setWindowTitle("Convert Files")

    def browseSrc(self):
        self.browse(self.srcComboBox)

    def browseDest(self):
        self.browse(self.destComboBox)

    def browse(self, comboBox):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Choose directory", QtCore.QDir.currentPath())

        if directory:
            if comboBox.findText(directory) == -1:
                comboBox.addItem(directory)

            comboBox.setCurrentIndex(comboBox.findText(directory))

    def convert(self):
        srcDir = self.srcComboBox.currentText()
        destDir = self.destComboBox.currentText()

        self.currentDir = QtCore.QDir(srcDir)
        fileName = "*.wac"
        files = self.currentDir.entryList(
            [fileName], QtCore.QDir.Files | QtCore.QDir.NoSymLinks)

        self.showFiles(files)

    def showFiles(self, files):
        self.logConsole.append("%d file(s) found: " % len(files))
        for fn in files:
            print(fn)
            print(type(fn))
            file_ = QtCore.QFile(self.currentDir.absoluteFilePath(fn))
            info = QtCore.QFileInfo(file_)
            self.logConsole.append("Found " + info.baseName() + " with size " +
                                   str(info.size()))

    def createButton(self, text, callback):
        button = QtWidgets.QPushButton(text)
        button.clicked.connect(callback)
        return button

    def logComboBox(self):
        sender = self.sender()
        message = sender.objectName() + " is set to: " + sender.currentText()
        self.logConsole.append(message)

    def createComboBox(self, name, text=""):
        comboBox = QtWidgets.QComboBox()
        comboBox.setObjectName(name)
        #comboBox.activated.connect(self.logComboBox)
        comboBox.setEditable(True)
        comboBox.addItem(text)
        comboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                               QtWidgets.QSizePolicy.Preferred)
        return comboBox


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
