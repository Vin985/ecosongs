# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_table_options.ui'
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

from gui.widgets.common.file_chooser import FileChooser
from gui.widgets.common.checkable_list import CheckableList


class Ui_ExportTableOptions(object):
    def setupUi(self, ExportTableOptions):
        if not ExportTableOptions.objectName():
            ExportTableOptions.setObjectName(u"ExportTableOptions")
        ExportTableOptions.resize(550, 500)
        ExportTableOptions.setMinimumSize(QSize(550, 500))
        self.verticalLayout_3 = QVBoxLayout(ExportTableOptions)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(ExportTableOptions)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.file_chooser = FileChooser(ExportTableOptions)
        self.file_chooser.setObjectName(u"file_chooser")

        self.verticalLayout_3.addWidget(self.file_chooser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(ExportTableOptions)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_select_all = QPushButton(ExportTableOptions)
        self.btn_select_all.setObjectName(u"btn_select_all")

        self.horizontalLayout.addWidget(self.btn_select_all)

        self.btn_deselect_all = QPushButton(ExportTableOptions)
        self.btn_deselect_all.setObjectName(u"btn_deselect_all")

        self.horizontalLayout.addWidget(self.btn_deselect_all)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.list_columns = CheckableList(ExportTableOptions)
        self.list_columns.setObjectName(u"list_columns")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_columns.sizePolicy().hasHeightForWidth())
        self.list_columns.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.list_columns)

        self.expand_frame = QFrame(ExportTableOptions)
        self.expand_frame.setObjectName(u"expand_frame")
        self.expand_frame.setMinimumSize(QSize(0, 0))
        self.expand_frame.setFrameShape(QFrame.NoFrame)
        self.expand_frame.setFrameShadow(QFrame.Plain)
        self.expand_frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.expand_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_expand = QLabel(self.expand_frame)
        self.lbl_expand.setObjectName(u"lbl_expand")
        font2 = QFont()
        font2.setBold(False)
        font2.setWeight(50)
        self.lbl_expand.setFont(font2)
        self.lbl_expand.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_expand)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radio_expand = QRadioButton(self.expand_frame)
        self.radiogroup_expand = QButtonGroup(ExportTableOptions)
        self.radiogroup_expand.setObjectName(u"radiogroup_expand")
        self.radiogroup_expand.addButton(self.radio_expand)
        self.radio_expand.setObjectName(u"radio_expand")
        self.radio_expand.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radio_expand)

        self.radio_backup = QRadioButton(self.expand_frame)
        self.radiogroup_expand.addButton(self.radio_backup)
        self.radio_backup.setObjectName(u"radio_backup")

        self.horizontalLayout_2.addWidget(self.radio_backup)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.expand_widget = QWidget(self.expand_frame)
        self.expand_widget.setObjectName(u"expand_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.expand_widget.sizePolicy().hasHeightForWidth())
        self.expand_widget.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.expand_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.list_expand_columns = CheckableList(self.expand_widget)
        self.list_expand_columns.setObjectName(u"list_expand_columns")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.list_expand_columns.sizePolicy().hasHeightForWidth())
        self.list_expand_columns.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.list_expand_columns, 3, 1, 3, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_expand_select_required = QPushButton(self.expand_widget)
        self.btn_expand_select_required.setObjectName(u"btn_expand_select_required")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_expand_select_required.sizePolicy().hasHeightForWidth())
        self.btn_expand_select_required.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.btn_expand_select_required)

        self.btn_expand_select_all = QPushButton(self.expand_widget)
        self.btn_expand_select_all.setObjectName(u"btn_expand_select_all")
        sizePolicy3.setHeightForWidth(self.btn_expand_select_all.sizePolicy().hasHeightForWidth())
        self.btn_expand_select_all.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.btn_expand_select_all)

        self.btn_expand_deselect_all = QPushButton(self.expand_widget)
        self.btn_expand_deselect_all.setObjectName(u"btn_expand_deselect_all")

        self.verticalLayout.addWidget(self.btn_expand_deselect_all)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 4, 0, 1, 1)

        self.combo_expand_table = QComboBox(self.expand_widget)
        self.combo_expand_table.setObjectName(u"combo_expand_table")
        self.combo_expand_table.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.combo_expand_table, 3, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.expand_widget)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.verticalLayout_3.addWidget(self.expand_frame)


        self.retranslateUi(ExportTableOptions)

        QMetaObject.connectSlotsByName(ExportTableOptions)
    # setupUi

    def retranslateUi(self, ExportTableOptions):
        ExportTableOptions.setWindowTitle(QCoreApplication.translate("ExportTableOptions", u"Form", None))
        self.label.setText(QCoreApplication.translate("ExportTableOptions", u"Table export options", None))
        self.label_2.setText(QCoreApplication.translate("ExportTableOptions", u"Select columns to export", None))
        self.btn_select_all.setText(QCoreApplication.translate("ExportTableOptions", u"Select all", None))
        self.btn_deselect_all.setText(QCoreApplication.translate("ExportTableOptions", u"Deselect all", None))
        self.lbl_expand.setText(QCoreApplication.translate("ExportTableOptions", u"The selected table is related to the following tables: <b>{1}</b>.\n"
"Do you want to add columns from this/these table(s)?", None))
        self.radio_expand.setText(QCoreApplication.translate("ExportTableOptions", u"Yes", None))
        self.radio_backup.setText(QCoreApplication.translate("ExportTableOptions", u"No, just do a backup of the current table", None))
        self.btn_expand_select_required.setText(QCoreApplication.translate("ExportTableOptions", u"Select required\n"
"columns for import", None))
        self.btn_expand_select_all.setText(QCoreApplication.translate("ExportTableOptions", u"Select All", None))
        self.btn_expand_deselect_all.setText(QCoreApplication.translate("ExportTableOptions", u"Deselect all", None))
    # retranslateUi

