# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detector_options.ui',
# licensing of 'detector_options.ui' applies.
#
# Created: Wed Mar 13 14:32:30 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.slider_activity = QtWidgets.QSlider(Form)
        self.slider_activity.setMaximum(100)
        self.slider_activity.setProperty("value", 95)
        self.slider_activity.setOrientation(QtCore.Qt.Horizontal)
        self.slider_activity.setObjectName("slider_activity")
        self.gridLayout.addWidget(self.slider_activity, 1, 1, 1, 1)
        self.lbl_activity = QtWidgets.QLabel(Form)
        self.lbl_activity.setText("")
        self.lbl_activity.setObjectName("lbl_activity")
        self.gridLayout.addWidget(self.lbl_activity, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.slider_end_threshold = QtWidgets.QSlider(Form)
        self.slider_end_threshold.setProperty("value", 60)
        self.slider_end_threshold.setOrientation(QtCore.Qt.Horizontal)
        self.slider_end_threshold.setObjectName("slider_end_threshold")
        self.gridLayout.addWidget(self.slider_end_threshold, 2, 1, 1, 1)
        self.lbl_end_threshold = QtWidgets.QLabel(Form)
        self.lbl_end_threshold.setText("")
        self.lbl_end_threshold.setObjectName("lbl_end_threshold")
        self.gridLayout.addWidget(self.lbl_end_threshold, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.spin_min_duration = QtWidgets.QDoubleSpinBox(Form)
        self.spin_min_duration.setSingleStep(0.01)
        self.spin_min_duration.setProperty("value", 0.1)
        self.spin_min_duration.setObjectName("spin_min_duration")
        self.gridLayout.addWidget(self.spin_min_duration, 3, 1, 1, 1)
        self.checkbox_remove_noise = QtWidgets.QCheckBox(Form)
        self.checkbox_remove_noise.setObjectName("checkbox_remove_noise")
        self.gridLayout.addWidget(self.checkbox_remove_noise, 4, 0, 1, 2)
        self.checkbox_resample = QtWidgets.QCheckBox(Form)
        self.checkbox_resample.setObjectName("checkbox_resample")
        self.gridLayout.addWidget(self.checkbox_resample, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 84, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.checkbox_save = QtWidgets.QCheckBox(Form)
        self.checkbox_save.setChecked(True)
        self.checkbox_save.setObjectName("checkbox_save")
        self.gridLayout.addWidget(self.checkbox_save, 7, 0, 1, 1)
        self.checkbox_overwrite = QtWidgets.QCheckBox(Form)
        self.checkbox_overwrite.setChecked(True)
        self.checkbox_overwrite.setObjectName("checkbox_overwrite")
        self.gridLayout.addWidget(self.checkbox_overwrite, 7, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Detect songs in selected recordings", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Activity level", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "End threshold", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Minimum duration (s)", None, -1))
        self.checkbox_remove_noise.setText(QtWidgets.QApplication.translate("Form", "Remove noise", None, -1))
        self.checkbox_resample.setText(QtWidgets.QApplication.translate("Form", "Resample", None, -1))
        self.checkbox_save.setText(QtWidgets.QApplication.translate("Form", "Save results", None, -1))
        self.checkbox_overwrite.setText(QtWidgets.QApplication.translate("Form", "Replace previous results", None, -1))

