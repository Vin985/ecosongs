# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_chooser.ui'
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


class Ui_FileChooser(object):
    def setupUi(self, FileChooser):
        if not FileChooser.objectName():
            FileChooser.setObjectName(u"FileChooser")
        FileChooser.resize(492, 59)
        self.horizontalLayout = QHBoxLayout(FileChooser)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.input_path = QLineEdit(FileChooser)
        self.input_path.setObjectName(u"input_path")

        self.horizontalLayout.addWidget(self.input_path)

        self.btn_browse = QPushButton(FileChooser)
        self.btn_browse.setObjectName(u"btn_browse")

        self.horizontalLayout.addWidget(self.btn_browse)


        self.retranslateUi(FileChooser)

        QMetaObject.connectSlotsByName(FileChooser)
    # setupUi

    def retranslateUi(self, FileChooser):
        FileChooser.setWindowTitle(QCoreApplication.translate("FileChooser", u"Form", None))
        self.btn_browse.setText(QCoreApplication.translate("FileChooser", u"Browse...", None))
    # retranslateUi

