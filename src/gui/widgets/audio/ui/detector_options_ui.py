# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detector_options.ui'
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


class Ui_DetectorOptions(object):
    def setupUi(self, DetectorOptions):
        if DetectorOptions.objectName():
            DetectorOptions.setObjectName(u"DetectorOptions")
        DetectorOptions.resize(501, 377)
        self.gridLayout = QGridLayout(DetectorOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(DetectorOptions)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 84, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 2)

        self.checkbox_overwrite = QCheckBox(DetectorOptions)
        self.checkbox_overwrite.setObjectName(u"checkbox_overwrite")
        self.checkbox_overwrite.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_overwrite, 6, 1, 1, 1)

        self.checkbox_save = QCheckBox(DetectorOptions)
        self.checkbox_save.setObjectName(u"checkbox_save")
        self.checkbox_save.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_save, 6, 0, 1, 1)

        self.checkbox_gpu = QCheckBox(DetectorOptions)
        self.checkbox_gpu.setObjectName(u"checkbox_gpu")
        self.checkbox_gpu.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_gpu, 3, 0, 1, 1)

        self.checkbox_resample = QCheckBox(DetectorOptions)
        self.checkbox_resample.setObjectName(u"checkbox_resample")

        self.gridLayout.addWidget(self.checkbox_resample, 2, 0, 1, 1)

        self.groupBox = QGroupBox(DetectorOptions)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setCheckable(True)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSlider = QSlider(self.groupBox)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.groupBox)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_2, 1, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox, 2, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 3)

        self.checkbox_remove_noise = QCheckBox(DetectorOptions)
        self.checkbox_remove_noise.setObjectName(u"checkbox_remove_noise")

        self.gridLayout.addWidget(self.checkbox_remove_noise, 1, 0, 1, 2)


        self.retranslateUi(DetectorOptions)

        QMetaObject.connectSlotsByName(DetectorOptions)
    # setupUi

    def retranslateUi(self, DetectorOptions):
        DetectorOptions.setWindowTitle(QCoreApplication.translate("DetectorOptions", u"Form", None))
        self.label.setText(QCoreApplication.translate("DetectorOptions", u"Detect activity in selected recordings", None))
        self.checkbox_overwrite.setText(QCoreApplication.translate("DetectorOptions", u"Replace previous results", None))
        self.checkbox_save.setText(QCoreApplication.translate("DetectorOptions", u"Save results", None))
        self.checkbox_gpu.setText(QCoreApplication.translate("DetectorOptions", u"Use GPU if available", None))
        self.checkbox_resample.setText(QCoreApplication.translate("DetectorOptions", u"Resample", None))
        self.groupBox.setTitle(QCoreApplication.translate("DetectorOptions", u"Use multithreading", None))
        self.label_8.setText("")
        self.label_5.setText(QCoreApplication.translate("DetectorOptions", u"Number of processes", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("DetectorOptions", u"Chunk size", None))
        self.checkBox.setText(QCoreApplication.translate("DetectorOptions", u"Select chunks as percent of original data", None))
        self.checkbox_remove_noise.setText(QCoreApplication.translate("DetectorOptions", u"Remove noise", None))
    # retranslateUi

