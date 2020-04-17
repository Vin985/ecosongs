# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sensitivity_plot.ui'
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

from pyqtgraph.parametertree import ParameterTree
from pyqtgraph import GraphicsLayoutWidget


class Ui_SensitivityPlot(object):
    def setupUi(self, SensitivityPlot):
        if SensitivityPlot.objectName():
            SensitivityPlot.setObjectName(u"SensitivityPlot")
        SensitivityPlot.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(SensitivityPlot)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plot_layout = GraphicsLayoutWidget(SensitivityPlot)
        self.plot_layout.setObjectName(u"plot_layout")

        self.gridLayout_2.addWidget(self.plot_layout, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_plot = QPushButton(SensitivityPlot)
        self.btn_plot.setObjectName(u"btn_plot")

        self.verticalLayout_3.addWidget(self.btn_plot)

        self.plot_options = ParameterTree(SensitivityPlot)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.plot_options.setHeaderItem(__qtreewidgetitem)
        self.plot_options.setObjectName(u"plot_options")

        self.verticalLayout_3.addWidget(self.plot_options)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(SensitivityPlot)

        QMetaObject.connectSlotsByName(SensitivityPlot)
    # setupUi

    def retranslateUi(self, SensitivityPlot):
        SensitivityPlot.setWindowTitle(QCoreApplication.translate("SensitivityPlot", u"Form", None))
        self.btn_plot.setText(QCoreApplication.translate("SensitivityPlot", u"PushButton", None))
    # retranslateUi

