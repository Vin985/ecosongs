# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detection_evaluator.ui'
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
from gui.widgets.common.table.dataframe_table_view import DataFrameTableView


class Ui_DetectionEvaluator(object):
    def setupUi(self, DetectionEvaluator):
        if not DetectionEvaluator.objectName():
            DetectionEvaluator.setObjectName(u"DetectionEvaluator")
        DetectionEvaluator.resize(845, 802)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DetectionEvaluator.sizePolicy().hasHeightForWidth())
        DetectionEvaluator.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Ubuntu")
        DetectionEvaluator.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(DetectionEvaluator)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(DetectionEvaluator)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 831, 837))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(9, 7, 9, 9)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.btn_export = QPushButton(self.scrollAreaWidgetContents)
        self.btn_export.setObjectName(u"btn_export")
        font1 = QFont()
        font1.setFamily(u"Ubuntu")
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_export.setFont(font1)

        self.horizontalLayout_4.addWidget(self.btn_export)

        self.btn_sensitivity = QPushButton(self.scrollAreaWidgetContents)
        self.btn_sensitivity.setObjectName(u"btn_sensitivity")
        font2 = QFont()
        font2.setFamily(u"Ubuntu")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_sensitivity.setFont(font2)

        self.horizontalLayout_4.addWidget(self.btn_sensitivity)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 17, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.checkbox_by_class = QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_by_class.setObjectName(u"checkbox_by_class")

        self.horizontalLayout_2.addWidget(self.checkbox_by_class)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.btn_calculate = QPushButton(self.scrollAreaWidgetContents)
        self.btn_calculate.setObjectName(u"btn_calculate")
        font3 = QFont()
        font3.setFamily(u"Ubuntu")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_calculate.setFont(font3)

        self.horizontalLayout_2.addWidget(self.btn_calculate)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 7, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 10, 0, 1, 1)

        self.options_widget = QWidget(self.scrollAreaWidgetContents)
        self.options_widget.setObjectName(u"options_widget")
        self.options_widget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.options_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.options_widget, 10, 0, 1, 1)

        self.table_tags = DataFrameTableView(self.scrollAreaWidgetContents)
        self.table_tags.setObjectName(u"table_tags")
        self.table_tags.setMinimumSize(QSize(0, 200))
        self.table_tags.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.table_tags, 3, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 9, -1, -1)
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_10, 0, 2, 1, 1)

        self.list_include_tag = QListWidget(self.groupBox_2)
        self.list_include_tag.setObjectName(u"list_include_tag")
        self.list_include_tag.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_4.addWidget(self.list_include_tag, 2, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.checkbox_keep_by_default = QCheckBox(self.groupBox_2)
        self.checkbox_keep_by_default.setObjectName(u"checkbox_keep_by_default")

        self.gridLayout_4.addWidget(self.checkbox_keep_by_default, 3, 0, 1, 2)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 1, 2, 1, 1)

        self.list_exclude_tag = QListWidget(self.groupBox_2)
        self.list_exclude_tag.setObjectName(u"list_exclude_tag")
        self.list_exclude_tag.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_4.addWidget(self.list_exclude_tag, 2, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 4, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 4, 1, 1, 1)

        self.results_widget = QWidget(self.scrollAreaWidgetContents)
        self.results_widget.setObjectName(u"results_widget")
        self.results_widget.setEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(self.results_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.results_widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_events_matched = QLabel(self.groupBox_3)
        self.lbl_events_matched.setObjectName(u"lbl_events_matched")

        self.gridLayout_2.addWidget(self.lbl_events_matched, 2, 1, 1, 1)

        self.lbl_recall = QLabel(self.groupBox_3)
        self.lbl_recall.setObjectName(u"lbl_recall")
        font4 = QFont()
        font4.setFamily(u"Ubuntu")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.lbl_recall.setFont(font4)

        self.gridLayout_2.addWidget(self.lbl_recall, 3, 3, 1, 1)

        self.lbl_n_annots = QLabel(self.groupBox_3)
        self.lbl_n_annots.setObjectName(u"lbl_n_annots")

        self.gridLayout_2.addWidget(self.lbl_n_annots, 1, 3, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 2, 2, 1, 1)

        self.lbl_precision = QLabel(self.groupBox_3)
        self.lbl_precision.setObjectName(u"lbl_precision")
        self.lbl_precision.setFont(font4)

        self.gridLayout_2.addWidget(self.lbl_precision, 3, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)

        self.lbl_n_events = QLabel(self.groupBox_3)
        self.lbl_n_events.setObjectName(u"lbl_n_events")

        self.gridLayout_2.addWidget(self.lbl_n_events, 1, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)

        self.gridLayout_2.addWidget(self.label_15, 3, 2, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 2, 0, 1, 1)

        self.lbl_annots_matched = QLabel(self.groupBox_3)
        self.lbl_annots_matched.setObjectName(u"lbl_annots_matched")

        self.gridLayout_2.addWidget(self.lbl_annots_matched, 2, 3, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 1, 2, 1, 1)

        self.table_results = DataFrameTableView(self.groupBox_3)
        self.table_results.setObjectName(u"table_results")
        self.table_results.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.table_results, 0, 0, 1, 4)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.gridLayout_3.addWidget(self.results_widget, 8, 0, 1, 2)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.song_events_options = SongEventsOptions(self.groupBox)
        self.song_events_options.setObjectName(u"song_events_options")

        self.verticalLayout_3.addWidget(self.song_events_options)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.gridLayout_3.addWidget(self.groupBox, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radio_selected = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup = QButtonGroup(DetectionEvaluator)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radio_selected)
        self.radio_selected.setObjectName(u"radio_selected")
        self.radio_selected.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radio_selected)

        self.radio_all = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.radio_all)
        self.radio_all.setObjectName(u"radio_all")

        self.horizontalLayout_3.addWidget(self.radio_all)

        self.checkbox_only_done = QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_only_done.setObjectName(u"checkbox_only_done")
        self.checkbox_only_done.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkbox_only_done)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.lbl_selected_tags = QLabel(self.scrollAreaWidgetContents)
        self.lbl_selected_tags.setObjectName(u"lbl_selected_tags")

        self.horizontalLayout.addWidget(self.lbl_selected_tags)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.checkbox_show_tags = QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_show_tags.setObjectName(u"checkbox_show_tags")

        self.gridLayout_3.addWidget(self.checkbox_show_tags, 2, 0, 1, 2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.retranslateUi(DetectionEvaluator)

        QMetaObject.connectSlotsByName(DetectionEvaluator)
    # setupUi

    def retranslateUi(self, DetectionEvaluator):
        DetectionEvaluator.setWindowTitle(QCoreApplication.translate("DetectionEvaluator", u"Form", None))
        self.btn_export.setText(QCoreApplication.translate("DetectionEvaluator", u"Export results", None))
        self.btn_sensitivity.setText(QCoreApplication.translate("DetectionEvaluator", u"Launch sensistivity analysis", None))
        self.checkbox_by_class.setText(QCoreApplication.translate("DetectionEvaluator", u"Break down statistics by class", None))
        self.btn_calculate.setText(QCoreApplication.translate("DetectionEvaluator", u"Calculate statistics", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DetectionEvaluator", u"Tag filtering", None))
        self.label_10.setText(QCoreApplication.translate("DetectionEvaluator", u"Exclude labels", None))
        self.label_8.setText(QCoreApplication.translate("DetectionEvaluator", u"Include labels", None))
        self.checkbox_keep_by_default.setText(QCoreApplication.translate("DetectionEvaluator", u"Keep tags by default", None))
        self.pushButton.setText(QCoreApplication.translate("DetectionEvaluator", u"PushButton", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("DetectionEvaluator", u"Results", None))
        self.lbl_events_matched.setText("")
        self.lbl_recall.setText("")
        self.lbl_n_annots.setText("")
        self.label_22.setText(QCoreApplication.translate("DetectionEvaluator", u"N annotations matched:", None))
        self.lbl_precision.setText("")
        self.label_13.setText(QCoreApplication.translate("DetectionEvaluator", u"Precision:", None))
        self.lbl_n_events.setText("")
        self.label_15.setText(QCoreApplication.translate("DetectionEvaluator", u"Recall:", None))
        self.label_17.setText(QCoreApplication.translate("DetectionEvaluator", u"N Events detected:", None))
        self.label_21.setText(QCoreApplication.translate("DetectionEvaluator", u"N events matched:", None))
        self.lbl_annots_matched.setText("")
        self.label_18.setText(QCoreApplication.translate("DetectionEvaluator", u"N annotations:", None))
        self.groupBox.setTitle(QCoreApplication.translate("DetectionEvaluator", u"Event filter options", None))
        self.radio_selected.setText(QCoreApplication.translate("DetectionEvaluator", u"Use selected tags", None))
        self.radio_all.setText(QCoreApplication.translate("DetectionEvaluator", u"Use all tags", None))
        self.checkbox_only_done.setText(QCoreApplication.translate("DetectionEvaluator", u"Only use completely done files", None))
        self.lbl_selected_tags.setText("")
        self.checkbox_show_tags.setText(QCoreApplication.translate("DetectionEvaluator", u"Show tags", None))
    # retranslateUi

