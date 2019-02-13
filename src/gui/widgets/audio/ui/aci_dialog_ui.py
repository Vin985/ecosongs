# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aci_dialog.ui',
# licensing of 'aci_dialog.ui' applies.
#
# Created: Wed Feb 13 15:59:31 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AciDialog(object):
    def setupUi(self, AciDialog):
        AciDialog.setObjectName("AciDialog")
        AciDialog.resize(577, 489)
        AciDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(AciDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.override_spectro = QtWidgets.QGroupBox(AciDialog)
        self.override_spectro.setCheckable(True)
        self.override_spectro.setObjectName("override_spectro")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.override_spectro)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spectro_settings = AciSpectroSettings(self.override_spectro)
        self.spectro_settings.setObjectName("spectro_settings")
        self.horizontalLayout.addWidget(self.spectro_settings)
        self.gridLayout.addWidget(self.override_spectro, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(AciDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.progress_bar = QtWidgets.QProgressBar(AciDialog)
        self.progress_bar.setEnabled(False)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout.addWidget(self.progress_bar, 5, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_cancel = QtWidgets.QPushButton(AciDialog)
        self.btn_cancel.setObjectName("btn_cancel")
        self.buttonGroup = QtWidgets.QButtonGroup(AciDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btn_cancel)
        self.horizontalLayout_3.addWidget(self.btn_cancel)
        self.btn_start = QtWidgets.QPushButton(AciDialog)
        self.btn_start.setObjectName("btn_start")
        self.buttonGroup.addButton(self.btn_start)
        self.horizontalLayout_3.addWidget(self.btn_start)
        self.btn_close = QtWidgets.QPushButton(AciDialog)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 1, 1, 1)
        self.lbl_progress = QtWidgets.QLabel(AciDialog)
        self.lbl_progress.setText("")
        self.lbl_progress.setObjectName("lbl_progress")
        self.gridLayout.addWidget(self.lbl_progress, 4, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 2)

        self.retranslateUi(AciDialog)
        QtCore.QMetaObject.connectSlotsByName(AciDialog)

    def retranslateUi(self, AciDialog):
        AciDialog.setWindowTitle(QtWidgets.QApplication.translate("AciDialog", "Dialog", None, -1))
        self.override_spectro.setTitle(QtWidgets.QApplication.translate("AciDialog", "Override spectrogram settings", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("AciDialog", "TextLabel", None, -1))
        self.btn_cancel.setText(QtWidgets.QApplication.translate("AciDialog", "Cancel", None, -1))
        self.btn_start.setText(QtWidgets.QApplication.translate("AciDialog", "Start", None, -1))
        self.btn_close.setText(QtWidgets.QApplication.translate("AciDialog", "Close", None, -1))

from gui.widgets.menus.acispectrosettings import AciSpectroSettings
