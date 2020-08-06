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
        DetectionEvaluator.resize(1118, 802)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DetectionEvaluator.sizePolicy().hasHeightForWidth())
        DetectionEvaluator.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Ubuntu")
        DetectionEvaluator.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(DetectionEvaluator)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.splitter = QSplitter(DetectionEvaluator)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 15)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radio_selected = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup = QButtonGroup(DetectionEvaluator)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radio_selected)
        self.radio_selected.setObjectName(u"radio_selected")
        self.radio_selected.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radio_selected)

        self.radio_all = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup.addButton(self.radio_all)
        self.radio_all.setObjectName(u"radio_all")

        self.horizontalLayout_3.addWidget(self.radio_all)

        self.checkbox_only_done = QCheckBox(self.verticalLayoutWidget)
        self.checkbox_only_done.setObjectName(u"checkbox_only_done")
        self.checkbox_only_done.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkbox_only_done)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.lbl_selected_tags = QLabel(self.verticalLayoutWidget)
        self.lbl_selected_tags.setObjectName(u"lbl_selected_tags")

        self.horizontalLayout.addWidget(self.lbl_selected_tags)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.checkbox_show_tags = QCheckBox(self.verticalLayoutWidget)
        self.checkbox_show_tags.setObjectName(u"checkbox_show_tags")

        self.verticalLayout_5.addWidget(self.checkbox_show_tags)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.song_events_options = SongEventsOptions(self.groupBox)
        self.song_events_options.setObjectName(u"song_events_options")

        self.verticalLayout_3.addWidget(self.song_events_options)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setChecked(False)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 9, -1, -1)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 1, 2, 1, 1)

        self.list_exclude_tag = QListWidget(self.groupBox_2)
        self.list_exclude_tag.setObjectName(u"list_exclude_tag")
        self.list_exclude_tag.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_4.addWidget(self.list_exclude_tag, 2, 2, 1, 1)

        self.list_include_tag = QListWidget(self.groupBox_2)
        self.list_include_tag.setObjectName(u"list_include_tag")
        self.list_include_tag.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_4.addWidget(self.list_include_tag, 2, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.label_10, 0, 2, 1, 1)

        self.checkbox_keep_by_default = QCheckBox(self.groupBox_2)
        self.checkbox_keep_by_default.setObjectName(u"checkbox_keep_by_default")

        self.gridLayout_4.addWidget(self.checkbox_keep_by_default, 3, 0, 1, 2)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.btn_calculate = QPushButton(self.verticalLayoutWidget)
        self.btn_calculate.setObjectName(u"btn_calculate")
        font1 = QFont()
        font1.setFamily(u"Ubuntu")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_calculate.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn_calculate)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.results_scrollArea = QScrollArea(self.splitter)
        self.results_scrollArea.setObjectName(u"results_scrollArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.results_scrollArea.sizePolicy().hasHeightForWidth())
        self.results_scrollArea.setSizePolicy(sizePolicy4)
        self.results_scrollArea.setAutoFillBackground(True)
        self.results_scrollArea.setStyleSheet(u"#results_scrollArea { background: transparent; }\n"
"#results_scrollArea > QWidget > QWidget { background: transparent; }\n"
"#results_scrollArea > QWidget > QScrollBar { background: palette(base); }")
        self.results_scrollArea.setFrameShape(QFrame.NoFrame)
        self.results_scrollArea.setFrameShadow(QFrame.Plain)
        self.results_scrollArea.setWidgetResizable(True)
        self.results_scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 558, 796))
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 6, 9, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.table_tags = DataFrameTableView(self.scrollAreaWidgetContents)
        self.table_tags.setObjectName(u"table_tags")
        self.table_tags.setMinimumSize(QSize(0, 200))
        self.table_tags.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_6.addWidget(self.table_tags)

        self.group_results = QGroupBox(self.scrollAreaWidgetContents)
        self.group_results.setObjectName(u"group_results")
        self.group_results.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.group_results)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_true_positives_ratio = QLabel(self.group_results)
        self.lbl_true_positives_ratio.setObjectName(u"lbl_true_positives_ratio")
        font2 = QFont()
        font2.setFamily(u"Ubuntu")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.lbl_true_positives_ratio.setFont(font2)

        self.gridLayout_2.addWidget(self.lbl_true_positives_ratio, 5, 1, 1, 1)

        self.label = QLabel(self.group_results)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.lbl_n_true_positives = QLabel(self.group_results)
        self.lbl_n_true_positives.setObjectName(u"lbl_n_true_positives")

        self.gridLayout_2.addWidget(self.lbl_n_true_positives, 2, 1, 1, 1)

        self.label_22 = QLabel(self.group_results)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 2, 2, 1, 1)

        self.label_21 = QLabel(self.group_results)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 2, 0, 1, 1)

        self.label_13 = QLabel(self.group_results)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.gridLayout_2.addWidget(self.label_13, 5, 0, 1, 1)

        self.label_18 = QLabel(self.group_results)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 1, 2, 1, 1)

        self.lbl_n_tags = QLabel(self.group_results)
        self.lbl_n_tags.setObjectName(u"lbl_n_tags")

        self.gridLayout_2.addWidget(self.lbl_n_tags, 1, 3, 1, 1)

        self.label_17 = QLabel(self.group_results)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)

        self.table_results = DataFrameTableView(self.group_results)
        self.table_results.setObjectName(u"table_results")
        self.table_results.setEnabled(True)
        self.table_results.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.table_results, 0, 0, 1, 4)

        self.lbl_n_events = QLabel(self.group_results)
        self.lbl_n_events.setObjectName(u"lbl_n_events")

        self.gridLayout_2.addWidget(self.lbl_n_events, 1, 1, 1, 1)

        self.lbl_n_tags_matched = QLabel(self.group_results)
        self.lbl_n_tags_matched.setObjectName(u"lbl_n_tags_matched")

        self.gridLayout_2.addWidget(self.lbl_n_tags_matched, 2, 3, 1, 1)

        self.label_2 = QLabel(self.group_results)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_2.setFont(font3)

        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_15 = QLabel(self.group_results)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.gridLayout_2.addWidget(self.label_15, 4, 2, 1, 1)

        self.lbl_recall = QLabel(self.group_results)
        self.lbl_recall.setObjectName(u"lbl_recall")
        self.lbl_recall.setFont(font2)

        self.gridLayout_2.addWidget(self.lbl_recall, 4, 3, 1, 1)

        self.label_3 = QLabel(self.group_results)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.gridLayout_2.addWidget(self.label_3, 5, 2, 1, 1)

        self.lbl_false_positive_rate = QLabel(self.group_results)
        self.lbl_false_positive_rate.setObjectName(u"lbl_false_positive_rate")
        self.lbl_false_positive_rate.setFont(font3)

        self.gridLayout_2.addWidget(self.lbl_false_positive_rate, 5, 3, 1, 1)

        self.lbl_precision = QLabel(self.group_results)
        self.lbl_precision.setObjectName(u"lbl_precision")
        self.lbl_precision.setFont(font3)

        self.gridLayout_2.addWidget(self.lbl_precision, 4, 1, 1, 1)

        self.label_6 = QLabel(self.group_results)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 2, 1, 1)

        self.lbl_n_tags_unmatched = QLabel(self.group_results)
        self.lbl_n_tags_unmatched.setObjectName(u"lbl_n_tags_unmatched")

        self.gridLayout_2.addWidget(self.lbl_n_tags_unmatched, 3, 3, 1, 1)

        self.lbl_n_false_positives = QLabel(self.group_results)
        self.lbl_n_false_positives.setObjectName(u"lbl_n_false_positives")

        self.gridLayout_2.addWidget(self.lbl_n_false_positives, 3, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.group_results)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.btn_export = QPushButton(self.scrollAreaWidgetContents)
        self.btn_export.setObjectName(u"btn_export")
        font4 = QFont()
        font4.setFamily(u"Ubuntu")
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_export.setFont(font4)

        self.horizontalLayout_4.addWidget(self.btn_export)

        self.btn_sensitivity = QPushButton(self.scrollAreaWidgetContents)
        self.btn_sensitivity.setObjectName(u"btn_sensitivity")
        font5 = QFont()
        font5.setFamily(u"Ubuntu")
        font5.setPointSize(9)
        font5.setBold(True)
        font5.setWeight(75)
        self.btn_sensitivity.setFont(font5)

        self.horizontalLayout_4.addWidget(self.btn_sensitivity)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.results_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.results_scrollArea)

        self.horizontalLayout_5.addWidget(self.splitter)


        self.retranslateUi(DetectionEvaluator)

        QMetaObject.connectSlotsByName(DetectionEvaluator)
    # setupUi

    def retranslateUi(self, DetectionEvaluator):
        DetectionEvaluator.setWindowTitle(QCoreApplication.translate("DetectionEvaluator", u"Form", None))
        self.radio_selected.setText(QCoreApplication.translate("DetectionEvaluator", u"Use selected tags", None))
        self.radio_all.setText(QCoreApplication.translate("DetectionEvaluator", u"Use all tags", None))
        self.checkbox_only_done.setText(QCoreApplication.translate("DetectionEvaluator", u"Only use completely done files", None))
        self.lbl_selected_tags.setText("")
        self.checkbox_show_tags.setText(QCoreApplication.translate("DetectionEvaluator", u"Show tags", None))
        self.groupBox.setTitle(QCoreApplication.translate("DetectionEvaluator", u"Event filter options", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DetectionEvaluator", u"Filter tags", None))
        self.label_8.setText(QCoreApplication.translate("DetectionEvaluator", u"Include tags", None))
        self.pushButton.setText(QCoreApplication.translate("DetectionEvaluator", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("DetectionEvaluator", u"Exclude tags", None))
        self.checkbox_keep_by_default.setText(QCoreApplication.translate("DetectionEvaluator", u"Keep tags by default", None))
        self.btn_calculate.setText(QCoreApplication.translate("DetectionEvaluator", u"Calculate statistics", None))
        self.group_results.setTitle(QCoreApplication.translate("DetectionEvaluator", u"Results", None))
        self.lbl_true_positives_ratio.setText("")
        self.label.setText(QCoreApplication.translate("DetectionEvaluator", u"False positives:", None))
        self.lbl_n_true_positives.setText("")
        self.label_22.setText(QCoreApplication.translate("DetectionEvaluator", u"Matched tags:", None))
        self.label_21.setText(QCoreApplication.translate("DetectionEvaluator", u"True positives:", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("DetectionEvaluator", u"True positive ratio = True positives / Tags ", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("DetectionEvaluator", u"True positive ratio:", None))
        self.label_18.setText(QCoreApplication.translate("DetectionEvaluator", u"Tags:", None))
        self.lbl_n_tags.setText("")
        self.label_17.setText(QCoreApplication.translate("DetectionEvaluator", u"Detected events:", None))
        self.lbl_n_events.setText("")
        self.lbl_n_tags_matched.setText("")
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("DetectionEvaluator", u"Precision = True positives / Detected Events", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DetectionEvaluator", u"Precision:", None))
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("DetectionEvaluator", u"Recall = Matched tags / Tags", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("DetectionEvaluator", u"Recall:", None))
        self.lbl_recall.setText("")
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("DetectionEvaluator", u"False positive rate: False positives/ Tags duration", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("DetectionEvaluator", u"False positive rate", None))
        self.lbl_false_positive_rate.setText("")
        self.lbl_precision.setText("")
        self.label_6.setText(QCoreApplication.translate("DetectionEvaluator", u"Unmatched tags:", None))
        self.lbl_n_tags_unmatched.setText("")
        self.lbl_n_false_positives.setText("")
        self.btn_export.setText(QCoreApplication.translate("DetectionEvaluator", u"Export results", None))
        self.btn_sensitivity.setText(QCoreApplication.translate("DetectionEvaluator", u"Launch sensistivity analysis", None))
    # retranslateUi

