# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detection_evaluator.ui'
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


class Ui_DetectionEvaluator(object):
    def setupUi(self, DetectionEvaluator):
        if DetectionEvaluator.objectName():
            DetectionEvaluator.setObjectName(u"DetectionEvaluator")
        DetectionEvaluator.resize(754, 740)
        self.gridLayout = QGridLayout(DetectionEvaluator)
        self.gridLayout.setObjectName(u"gridLayout")
        self.input_audio_folder = QLineEdit(DetectionEvaluator)
        self.input_audio_folder.setObjectName(u"input_audio_folder")

        self.gridLayout.addWidget(self.input_audio_folder, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 11, 0, 1, 3)

        self.options_widget = QWidget(DetectionEvaluator)
        self.options_widget.setObjectName(u"options_widget")
        self.options_widget.setEnabled(False)
        self.verticalLayout = QVBoxLayout(self.options_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.options_widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cb_keep_by_default = QCheckBox(self.groupBox_2)
        self.cb_keep_by_default.setObjectName(u"cb_keep_by_default")

        self.gridLayout_4.addWidget(self.cb_keep_by_default, 3, 0, 1, 2)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_10, 0, 2, 1, 1)

        self.list_exclude_tag = QListWidget(self.groupBox_2)
        self.list_exclude_tag.setObjectName(u"list_exclude_tag")
        self.list_exclude_tag.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_4.addWidget(self.list_exclude_tag, 2, 2, 1, 1)

        self.list_include_tag = QListWidget(self.groupBox_2)
        self.list_include_tag.setObjectName(u"list_include_tag")
        self.list_include_tag.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_4.addWidget(self.list_include_tag, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.options_widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.slider_min_duration = QSlider(self.groupBox)
        self.slider_min_duration.setObjectName(u"slider_min_duration")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slider_min_duration.sizePolicy().hasHeightForWidth())
        self.slider_min_duration.setSizePolicy(sizePolicy1)
        self.slider_min_duration.setMaximum(100)
        self.slider_min_duration.setValue(1)
        self.slider_min_duration.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.slider_min_duration, 2, 1, 1, 1)

        self.slider_end_threshold = QSlider(self.groupBox)
        self.slider_end_threshold.setObjectName(u"slider_end_threshold")
        sizePolicy1.setHeightForWidth(self.slider_end_threshold.sizePolicy().hasHeightForWidth())
        self.slider_end_threshold.setSizePolicy(sizePolicy1)
        self.slider_end_threshold.setValue(60)
        self.slider_end_threshold.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.slider_end_threshold, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.lbl_end_threshold = QLabel(self.groupBox)
        self.lbl_end_threshold.setObjectName(u"lbl_end_threshold")

        self.gridLayout_3.addWidget(self.lbl_end_threshold, 1, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.lbl_min_activity = QLabel(self.groupBox)
        self.lbl_min_activity.setObjectName(u"lbl_min_activity")

        self.gridLayout_3.addWidget(self.lbl_min_activity, 0, 2, 1, 1)

        self.slider_min_activity = QSlider(self.groupBox)
        self.slider_min_activity.setObjectName(u"slider_min_activity")
        sizePolicy1.setHeightForWidth(self.slider_min_activity.sizePolicy().hasHeightForWidth())
        self.slider_min_activity.setSizePolicy(sizePolicy1)
        self.slider_min_activity.setValue(95)
        self.slider_min_activity.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.slider_min_activity, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.lbl_min_duration = QLabel(self.groupBox)
        self.lbl_min_duration.setObjectName(u"lbl_min_duration")

        self.gridLayout_3.addWidget(self.lbl_min_duration, 2, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.gridLayout.addWidget(self.options_widget, 5, 0, 1, 3)

        self.btn_label_folder = QPushButton(DetectionEvaluator)
        self.btn_label_folder.setObjectName(u"btn_label_folder")

        self.gridLayout.addWidget(self.btn_label_folder, 3, 2, 1, 1)

        self.cb_only_done = QCheckBox(DetectionEvaluator)
        self.cb_only_done.setObjectName(u"cb_only_done")
        self.cb_only_done.setChecked(True)

        self.gridLayout.addWidget(self.cb_only_done, 4, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_message = QLabel(DetectionEvaluator)
        self.lbl_message.setObjectName(u"lbl_message")

        self.horizontalLayout_5.addWidget(self.lbl_message)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cb_check_label = QCheckBox(DetectionEvaluator)
        self.cb_check_label.setObjectName(u"cb_check_label")
        self.cb_check_label.setChecked(True)

        self.horizontalLayout.addWidget(self.cb_check_label)

        self.cb_autosave = QCheckBox(DetectionEvaluator)
        self.cb_autosave.setObjectName(u"cb_autosave")

        self.horizontalLayout.addWidget(self.cb_autosave)

        self.cb_recalculate = QCheckBox(DetectionEvaluator)
        self.cb_recalculate.setObjectName(u"cb_recalculate")

        self.horizontalLayout.addWidget(self.cb_recalculate)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)

        self.btn_audio_folder = QPushButton(DetectionEvaluator)
        self.btn_audio_folder.setObjectName(u"btn_audio_folder")

        self.gridLayout.addWidget(self.btn_audio_folder, 2, 2, 1, 1)

        self.results_widget = QWidget(DetectionEvaluator)
        self.results_widget.setObjectName(u"results_widget")
        self.results_widget.setEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(self.results_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.results_widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_recall = QLabel(self.groupBox_3)
        self.lbl_recall.setObjectName(u"lbl_recall")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_recall.setFont(font)

        self.gridLayout_2.addWidget(self.lbl_recall, 2, 3, 1, 1)

        self.lbl_precision = QLabel(self.groupBox_3)
        self.lbl_precision.setObjectName(u"lbl_precision")
        self.lbl_precision.setFont(font)

        self.gridLayout_2.addWidget(self.lbl_precision, 2, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_2.addWidget(self.label_15, 2, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)

        self.lbl_n_events = QLabel(self.groupBox_3)
        self.lbl_n_events.setObjectName(u"lbl_n_events")

        self.gridLayout_2.addWidget(self.lbl_n_events, 0, 1, 1, 1)

        self.lbl_n_annots = QLabel(self.groupBox_3)
        self.lbl_n_annots.setObjectName(u"lbl_n_annots")

        self.gridLayout_2.addWidget(self.lbl_n_annots, 0, 3, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 0, 2, 1, 1)

        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 1, 2, 1, 1)

        self.lbl_events_matched = QLabel(self.groupBox_3)
        self.lbl_events_matched.setObjectName(u"lbl_events_matched")

        self.gridLayout_2.addWidget(self.lbl_events_matched, 1, 1, 1, 1)

        self.lbl_annots_matched = QLabel(self.groupBox_3)
        self.lbl_annots_matched.setObjectName(u"lbl_annots_matched")

        self.gridLayout_2.addWidget(self.lbl_annots_matched, 1, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.gridLayout.addWidget(self.results_widget, 8, 0, 1, 3)

        self.label_12 = QLabel(DetectionEvaluator)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.btn_load_data = QPushButton(DetectionEvaluator)
        self.btn_load_data.setObjectName(u"btn_load_data")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_load_data.setFont(font1)

        self.horizontalLayout_3.addWidget(self.btn_load_data)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)

        self.label = QLabel(DetectionEvaluator)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.input_label_folder = QLineEdit(DetectionEvaluator)
        self.input_label_folder.setObjectName(u"input_label_folder")
        self.input_label_folder.setFrame(True)

        self.gridLayout.addWidget(self.input_label_folder, 3, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.btn_calculate = QPushButton(DetectionEvaluator)
        self.btn_calculate.setObjectName(u"btn_calculate")
        self.btn_calculate.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn_calculate)


        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.btn_sensitivity = QPushButton(DetectionEvaluator)
        self.btn_sensitivity.setObjectName(u"btn_sensitivity")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_sensitivity.setFont(font2)

        self.horizontalLayout_4.addWidget(self.btn_sensitivity)


        self.gridLayout.addLayout(self.horizontalLayout_4, 9, 2, 1, 1)


        self.retranslateUi(DetectionEvaluator)

        QMetaObject.connectSlotsByName(DetectionEvaluator)
    # setupUi

    def retranslateUi(self, DetectionEvaluator):
        DetectionEvaluator.setWindowTitle(QCoreApplication.translate("DetectionEvaluator", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DetectionEvaluator", u"Tag filtering", None))
        self.cb_keep_by_default.setText(QCoreApplication.translate("DetectionEvaluator", u"Keep tags by default", None))
        self.label_8.setText(QCoreApplication.translate("DetectionEvaluator", u"Include labels", None))
        self.label_10.setText(QCoreApplication.translate("DetectionEvaluator", u"Exclude labels", None))
        self.pushButton.setText(QCoreApplication.translate("DetectionEvaluator", u"PushButton", None))
        self.groupBox.setTitle(QCoreApplication.translate("DetectionEvaluator", u"Event filter options", None))
        self.label_4.setText(QCoreApplication.translate("DetectionEvaluator", u"End threshold", None))
        self.lbl_end_threshold.setText("")
        self.label_6.setText(QCoreApplication.translate("DetectionEvaluator", u"Minimum duration", None))
        self.lbl_min_activity.setText("")
        self.label_2.setText(QCoreApplication.translate("DetectionEvaluator", u"Min activity", None))
        self.lbl_min_duration.setText("")
        self.btn_label_folder.setText(QCoreApplication.translate("DetectionEvaluator", u"Choose folder", None))
        self.cb_only_done.setText(QCoreApplication.translate("DetectionEvaluator", u"Only use completely done files", None))
        self.lbl_message.setText("")
#if QT_CONFIG(tooltip)
        self.cb_check_label.setToolTip(QCoreApplication.translate("DetectionEvaluator", u"Automatically check if a 'labels' folder exists below the selected audio folder", None))
#endif // QT_CONFIG(tooltip)
        self.cb_check_label.setText(QCoreApplication.translate("DetectionEvaluator", u"Check for label folder", None))
        self.cb_autosave.setText(QCoreApplication.translate("DetectionEvaluator", u"Autosave simulations", None))
#if QT_CONFIG(tooltip)
        self.cb_recalculate.setToolTip(QCoreApplication.translate("DetectionEvaluator", u"Will not load previously saved results and perform the analysis again", None))
#endif // QT_CONFIG(tooltip)
        self.cb_recalculate.setText(QCoreApplication.translate("DetectionEvaluator", u"Recalculate", None))
        self.btn_audio_folder.setText(QCoreApplication.translate("DetectionEvaluator", u"Choose folder", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("DetectionEvaluator", u"Results", None))
        self.lbl_recall.setText("")
        self.lbl_precision.setText("")
        self.label_15.setText(QCoreApplication.translate("DetectionEvaluator", u"Recall:", None))
        self.label_13.setText(QCoreApplication.translate("DetectionEvaluator", u"Precision:", None))
        self.lbl_n_events.setText("")
        self.lbl_n_annots.setText("")
        self.label_17.setText(QCoreApplication.translate("DetectionEvaluator", u"N Events detected:", None))
        self.label_18.setText(QCoreApplication.translate("DetectionEvaluator", u"N annotations:", None))
        self.label_21.setText(QCoreApplication.translate("DetectionEvaluator", u"N events matched:", None))
        self.label_22.setText(QCoreApplication.translate("DetectionEvaluator", u"N annotations matched:", None))
        self.lbl_events_matched.setText("")
        self.lbl_annots_matched.setText("")
        self.label_12.setText(QCoreApplication.translate("DetectionEvaluator", u"Reference audio files folder", None))
        self.btn_load_data.setText(QCoreApplication.translate("DetectionEvaluator", u"Load data", None))
        self.label.setText(QCoreApplication.translate("DetectionEvaluator", u"Reference labels folder:", None))
        self.btn_calculate.setText(QCoreApplication.translate("DetectionEvaluator", u"Calculate statistics", None))
        self.btn_sensitivity.setText(QCoreApplication.translate("DetectionEvaluator", u"Launch sensistivity analysis", None))
    # retranslateUi
