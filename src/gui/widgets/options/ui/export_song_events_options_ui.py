# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_song_events_options.ui'
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

from gui.widgets.options.song_events_options import SongEventsOptions
from gui.widgets.common.file_chooser import FileChooser


class Ui_ExportSongEventsOptions(object):
    def setupUi(self, ExportSongEventsOptions):
        if not ExportSongEventsOptions.objectName():
            ExportSongEventsOptions.setObjectName(u"ExportSongEventsOptions")
        ExportSongEventsOptions.resize(578, 299)
        self.verticalLayout = QVBoxLayout(ExportSongEventsOptions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(ExportSongEventsOptions)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.song_events_options = SongEventsOptions(self.groupBox)
        self.song_events_options.setObjectName(u"song_events_options")

        self.verticalLayout_4.addWidget(self.song_events_options)

        self.frame_calculate_predictions = QFrame(self.groupBox)
        self.frame_calculate_predictions.setObjectName(u"frame_calculate_predictions")
        self.frame_calculate_predictions.setFrameShape(QFrame.NoFrame)
        self.frame_calculate_predictions.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_calculate_predictions)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 15, 0, 0)
        self.lbl_no_preds = QLabel(self.frame_calculate_predictions)
        self.lbl_no_preds.setObjectName(u"lbl_no_preds")

        self.verticalLayout_2.addWidget(self.lbl_no_preds)

        self.checkbox_calculate_predictions = QCheckBox(self.frame_calculate_predictions)
        self.checkbox_calculate_predictions.setObjectName(u"checkbox_calculate_predictions")

        self.verticalLayout_2.addWidget(self.checkbox_calculate_predictions)

        self.checkbox_save = QCheckBox(self.frame_calculate_predictions)
        self.checkbox_save.setObjectName(u"checkbox_save")
        self.checkbox_save.setEnabled(False)
        self.checkbox_save.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkbox_save)


        self.verticalLayout_4.addWidget(self.frame_calculate_predictions)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(ExportSongEventsOptions)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_csv = QRadioButton(self.groupBox_2)
        self.radiogroup_format = QButtonGroup(ExportSongEventsOptions)
        self.radiogroup_format.setObjectName(u"radiogroup_format")
        self.radiogroup_format.addButton(self.radio_csv)
        self.radio_csv.setObjectName(u"radio_csv")
        self.radio_csv.setChecked(True)

        self.horizontalLayout.addWidget(self.radio_csv)

        self.radio_db = QRadioButton(self.groupBox_2)
        self.radiogroup_format.addButton(self.radio_db)
        self.radio_db.setObjectName(u"radio_db")

        self.horizontalLayout.addWidget(self.radio_db)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.file_chooser = FileChooser(self.groupBox_2)
        self.file_chooser.setObjectName(u"file_chooser")

        self.verticalLayout_3.addWidget(self.file_chooser)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ExportSongEventsOptions)

        QMetaObject.connectSlotsByName(ExportSongEventsOptions)
    # setupUi

    def retranslateUi(self, ExportSongEventsOptions):
        ExportSongEventsOptions.setWindowTitle(QCoreApplication.translate("ExportSongEventsOptions", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("ExportSongEventsOptions", u"Event detection options", None))
        self.lbl_no_preds.setText("")
        self.checkbox_calculate_predictions.setText(QCoreApplication.translate("ExportSongEventsOptions", u"Calculate these predictions (this could be long)", None))
        self.checkbox_save.setText(QCoreApplication.translate("ExportSongEventsOptions", u"Save predictions", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ExportSongEventsOptions", u"Select destination file", None))
        self.label_2.setText(QCoreApplication.translate("ExportSongEventsOptions", u"Export format:", None))
        self.radio_csv.setText(QCoreApplication.translate("ExportSongEventsOptions", u"csv", None))
        self.radio_db.setText(QCoreApplication.translate("ExportSongEventsOptions", u"database format", None))
    # retranslateUi

