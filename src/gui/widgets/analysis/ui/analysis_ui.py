# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis.ui'
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

from gui.widgets.analysis.detection_evaluator import DetectionEvaluator


class Ui_Analysis(object):
    def setupUi(self, Analysis):
        if Analysis.objectName():
            Analysis.setObjectName(u"Analysis")
        Analysis.resize(506, 366)
        self.horizontalLayout = QHBoxLayout(Analysis)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.analysis_tabs = QTabWidget(Analysis)
        self.analysis_tabs.setObjectName(u"analysis_tabs")
        self.detector_evaluation = DetectionEvaluator()
        self.detector_evaluation.setObjectName(u"detector_evaluation")
        self.analysis_tabs.addTab(self.detector_evaluation, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.analysis_tabs.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.analysis_tabs)


        self.retranslateUi(Analysis)

        QMetaObject.connectSlotsByName(Analysis)
    # setupUi

    def retranslateUi(self, Analysis):
        Analysis.setWindowTitle(QCoreApplication.translate("Analysis", u"Form", None))
        self.analysis_tabs.setTabText(self.analysis_tabs.indexOf(self.detector_evaluation), QCoreApplication.translate("Analysis", u"Evaluate detector", None))
        self.analysis_tabs.setTabText(self.analysis_tabs.indexOf(self.tab_2), QCoreApplication.translate("Analysis", u"Tab 2", None))
    # retranslateUi

