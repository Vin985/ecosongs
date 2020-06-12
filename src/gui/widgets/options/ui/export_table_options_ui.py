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
        ExportTableOptions.resize(582, 514)
        self.gridLayout = QGridLayout(ExportTableOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(8)
        self.label = QLabel(ExportTableOptions)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_2 = QLabel(ExportTableOptions)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.list_columns = CheckableList(ExportTableOptions)
        self.list_columns.setObjectName(u"list_columns")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_columns.sizePolicy().hasHeightForWidth())
        self.list_columns.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.list_columns, 3, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_select_all = QPushButton(ExportTableOptions)
        self.btn_select_all.setObjectName(u"btn_select_all")

        self.horizontalLayout.addWidget(self.btn_select_all)

        self.btn_deselect_all = QPushButton(ExportTableOptions)
        self.btn_deselect_all.setObjectName(u"btn_deselect_all")

        self.horizontalLayout.addWidget(self.btn_deselect_all)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.file_chooser = FileChooser(ExportTableOptions)
        self.file_chooser.setObjectName(u"file_chooser")

        self.gridLayout.addWidget(self.file_chooser, 1, 0, 1, 2)

        self.expand_widget = QWidget(ExportTableOptions)
        self.expand_widget.setObjectName(u"expand_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.expand_widget.sizePolicy().hasHeightForWidth())
        self.expand_widget.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.expand_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_expand = QLabel(self.expand_widget)
        self.lbl_expand.setObjectName(u"lbl_expand")
        font2 = QFont()
        font2.setBold(False)
        font2.setWeight(50)
        self.lbl_expand.setFont(font2)
        self.lbl_expand.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lbl_expand, 0, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_expand_select_required = QPushButton(self.expand_widget)
        self.btn_expand_select_required.setObjectName(u"btn_expand_select_required")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_expand_select_required.sizePolicy().hasHeightForWidth())
        self.btn_expand_select_required.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.btn_expand_select_required)

        self.btn_expand_select_all = QPushButton(self.expand_widget)
        self.btn_expand_select_all.setObjectName(u"btn_expand_select_all")
        sizePolicy2.setHeightForWidth(self.btn_expand_select_all.sizePolicy().hasHeightForWidth())
        self.btn_expand_select_all.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.btn_expand_select_all)

        self.btn_expand_deselect_all = QPushButton(self.expand_widget)
        self.btn_expand_deselect_all.setObjectName(u"btn_expand_deselect_all")

        self.verticalLayout.addWidget(self.btn_expand_deselect_all)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.combo_expand_table = QComboBox(self.expand_widget)
        self.combo_expand_table.setObjectName(u"combo_expand_table")
        self.combo_expand_table.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.combo_expand_table, 1, 0, 1, 1)

        self.list_expand_columns = CheckableList(self.expand_widget)
        self.list_expand_columns.setObjectName(u"list_expand_columns")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.list_expand_columns.sizePolicy().hasHeightForWidth())
        self.list_expand_columns.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.list_expand_columns, 1, 1, 3, 1)


        self.gridLayout.addWidget(self.expand_widget, 4, 0, 1, 2)


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
        self.btn_expand_select_required.setText(QCoreApplication.translate("ExportTableOptions", u"Select required\n"
"columns for import", None))
        self.btn_expand_select_all.setText(QCoreApplication.translate("ExportTableOptions", u"Select All", None))
        self.btn_expand_deselect_all.setText(QCoreApplication.translate("ExportTableOptions", u"Deselect all", None))
    # retranslateUi

