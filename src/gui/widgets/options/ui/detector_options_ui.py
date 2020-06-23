# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detector_options.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from gui.widgets.common.labeled_slider import LabeledSlider


class Ui_DetectorOptions(object):
    def setupUi(self, DetectorOptions):
        if not DetectorOptions.objectName():
            DetectorOptions.setObjectName(u"DetectorOptions")
        DetectorOptions.resize(501, 377)
        self.gridLayout = QGridLayout(DetectorOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(DetectorOptions)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

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

        self.group_multiprocess = QGroupBox(DetectorOptions)
        self.group_multiprocess.setObjectName(u"group_multiprocess")
        self.group_multiprocess.setCheckable(True)
        self.gridLayout_2 = QGridLayout(self.group_multiprocess)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.group_multiprocess)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)

        self.slider_chunk_size = LabeledSlider(self.group_multiprocess)
        self.slider_chunk_size.setObjectName(u"slider_chunk_size")
        self.slider_chunk_size.setMinimum(1)
        self.slider_chunk_size.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.slider_chunk_size, 1, 1, 1, 1)

        self.label_7 = QLabel(self.group_multiprocess)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.slider_nprocess = LabeledSlider(self.group_multiprocess)
        self.slider_nprocess.setObjectName(u"slider_nprocess")
        self.slider_nprocess.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.slider_nprocess, 0, 1, 1, 1)

        self.checkbox_chunk_percent = QCheckBox(self.group_multiprocess)
        self.checkbox_chunk_percent.setObjectName(u"checkbox_chunk_percent")
        self.checkbox_chunk_percent.setChecked(True)

        self.gridLayout_2.addWidget(self.checkbox_chunk_percent, 2, 0, 1, 2)

        self.label_8 = QLabel(self.group_multiprocess)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 2, 1, 1)

        self.label_5 = QLabel(self.group_multiprocess)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.lbl_chunksize = QLabel(self.group_multiprocess)
        self.lbl_chunksize.setObjectName(u"lbl_chunksize")

        self.gridLayout_2.addWidget(self.lbl_chunksize, 3, 0, 1, 3)


        self.gridLayout.addWidget(self.group_multiprocess, 4, 0, 1, 3)

        self.checkbox_remove_noise = QCheckBox(DetectorOptions)
        self.checkbox_remove_noise.setObjectName(u"checkbox_remove_noise")

        self.gridLayout.addWidget(self.checkbox_remove_noise, 1, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 84, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 3)


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
        self.group_multiprocess.setTitle(QCoreApplication.translate("DetectorOptions", u"Use multiple processes", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("DetectorOptions", u"Chunk size", None))
        self.checkbox_chunk_percent.setText(QCoreApplication.translate("DetectorOptions", u"Select chunks as percent of original data", None))
        self.label_8.setText("")
        self.label_5.setText(QCoreApplication.translate("DetectorOptions", u"Number of processes", None))
        self.lbl_chunksize.setText("")
        self.checkbox_remove_noise.setText(QCoreApplication.translate("DetectorOptions", u"Remove noise", None))
    # retranslateUi

