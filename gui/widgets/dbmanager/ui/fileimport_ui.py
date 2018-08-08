# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileimport.ui',
# licensing of 'fileimport.ui' applies.
#
# Created: Wed Aug  8 17:22:23 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1530708810518
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FileImport(object):
    def setupUi(self, FileImport):
        FileImport.setObjectName("FileImport")
        FileImport.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(FileImport)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(FileImport)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(FileImport)
        QtCore.QMetaObject.connectSlotsByName(FileImport)

    def retranslateUi(self, FileImport):
        FileImport.setWindowTitle(QtWidgets.QApplication.translate("FileImport", "Form", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("FileImport", "Import file", None, -1))

