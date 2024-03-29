# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis.ui'
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

from gui.widgets.analysis.detection_evaluator import DetectionEvaluator
from gui.widgets.plot.sensitivity_plot import SensitivityPlot


class Ui_Analysis(object):
    def setupUi(self, Analysis):
        if not Analysis.objectName():
            Analysis.setObjectName(u"Analysis")
        Analysis.resize(506, 366)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Analysis.sizePolicy().hasHeightForWidth())
        Analysis.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Analysis)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.analysis_tabs = QTabWidget(Analysis)
        self.analysis_tabs.setObjectName(u"analysis_tabs")
        self.detector_evaluation = DetectionEvaluator()
        self.detector_evaluation.setObjectName(u"detector_evaluation")
        self.analysis_tabs.addTab(self.detector_evaluation, "")
        self.plot = SensitivityPlot()
        self.plot.setObjectName(u"plot")
        self.analysis_tabs.addTab(self.plot, "")

        self.horizontalLayout.addWidget(self.analysis_tabs)


        self.retranslateUi(Analysis)

        self.analysis_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Analysis)
    # setupUi

    def retranslateUi(self, Analysis):
        Analysis.setWindowTitle(QCoreApplication.translate("Analysis", u"Form", None))
        self.analysis_tabs.setTabText(self.analysis_tabs.indexOf(self.detector_evaluation), QCoreApplication.translate("Analysis", u"Evaluate detector", None))
        self.analysis_tabs.setTabText(self.analysis_tabs.indexOf(self.plot), QCoreApplication.translate("Analysis", u"Sensitivity Plot", None))
    # retranslateUi

