# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progressdialog.ui'
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


class Ui_ProgressDialog(object):
    def setupUi(self, ProgressDialog):
        if not ProgressDialog.objectName():
            ProgressDialog.setObjectName(u"ProgressDialog")
        ProgressDialog.resize(577, 498)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressDialog.sizePolicy().hasHeightForWidth())
        ProgressDialog.setSizePolicy(sizePolicy)
        ProgressDialog.setMaximumSize(QSize(16777215, 16777214))
        self.verticalLayout = QVBoxLayout(ProgressDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.content_layout = QHBoxLayout()
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.verticalLayout.addLayout(self.content_layout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(ProgressDialog)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_start = QPushButton(ProgressDialog)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout.addWidget(self.btn_start)

        self.btn_close = QPushButton(ProgressDialog)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout.addWidget(self.btn_close)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.progress_bar = QProgressBar(ProgressDialog)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.gridLayout_2.addWidget(self.progress_bar, 2, 0, 1, 1)

        self.lbl_message = QLabel(ProgressDialog)
        self.lbl_message.setObjectName(u"lbl_message")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_message.sizePolicy().hasHeightForWidth())
        self.lbl_message.setSizePolicy(sizePolicy1)
        self.lbl_message.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lbl_message, 1, 0, 1, 1)

        self.lbl_error = QLabel(ProgressDialog)
        self.lbl_error.setObjectName(u"lbl_error")
        sizePolicy1.setHeightForWidth(self.lbl_error.sizePolicy().hasHeightForWidth())
        self.lbl_error.setSizePolicy(sizePolicy1)
        self.lbl_error.setStyleSheet(u"#lbl_error {color: red}")
        self.lbl_error.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lbl_error, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(ProgressDialog)

        QMetaObject.connectSlotsByName(ProgressDialog)
    # setupUi

    def retranslateUi(self, ProgressDialog):
        ProgressDialog.setWindowTitle(QCoreApplication.translate("ProgressDialog", u"Dialog", None))
        self.btn_cancel.setText(QCoreApplication.translate("ProgressDialog", u"Cancel", None))
        self.btn_start.setText(QCoreApplication.translate("ProgressDialog", u"Start", None))
        self.btn_close.setText(QCoreApplication.translate("ProgressDialog", u"Close", None))
        self.lbl_message.setText("")
        self.lbl_error.setText("")
    # retranslateUi

