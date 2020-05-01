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

from pysoundplayer.gui.QSoundPlayer import QSoundPlayer
from pysoundplayer.gui.QImageOptions import QImageOptions
from pysoundplayer.gui.QSpectrogramViewer import QSpectrogramViewer
from pysoundplayer.gui.QSpectrogramOptions import QSpectrogramOptions


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
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tree_view = QTreeView(self.verticalLayoutWidget)
        self.tree_view.setObjectName(u"tree_view")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_view.sizePolicy().hasHeightForWidth())
        self.tree_view.setSizePolicy(sizePolicy)
        self.tree_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree_view.setUniformRowHeights(True)
        self.tree_view.setHeaderHidden(True)
        self.tree_view.header().setVisible(False)

        self.verticalLayout_6.addWidget(self.tree_view)

        self.splitter.addWidget(self.verticalLayoutWidget)
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
        self.label = QLabel(self.details_pane)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.label_5 = QLabel(self.details_pane)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.lbl_year = QLabel(self.details_pane)
        self.lbl_year.setObjectName(u"lbl_year")

        self.gridLayout_2.addWidget(self.lbl_year, 0, 3, 1, 1)

        self.label_3 = QLabel(self.details_pane)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 2, 1, 1)

        self.lbl_name = QLabel(self.details_pane)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout_2.addWidget(self.lbl_name, 2, 1, 1, 1)

        self.lbl_id = QLabel(self.details_pane)
        self.lbl_id.setObjectName(u"lbl_id")

        self.gridLayout_2.addWidget(self.lbl_id, 0, 1, 1, 1)

        self.label_2 = QLabel(self.details_pane)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.lbl_path = QLabel(self.details_pane)
        self.lbl_path.setObjectName(u"lbl_path")

        self.gridLayout_2.addWidget(self.lbl_path, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.spectrogram_viewer = QSpectrogramViewer(self.details_pane)
        self.spectrogram_viewer.setObjectName(u"spectrogram_viewer")
        sizePolicy.setHeightForWidth(self.spectrogram_viewer.sizePolicy().hasHeightForWidth())
        self.spectrogram_viewer.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.spectrogram_viewer)

        self.sound_player = QSoundPlayer(self.details_pane)
        self.sound_player.setObjectName(u"sound_player")

        self.verticalLayout.addWidget(self.sound_player)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.details_pane)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.spectrogram_options = QSpectrogramOptions(self.groupBox)
        self.spectrogram_options.setObjectName(u"spectrogram_options")

        self.verticalLayout_2.addWidget(self.spectrogram_options)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.details_pane)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.image_options = QImageOptions(self.groupBox_2)
        self.image_options.setObjectName(u"image_options")

        self.verticalLayout_3.addWidget(self.image_options)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.group_draw_events = QGroupBox(self.details_pane)
        self.group_draw_events.setObjectName(u"group_draw_events")
        self.group_draw_events.setCheckable(True)
        self.gridLayout = QGridLayout(self.group_draw_events)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(self.group_draw_events)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.slider_activity = QSlider(self.group_draw_events)
        self.slider_activity.setObjectName(u"slider_activity")
        self.slider_activity.setMaximum(100)
        self.slider_activity.setValue(95)
        self.slider_activity.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_activity, 2, 1, 1, 1)

        self.label_8 = QLabel(self.group_draw_events)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.slider_end_threshold = QSlider(self.group_draw_events)
        self.slider_end_threshold.setObjectName(u"slider_end_threshold")
        self.slider_end_threshold.setValue(60)
        self.slider_end_threshold.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_end_threshold, 3, 1, 1, 1)

        self.label_7 = QLabel(self.group_draw_events)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.spin_min_duration = QDoubleSpinBox(self.group_draw_events)
        self.spin_min_duration.setObjectName(u"spin_min_duration")
        self.spin_min_duration.setDecimals(0)
        self.spin_min_duration.setMaximum(10000.000000000000000)
        self.spin_min_duration.setSingleStep(1.000000000000000)
        self.spin_min_duration.setValue(30.000000000000000)

        self.gridLayout.addWidget(self.spin_min_duration, 4, 1, 1, 1)

        self.label_6 = QLabel(self.group_draw_events)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_export_pdf = QPushButton(self.group_draw_events)
        self.btn_export_pdf.setObjectName(u"btn_export_pdf")

        self.horizontalLayout.addWidget(self.btn_export_pdf)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.label_4 = QLabel(self.group_draw_events)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.combo_method = QComboBox(self.group_draw_events)
        self.combo_method.addItem("")
        self.combo_method.addItem("")
        self.combo_method.setObjectName(u"combo_method")

        self.gridLayout.addWidget(self.combo_method, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.group_draw_events)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

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
        self.label.setText(QCoreApplication.translate("AudioManager", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("AudioManager", u"Year", None))
        self.lbl_year.setText("")
        self.label_3.setText(QCoreApplication.translate("AudioManager", u"Path", None))
        self.lbl_name.setText("")
        self.lbl_id.setText("")
        self.label_2.setText(QCoreApplication.translate("AudioManager", u"Id", None))
        self.lbl_path.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("AudioManager", u"Spectrogram", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AudioManager", u"Image", None))
        self.group_draw_events.setTitle(QCoreApplication.translate("AudioManager", u"Draw events", None))
        self.label_9.setText(QCoreApplication.translate("AudioManager", u"Activity level", None))
        self.label_8.setText(QCoreApplication.translate("AudioManager", u"End threshold", None))
        self.label_7.setText(QCoreApplication.translate("AudioManager", u"Minimum duration (ms)", None))
        self.label_6.setText(QCoreApplication.translate("AudioManager", u"Detect songs in selected recordings", None))
        self.btn_export_pdf.setText(QCoreApplication.translate("AudioManager", u"Export events to pdf", None))
        self.label_4.setText(QCoreApplication.translate("AudioManager", u"Method", None))
        self.combo_method.setItemText(0, QCoreApplication.translate("AudioManager", u"Event detection", None))
        self.combo_method.setItemText(1, QCoreApplication.translate("AudioManager", u"Subsampling", None))

    # retranslateUi

