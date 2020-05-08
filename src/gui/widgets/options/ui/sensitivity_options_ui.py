# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sensitivity_options.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from gui.widgets.common.labeled_slider import LabeledSlider


class Ui_SensitivityOptions(object):
    def setupUi(self, SensitivityOptions):
        if SensitivityOptions.objectName():
            SensitivityOptions.setObjectName(u"SensitivityOptions")
        SensitivityOptions.resize(618, 402)
        self.gridLayout = QGridLayout(SensitivityOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.slider_min_duration_start = LabeledSlider(SensitivityOptions)
        self.slider_min_duration_start.setObjectName(u"slider_min_duration_start")
        self.slider_min_duration_start.setMinimum(10)
        self.slider_min_duration_start.setMaximum(1000)
        self.slider_min_duration_start.setSingleStep(10)
        self.slider_min_duration_start.setPageStep(100)
        self.slider_min_duration_start.setSliderPosition(10)
        self.slider_min_duration_start.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_min_duration_start, 6, 1, 1, 1)

        self.slider_min_duration_end = LabeledSlider(SensitivityOptions)
        self.slider_min_duration_end.setObjectName(u"slider_min_duration_end")
        self.slider_min_duration_end.setMinimum(10)
        self.slider_min_duration_end.setMaximum(1000)
        self.slider_min_duration_end.setSingleStep(10)
        self.slider_min_duration_end.setPageStep(100)
        self.slider_min_duration_end.setValue(500)
        self.slider_min_duration_end.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_min_duration_end, 6, 3, 1, 1)

        self.checkbox_save = QCheckBox(SensitivityOptions)
        self.checkbox_save.setObjectName(u"checkbox_save")
        self.checkbox_save.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_save, 9, 0, 1, 1)

        self.checkbox_overwrite = QCheckBox(SensitivityOptions)
        self.checkbox_overwrite.setObjectName(u"checkbox_overwrite")
        self.checkbox_overwrite.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_overwrite, 9, 1, 1, 1)

        self.slider_end_threshold_start = LabeledSlider(SensitivityOptions)
        self.slider_end_threshold_start.setObjectName(u"slider_end_threshold_start")
        self.slider_end_threshold_start.setValue(5)
        self.slider_end_threshold_start.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_end_threshold_start, 5, 1, 1, 1)

        self.label = QLabel(SensitivityOptions)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.label_3 = QLabel(SensitivityOptions)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.slider_activity_end = LabeledSlider(SensitivityOptions)
        self.slider_activity_end.setObjectName(u"slider_activity_end")
        self.slider_activity_end.setValue(95)
        self.slider_activity_end.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_activity_end, 4, 3, 1, 1)

        self.label_2 = QLabel(SensitivityOptions)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_4 = QLabel(SensitivityOptions)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_9 = QLabel(SensitivityOptions)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 6, 2, 1, 1)

        self.label_5 = QLabel(SensitivityOptions)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        self.slider_end_threshold_end = LabeledSlider(SensitivityOptions)
        self.slider_end_threshold_end.setObjectName(u"slider_end_threshold_end")
        self.slider_end_threshold_end.setValue(60)
        self.slider_end_threshold_end.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_end_threshold_end, 5, 3, 1, 1)

        self.label_7 = QLabel(SensitivityOptions)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(597, 238, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 5)

        self.slider_activity_start = LabeledSlider(SensitivityOptions)
        self.slider_activity_start.setObjectName(u"slider_activity_start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slider_activity_start.sizePolicy().hasHeightForWidth())
        self.slider_activity_start.setSizePolicy(sizePolicy1)
        self.slider_activity_start.setValue(60)
        self.slider_activity_start.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_activity_start, 4, 1, 1, 1)

        self.label_6 = QLabel(SensitivityOptions)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.spin_end_threshold_step = QDoubleSpinBox(SensitivityOptions)
        self.spin_end_threshold_step.setObjectName(u"spin_end_threshold_step")
        self.spin_end_threshold_step.setDecimals(2)
        self.spin_end_threshold_step.setMaximum(0.990000000000000)
        self.spin_end_threshold_step.setSingleStep(0.010000000000000)
        self.spin_end_threshold_step.setValue(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.spin_end_threshold_step)


        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 4, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spin_duration_step = QSpinBox(SensitivityOptions)
        self.spin_duration_step.setObjectName(u"spin_duration_step")
        self.spin_duration_step.setMaximum(1000)
        self.spin_duration_step.setSingleStep(10)
        self.spin_duration_step.setValue(20)

        self.horizontalLayout_2.addWidget(self.spin_duration_step)

        self.label_8 = QLabel(SensitivityOptions)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)


        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 4, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spin_activity_step = QDoubleSpinBox(SensitivityOptions)
        self.spin_activity_step.setObjectName(u"spin_activity_step")
        self.spin_activity_step.setDecimals(2)
        self.spin_activity_step.setMaximum(0.990000000000000)
        self.spin_activity_step.setSingleStep(0.010000000000000)
        self.spin_activity_step.setValue(0.100000000000000)

        self.horizontalLayout.addWidget(self.spin_activity_step)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 4, 1, 1)

        self.label_10 = QLabel(SensitivityOptions)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.checkbox_method_standard = QCheckBox(SensitivityOptions)
        self.method_group = QButtonGroup(SensitivityOptions)
        self.method_group.setObjectName(u"method_group")
        self.method_group.setExclusive(False)
        self.method_group.addButton(self.checkbox_method_standard)
        self.checkbox_method_standard.setObjectName(u"checkbox_method_standard")
        self.checkbox_method_standard.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_method_standard, 1, 1, 1, 1)

        self.checkbox_method_subsampling = QCheckBox(SensitivityOptions)
        self.method_group.addButton(self.checkbox_method_subsampling)
        self.checkbox_method_subsampling.setObjectName(u"checkbox_method_subsampling")
        self.checkbox_method_subsampling.setChecked(False)

        self.gridLayout.addWidget(self.checkbox_method_subsampling, 1, 3, 1, 1)


        self.retranslateUi(SensitivityOptions)

        QMetaObject.connectSlotsByName(SensitivityOptions)
    # setupUi

    def retranslateUi(self, SensitivityOptions):
        SensitivityOptions.setWindowTitle(QCoreApplication.translate("SensitivityOptions", u"Form", None))
        self.checkbox_save.setText(QCoreApplication.translate("SensitivityOptions", u"Save results", None))
        self.checkbox_overwrite.setText(QCoreApplication.translate("SensitivityOptions", u"Replace previous results", None))
        self.label.setText(QCoreApplication.translate("SensitivityOptions", u"Launch sensitivity analysis to detect optimal option values", None))
        self.label_3.setText(QCoreApplication.translate("SensitivityOptions", u"Minimum duration (s)", None))
        self.label_2.setText(QCoreApplication.translate("SensitivityOptions", u"Activity level", None))
        self.label_4.setText(QCoreApplication.translate("SensitivityOptions", u"End threshold", None))
        self.label_9.setText("")
        self.label_5.setText(QCoreApplication.translate("SensitivityOptions", u"Start", None))
        self.label_7.setText(QCoreApplication.translate("SensitivityOptions", u"End", None))
        self.label_6.setText(QCoreApplication.translate("SensitivityOptions", u"Step", None))
        self.label_8.setText(QCoreApplication.translate("SensitivityOptions", u"ms", None))
        self.label_10.setText(QCoreApplication.translate("SensitivityOptions", u"Method", None))
        self.checkbox_method_standard.setText(QCoreApplication.translate("SensitivityOptions", u"Standard", None))
        self.checkbox_method_subsampling.setText(QCoreApplication.translate("SensitivityOptions", u"Subsampling", None))
    # retranslateUi

