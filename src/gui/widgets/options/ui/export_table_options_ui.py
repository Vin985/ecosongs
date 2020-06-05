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


class Ui_ExportTableOptions(object):
    def setupUi(self, ExportTableOptions):
        if not ExportTableOptions.objectName():
            ExportTableOptions.setObjectName(u"ExportTableOptions")
        ExportTableOptions.resize(400, 300)
        self.gridLayout = QGridLayout(ExportTableOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 2)

        self.radio_expand = QRadioButton(ExportTableOptions)
        self.buttonGroup = QButtonGroup(ExportTableOptions)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radio_expand)
        self.radio_expand.setObjectName(u"radio_expand")

        self.gridLayout.addWidget(self.radio_expand, 1, 1, 1, 1)

        self.radio_raw = QRadioButton(ExportTableOptions)
        self.buttonGroup.addButton(self.radio_raw)
        self.radio_raw.setObjectName(u"radio_raw")

        self.gridLayout.addWidget(self.radio_raw, 1, 0, 1, 1)

        self.label = QLabel(ExportTableOptions)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.retranslateUi(ExportTableOptions)

        QMetaObject.connectSlotsByName(ExportTableOptions)
    # setupUi

    def retranslateUi(self, ExportTableOptions):
        ExportTableOptions.setWindowTitle(QCoreApplication.translate("ExportTableOptions", u"Form", None))
        self.radio_expand.setText(QCoreApplication.translate("ExportTableOptions", u"RadioButton", None))
        self.radio_raw.setText(QCoreApplication.translate("ExportTableOptions", u"RadioButton", None))
        self.label.setText(QCoreApplication.translate("ExportTableOptions", u"Table export options", None))
    # retranslateUi

