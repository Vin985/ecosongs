# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audiomanager.ui',
# licensing of 'audiomanager.ui' applies.
#
# Created: Thu Aug 23 17:11:17 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1530708810518
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AudioManager(object):
    def setupUi(self, AudioManager):
        AudioManager.setObjectName("AudioManager")
        AudioManager.resize(610, 456)
        self.gridLayout = QtWidgets.QGridLayout(AudioManager)
        self.gridLayout.setObjectName("gridLayout")
        self.treeView = QtWidgets.QTreeView(AudioManager)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)

        self.retranslateUi(AudioManager)
        QtCore.QMetaObject.connectSlotsByName(AudioManager)

    def retranslateUi(self, AudioManager):
        AudioManager.setWindowTitle(QtWidgets.QApplication.translate("AudioManager", "Form", None, -1))

