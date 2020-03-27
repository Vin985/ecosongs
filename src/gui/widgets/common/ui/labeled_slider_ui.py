# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'labeled_slider.ui'
##
# Created by: Qt User Interface Compiler version 5.14.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class Ui_LabeledSlider(object):
    HPOS = ["left", "right"]
    VPOS = ["top", "bottom"]

    def setupUi(self, LabeledSlider, text_pos="right", text_align="center"):
        self.text_pos = text_pos
        if LabeledSlider.objectName():
            LabeledSlider.setObjectName(u"LabeledSlider")
        LabeledSlider.resize(400, 35)

        if self.is_horizontal():
            self.layout = QHBoxLayout(LabeledSlider)
        else:
            self.layout = QVBoxLayout(LabeledSlider)
        self.layout.setObjectName(u"layout")

        self.slider = QSlider(LabeledSlider)
        self.slider.setObjectName(u"slider")
        self.slider.setOrientation(Qt.Horizontal)

        self.lbl_value = QLabel(LabeledSlider)
        self.lbl_value.setObjectName(u"lbl_value")
        if text_align == "center":
            self.lbl_value.setAlignment(Qt.AlignCenter)
        elif text_align == "right":
            self.lbl_value.setAlignment(
                Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        else:
            self.lbl_value.setAlignment(
                Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        if self.text_pos in ["left", "top"]:
            self.layout.addWidget(self.lbl_value)
            self.layout.addWidget(self.slider)
        else:
            self.layout.addWidget(self.slider)
            self.layout.addWidget(self.lbl_value)

        self.retranslateUi(LabeledSlider)

        QMetaObject.connectSlotsByName(LabeledSlider)

    def is_horizontal(self):
        return self.text_pos in self.HPOS

    def is_vertical(self):
        return self.text_pos in self.VPOS
    # setupUi

    def retranslateUi(self, LabeledSlider):
        LabeledSlider.setWindowTitle(
            QCoreApplication.translate("LabeledSlider", u"Form", None))
        self.lbl_value.setText("")
    # retranslateUi
