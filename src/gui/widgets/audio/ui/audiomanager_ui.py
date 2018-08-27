# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audiomanager.ui',
# licensing of 'audiomanager.ui' applies.
#
# Created: Sun Aug 26 13:59:40 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1530708810518
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AudioManager(object):
    def setupUi(self, AudioManager):
        AudioManager.setObjectName("AudioManager")
        AudioManager.resize(984, 682)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(AudioManager)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter = QtWidgets.QSplitter(AudioManager)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeExplorer = TreeExplorer(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeExplorer.sizePolicy().hasHeightForWidth())
        self.treeExplorer.setSizePolicy(sizePolicy)
        self.treeExplorer.setMinimumSize(QtCore.QSize(250, 0))
        self.treeExplorer.setObjectName("treeExplorer")
        self.details_pane = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details_pane.sizePolicy().hasHeightForWidth())
        self.details_pane.setSizePolicy(sizePolicy)
        self.details_pane.setObjectName("details_pane")
        self.gridLayout = QtWidgets.QGridLayout(self.details_pane)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.details_pane)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.name = QtWidgets.QLabel(self.details_pane)
        self.name.setText("")
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.details_pane)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.details_pane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.year = QtWidgets.QLabel(self.details_pane)
        self.year.setObjectName("year")
        self.gridLayout.addWidget(self.year, 2, 1, 1, 1)
        self.path = QtWidgets.QLabel(self.details_pane)
        self.path.setText("")
        self.path.setObjectName("path")
        self.gridLayout.addWidget(self.path, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.details_pane)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.splitter)

        self.retranslateUi(AudioManager)
        QtCore.QMetaObject.connectSlotsByName(AudioManager)

    def retranslateUi(self, AudioManager):
        AudioManager.setWindowTitle(QtWidgets.QApplication.translate("AudioManager", "Form", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("AudioManager", "Path", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("AudioManager", "Name", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("AudioManager", "Year", None, -1))
        self.year.setText(QtWidgets.QApplication.translate("AudioManager", "TextLabel", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("AudioManager", "compute ACI", None, -1))

from gui.widgets.treeexplorer.treeexplorer import TreeExplorer
