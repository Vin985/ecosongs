# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressdialog.ui',
# licensing of 'progressdialog.ui' applies.
#
# Created: Wed Mar 13 16:12:59 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ProgressDialog(object):
    def setupUi(self, ProgressDialog):
        ProgressDialog.setObjectName("ProgressDialog")
        ProgressDialog.resize(533, 391)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressDialog.sizePolicy().hasHeightForWidth())
        ProgressDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProgressDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content_layout = QtWidgets.QHBoxLayout()
        self.content_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.content_layout.setObjectName("content_layout")
        self.verticalLayout.addLayout(self.content_layout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_cancel = QtWidgets.QPushButton(ProgressDialog)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.btn_start = QtWidgets.QPushButton(ProgressDialog)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        self.btn_close = QtWidgets.QPushButton(ProgressDialog)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.progress_bar = QtWidgets.QProgressBar(ProgressDialog)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout_2.addWidget(self.progress_bar, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.lbl_progress = QtWidgets.QLabel(ProgressDialog)
        self.lbl_progress.setText("")
        self.lbl_progress.setObjectName("lbl_progress")
        self.gridLayout_2.addWidget(self.lbl_progress, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(ProgressDialog)
        QtCore.QMetaObject.connectSlotsByName(ProgressDialog)

    def retranslateUi(self, ProgressDialog):
        ProgressDialog.setWindowTitle(QtWidgets.QApplication.translate("ProgressDialog", "Dialog", None, -1))
        self.btn_cancel.setText(QtWidgets.QApplication.translate("ProgressDialog", "Cancel", None, -1))
        self.btn_start.setText(QtWidgets.QApplication.translate("ProgressDialog", "Start", None, -1))
        self.btn_close.setText(QtWidgets.QApplication.translate("ProgressDialog", "Close", None, -1))

