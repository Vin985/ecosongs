# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detector_dialog.ui',
# licensing of 'detector_dialog.ui' applies.
#
# Created: Wed Feb 13 15:26:52 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DetectorDialog(object):
    def setupUi(self, DetectorDialog):
        DetectorDialog.setObjectName("DetectorDialog")
        DetectorDialog.resize(485, 415)
        self.gridLayout = QtWidgets.QGridLayout(DetectorDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_cancel = QtWidgets.QPushButton(DetectorDialog)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.btn_start = QtWidgets.QPushButton(DetectorDialog)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        self.btn_close = QtWidgets.QPushButton(DetectorDialog)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 3)
        self.lbl_progress = QtWidgets.QLabel(DetectorDialog)
        self.lbl_progress.setText("")
        self.lbl_progress.setObjectName("lbl_progress")
        self.gridLayout.addWidget(self.lbl_progress, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(DetectorDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(DetectorDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.progress_bar = QtWidgets.QProgressBar(DetectorDialog)
        self.progress_bar.setEnabled(False)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout.addWidget(self.progress_bar, 5, 0, 1, 3)
        self.slider_activity = QtWidgets.QSlider(DetectorDialog)
        self.slider_activity.setMaximum(100)
        self.slider_activity.setProperty("value", 95)
        self.slider_activity.setOrientation(QtCore.Qt.Horizontal)
        self.slider_activity.setObjectName("slider_activity")
        self.gridLayout.addWidget(self.slider_activity, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(DetectorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lbl_activity = QtWidgets.QLabel(DetectorDialog)
        self.lbl_activity.setText("")
        self.lbl_activity.setObjectName("lbl_activity")
        self.gridLayout.addWidget(self.lbl_activity, 1, 2, 1, 1)
        self.spin_min_duration = QtWidgets.QDoubleSpinBox(DetectorDialog)
        self.spin_min_duration.setSingleStep(0.01)
        self.spin_min_duration.setProperty("value", 0.1)
        self.spin_min_duration.setObjectName("spin_min_duration")
        self.gridLayout.addWidget(self.spin_min_duration, 2, 1, 1, 1)

        self.retranslateUi(DetectorDialog)
        QtCore.QMetaObject.connectSlotsByName(DetectorDialog)

    def retranslateUi(self, DetectorDialog):
        DetectorDialog.setWindowTitle(QtWidgets.QApplication.translate("DetectorDialog", "Dialog", None, -1))
        self.btn_cancel.setText(QtWidgets.QApplication.translate("DetectorDialog", "Cancel", None, -1))
        self.btn_start.setText(QtWidgets.QApplication.translate("DetectorDialog", "Start", None, -1))
        self.btn_close.setText(QtWidgets.QApplication.translate("DetectorDialog", "Close", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("DetectorDialog", "Detect songs in selected recordings", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("DetectorDialog", "Minimum duration (s)", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("DetectorDialog", "Activity level", None, -1))
