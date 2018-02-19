# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ecosongs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Ecosongs(object):
    def setupUi(self, Ecosongs):
        Ecosongs.setObjectName("Ecosongs")
        Ecosongs.resize(903, 676)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ecosongs.sizePolicy().hasHeightForWidth())
        Ecosongs.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Ecosongs)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 873, 505))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setEnabled(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 2)
        self.sourceLabel = QtWidgets.QLabel(self.groupBox)
        self.sourceLabel.setMaximumSize(QtCore.QSize(169, 16777215))
        self.sourceLabel.setObjectName("sourceLabel")
        self.gridLayout.addWidget(self.sourceLabel, 2, 0, 1, 1)
        self.destinationLabel = QtWidgets.QLabel(self.groupBox)
        self.destinationLabel.setObjectName("destinationLabel")
        self.gridLayout.addWidget(self.destinationLabel, 3, 0, 1, 1)
        self.logConsole = QtWidgets.QTextEdit(self.groupBox)
        self.logConsole.setObjectName("logConsole")
        self.gridLayout.addWidget(self.logConsole, 4, 0, 1, 4)
        self.srcBrowseBtn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.srcBrowseBtn.sizePolicy().hasHeightForWidth())
        self.srcBrowseBtn.setSizePolicy(sizePolicy)
        self.srcBrowseBtn.setObjectName("srcBrowseBtn")
        self.gridLayout.addWidget(self.srcBrowseBtn, 2, 3, 1, 1)
        self.destBrowseBtn = QtWidgets.QPushButton(self.groupBox)
        self.destBrowseBtn.setObjectName("destBrowseBtn")
        self.gridLayout.addWidget(self.destBrowseBtn, 3, 3, 1, 1)
        self.overwrite = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.overwrite.sizePolicy().hasHeightForWidth())
        self.overwrite.setSizePolicy(sizePolicy)
        self.overwrite.setObjectName("overwrite")
        self.gridLayout.addWidget(self.overwrite, 0, 2, 1, 1)
        self.cancelBtn = QtWidgets.QPushButton(self.groupBox)
        self.cancelBtn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy)
        self.cancelBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout.addWidget(self.cancelBtn, 5, 2, 1, 1,
                                  QtCore.Qt.AlignRight)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.isFolder = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.isFolder.sizePolicy().hasHeightForWidth())
        self.isFolder.setSizePolicy(sizePolicy)
        self.isFolder.setChecked(True)
        self.isFolder.setObjectName("isFolder")
        self.fileOptions = QtWidgets.QButtonGroup(Ecosongs)
        self.fileOptions.setObjectName("fileOptions")
        self.fileOptions.addButton(self.isFolder)
        self.horizontalLayout_2.addWidget(self.isFolder)
        self.isFile = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.isFile.sizePolicy().hasHeightForWidth())
        self.isFile.setSizePolicy(sizePolicy)
        self.isFile.setMinimumSize(QtCore.QSize(0, 0))
        self.isFile.setChecked(False)
        self.isFile.setObjectName("isFile")
        self.fileOptions.addButton(self.isFile)
        self.horizontalLayout_2.addWidget(self.isFile)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.isRecursive = QtWidgets.QCheckBox(self.groupBox)
        self.isRecursive.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.isRecursive.sizePolicy().hasHeightForWidth())
        self.isRecursive.setSizePolicy(sizePolicy)
        self.isRecursive.setChecked(True)
        self.isRecursive.setObjectName("isRecursive")
        self.gridLayout.addWidget(self.isRecursive, 1, 0, 1, 1)
        self.convertBtn = QtWidgets.QPushButton(self.groupBox)
        self.convertBtn.setObjectName("convertBtn")
        self.gridLayout.addWidget(self.convertBtn, 5, 3, 1, 1)
        self.destPathInput = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.destPathInput.sizePolicy().hasHeightForWidth())
        self.destPathInput.setSizePolicy(sizePolicy)
        self.destPathInput.setObjectName("destPathInput")
        self.gridLayout.addWidget(self.destPathInput, 3, 1, 1, 2)
        self.srcPathInput = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.srcPathInput.sizePolicy().hasHeightForWidth())
        self.srcPathInput.setSizePolicy(sizePolicy)
        self.srcPathInput.setMaximumSize(QtCore.QSize(628, 21))
        self.srcPathInput.setObjectName("srcPathInput")
        self.gridLayout.addWidget(self.srcPathInput, 2, 1, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        Ecosongs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ecosongs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 20))
        self.menubar.setObjectName("menubar")
        Ecosongs.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ecosongs)
        self.statusbar.setObjectName("statusbar")
        Ecosongs.setStatusBar(self.statusbar)

        self.retranslateUi(Ecosongs)
        QtCore.QMetaObject.connectSlotsByName(Ecosongs)
        Ecosongs.setTabOrder(self.isFolder, self.srcPathInput)
        Ecosongs.setTabOrder(self.srcPathInput, self.srcBrowseBtn)
        Ecosongs.setTabOrder(self.srcBrowseBtn, self.destPathInput)
        Ecosongs.setTabOrder(self.destPathInput, self.destBrowseBtn)
        Ecosongs.setTabOrder(self.destBrowseBtn, self.logConsole)

    def retranslateUi(self, Ecosongs):
        _translate = QtCore.QCoreApplication.translate
        Ecosongs.setWindowTitle(_translate("Ecosongs", "MainWindow"))
        self.groupBox.setTitle(_translate("Ecosongs", "Wac converter"))
        self.sourceLabel.setText(_translate("Ecosongs", "Source"))
        self.destinationLabel.setText(_translate("Ecosongs", "Destination"))
        self.srcBrowseBtn.setText(_translate("Ecosongs", "Browse"))
        self.destBrowseBtn.setText(_translate("Ecosongs", "Browse"))
        self.overwrite.setText(_translate("Ecosongs", "Overwrite old files"))
        self.cancelBtn.setText(_translate("Ecosongs", "Cancel"))
        self.isFolder.setText(_translate("Ecosongs", "Choose a folder"))
        self.isFile.setText(_translate("Ecosongs", "Choose files"))
        self.isRecursive.setText(_translate("Ecosongs", "include subfolders"))
        self.convertBtn.setText(_translate("Ecosongs", "Convert"))
