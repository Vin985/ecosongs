# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'audiomanager.ui'
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

from pysoundplayer.gui.QSpectrogramVizualizer import QSpectrogramVizualizer


class Ui_AudioManager(object):
    def setupUi(self, AudioManager):
        if AudioManager.objectName():
            AudioManager.setObjectName(u"AudioManager")
        AudioManager.resize(984, 682)
        self.action_ACI = QAction(AudioManager)
        self.action_ACI.setObjectName(u"action_ACI")
        self.action_detect_songs = QAction(AudioManager)
        self.action_detect_songs.setObjectName(u"action_detect_songs")
        self.action_delete = QAction(AudioManager)
        self.action_delete.setObjectName(u"action_delete")
        self.action_create_links = QAction(AudioManager)
        self.action_create_links.setObjectName(u"action_create_links")
        self.horizontalLayout_2 = QHBoxLayout(AudioManager)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(AudioManager)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.tree_view = QTreeView(self.splitter)
        self.tree_view.setObjectName(u"tree_view")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_view.sizePolicy().hasHeightForWidth())
        self.tree_view.setSizePolicy(sizePolicy)
        self.tree_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree_view.setUniformRowHeights(True)
        self.tree_view.setHeaderHidden(True)
        self.splitter.addWidget(self.tree_view)
        self.tree_view.header().setVisible(False)
        self.details_pane = QWidget(self.splitter)
        self.details_pane.setObjectName(u"details_pane")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.details_pane.sizePolicy().hasHeightForWidth())
        self.details_pane.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.details_pane)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.details_pane)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.lbl_id = QLabel(self.details_pane)
        self.lbl_id.setObjectName(u"lbl_id")

        self.gridLayout_2.addWidget(self.lbl_id, 0, 1, 1, 1)

        self.label_2 = QLabel(self.details_pane)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.lbl_name = QLabel(self.details_pane)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout_2.addWidget(self.lbl_name, 1, 1, 1, 1)

        self.label_3 = QLabel(self.details_pane)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.lbl_year = QLabel(self.details_pane)
        self.lbl_year.setObjectName(u"lbl_year")

        self.gridLayout_2.addWidget(self.lbl_year, 3, 1, 1, 1)

        self.label = QLabel(self.details_pane)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_5 = QLabel(self.details_pane)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.lbl_path = QLabel(self.details_pane)
        self.lbl_path.setObjectName(u"lbl_path")

        self.gridLayout_2.addWidget(self.lbl_path, 2, 1, 1, 1)

        self.checkbox_draw_events = QCheckBox(self.details_pane)
        self.checkbox_draw_events.setObjectName(u"checkbox_draw_events")
        self.checkbox_draw_events.setChecked(True)

        self.gridLayout_2.addWidget(self.checkbox_draw_events, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_export_pdf = QPushButton(self.details_pane)
        self.btn_export_pdf.setObjectName(u"btn_export_pdf")

        self.horizontalLayout.addWidget(self.btn_export_pdf)


        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.spectrogram_visualizer = QSpectrogramVizualizer(self.details_pane)
        self.spectrogram_visualizer.setObjectName(u"spectrogram_visualizer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spectrogram_visualizer.sizePolicy().hasHeightForWidth())
        self.spectrogram_visualizer.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.spectrogram_visualizer)

        self.splitter.addWidget(self.details_pane)

        self.horizontalLayout_2.addWidget(self.splitter)


        self.retranslateUi(AudioManager)

        QMetaObject.connectSlotsByName(AudioManager)
    # setupUi

    def retranslateUi(self, AudioManager):
        AudioManager.setWindowTitle(QCoreApplication.translate("AudioManager", u"Form", None))
        self.action_ACI.setText(QCoreApplication.translate("AudioManager", u"Compute ACI", None))
        self.action_detect_songs.setText(QCoreApplication.translate("AudioManager", u"Detect bird songs", None))
        self.action_delete.setText(QCoreApplication.translate("AudioManager", u"Delete", None))
        self.action_create_links.setText(QCoreApplication.translate("AudioManager", u"Create virtual links", None))
#if QT_CONFIG(tooltip)
        self.action_create_links.setToolTip(QCoreApplication.translate("AudioManager", u"<html><head/><body><p>Create virtual links to files to easily have human readable filenames</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("AudioManager", u"ACI", None))
        self.lbl_id.setText("")
        self.label_2.setText(QCoreApplication.translate("AudioManager", u"Id", None))
        self.lbl_name.setText("")
        self.label_3.setText(QCoreApplication.translate("AudioManager", u"Path", None))
        self.lbl_year.setText("")
        self.label.setText(QCoreApplication.translate("AudioManager", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("AudioManager", u"Year", None))
        self.lbl_path.setText("")
        self.checkbox_draw_events.setText(QCoreApplication.translate("AudioManager", u"Draw events", None))
        self.btn_export_pdf.setText(QCoreApplication.translate("AudioManager", u"export events", None))
    # retranslateUi

