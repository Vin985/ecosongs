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
        ExportTableOptions.resize(434, 480)
        self.gridLayout = QGridLayout(ExportTableOptions)
        self.gridLayout.setObjectName(u"gridLayout")
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
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.list_columns = CheckableList(ExportTableOptions)
        self.list_columns.setObjectName(u"list_columns")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_columns.sizePolicy().hasHeightForWidth())
        self.list_columns.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.list_columns, 4, 0, 1, 2)

        self.radio_raw = QRadioButton(ExportTableOptions)
        self.buttonGroup = QButtonGroup(ExportTableOptions)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radio_raw)
        self.radio_raw.setObjectName(u"radio_raw")

        self.gridLayout.addWidget(self.radio_raw, 2, 1, 1, 1)

        self.widget = QWidget(ExportTableOptions)
        self.widget.setObjectName(u"widget")

        self.gridLayout.addWidget(self.widget, 5, 0, 1, 2)

        self.radio_expand = QRadioButton(ExportTableOptions)
        self.buttonGroup.addButton(self.radio_expand)
        self.radio_expand.setObjectName(u"radio_expand")
        self.radio_expand.setChecked(True)

        self.gridLayout.addWidget(self.radio_expand, 2, 0, 1, 1)

        self.file_chooser = FileChooser(ExportTableOptions)
        self.file_chooser.setObjectName(u"file_chooser")

        self.gridLayout.addWidget(self.file_chooser, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 2)

        self.expand_widget = QWidget(ExportTableOptions)
        self.expand_widget.setObjectName(u"expand_widget")
        self.gridLayout_2 = QGridLayout(self.expand_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_expand = QLabel(self.expand_widget)
        self.lbl_expand.setObjectName(u"lbl_expand")
        self.lbl_expand.setFont(font1)
        self.lbl_expand.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lbl_expand, 0, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.combo_expand_table = QComboBox(self.expand_widget)
        self.combo_expand_table.setObjectName(u"combo_expand_table")
        self.combo_expand_table.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.combo_expand_table)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.list_expand_columns = CheckableList(self.expand_widget)
        self.list_expand_columns.setObjectName(u"list_expand_columns")

        self.gridLayout_2.addWidget(self.list_expand_columns, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.expand_widget, 7, 0, 1, 2)


        self.retranslateUi(ExportTableOptions)

        QMetaObject.connectSlotsByName(ExportTableOptions)
    # setupUi

    def retranslateUi(self, ExportTableOptions):
        ExportTableOptions.setWindowTitle(QCoreApplication.translate("ExportTableOptions", u"Form", None))
        self.label.setText(QCoreApplication.translate("ExportTableOptions", u"Table export options", None))
        self.label_2.setText(QCoreApplication.translate("ExportTableOptions", u"Select columns to export", None))
#if QT_CONFIG(tooltip)
        self.radio_raw.setToolTip(QCoreApplication.translate("ExportTableOptions", u"Export the table ", None))
#endif // QT_CONFIG(tooltip)
        self.radio_raw.setText(QCoreApplication.translate("ExportTableOptions", u"Raw data", None))
#if QT_CONFIG(tooltip)
        self.radio_expand.setToolTip(QCoreApplication.translate("ExportTableOptions", u"Expand the table by adding columns from related tables", None))
#endif // QT_CONFIG(tooltip)
        self.radio_expand.setText(QCoreApplication.translate("ExportTableOptions", u"Expand table", None))
        self.lbl_expand.setText(QCoreApplication.translate("ExportTableOptions", u"The selected table is related to the following tables: {1}.\n"
"Do you want to add columns from this/these table(s)?", None))
    # retranslateUi

