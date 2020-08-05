# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'song_events_options.ui'
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


class Ui_SongEventsOptions(object):
    def setupUi(self, SongEventsOptions):
        if not SongEventsOptions.objectName():
            SongEventsOptions.setObjectName(u"SongEventsOptions")
        SongEventsOptions.resize(524, 213)
        self.gridLayout = QGridLayout(SongEventsOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 11, 0, 1, 2)

        self.label_7 = QLabel(SongEventsOptions)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_4 = QLabel(SongEventsOptions)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_2 = QLabel(SongEventsOptions)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 8, 2, 1, 1)

        self.label = QLabel(SongEventsOptions)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)

        self.label_9 = QLabel(SongEventsOptions)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.spin_activity = QDoubleSpinBox(SongEventsOptions)
        self.spin_activity.setObjectName(u"spin_activity")
        self.spin_activity.setKeyboardTracking(False)
        self.spin_activity.setMaximum(1.000000000000000)
        self.spin_activity.setSingleStep(0.010000000000000)
        self.spin_activity.setValue(0.950000000000000)

        self.gridLayout.addWidget(self.spin_activity, 4, 1, 1, 1)

        self.spin_dtc = QDoubleSpinBox(SongEventsOptions)
        self.spin_dtc.setObjectName(u"spin_dtc")
        self.spin_dtc.setKeyboardTracking(False)
        self.spin_dtc.setMaximum(1.000000000000000)
        self.spin_dtc.setSingleStep(0.010000000000000)
        self.spin_dtc.setValue(0.300000000000000)

        self.gridLayout.addWidget(self.spin_dtc, 8, 1, 1, 1)

        self.checkbox_isolate_events = QCheckBox(SongEventsOptions)
        self.checkbox_isolate_events.setObjectName(u"checkbox_isolate_events")
        self.checkbox_isolate_events.setEnabled(True)

        self.gridLayout.addWidget(self.checkbox_isolate_events, 10, 0, 1, 2)

        self.spin_min_duration = QDoubleSpinBox(SongEventsOptions)
        self.spin_min_duration.setObjectName(u"spin_min_duration")
        self.spin_min_duration.setKeyboardTracking(False)
        self.spin_min_duration.setDecimals(0)
        self.spin_min_duration.setMaximum(10000.000000000000000)
        self.spin_min_duration.setSingleStep(1.000000000000000)
        self.spin_min_duration.setValue(300.000000000000000)

        self.gridLayout.addWidget(self.spin_min_duration, 7, 1, 1, 1)

        self.spin_gtc = QDoubleSpinBox(SongEventsOptions)
        self.spin_gtc.setObjectName(u"spin_gtc")
        self.spin_gtc.setKeyboardTracking(False)
        self.spin_gtc.setMaximum(1.000000000000000)
        self.spin_gtc.setSingleStep(0.010000000000000)
        self.spin_gtc.setValue(0.300000000000000)

        self.gridLayout.addWidget(self.spin_gtc, 8, 3, 1, 1)

        self.label_8 = QLabel(SongEventsOptions)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 2, 1, 1)

        self.spin_end_threshold = QDoubleSpinBox(SongEventsOptions)
        self.spin_end_threshold.setObjectName(u"spin_end_threshold")
        self.spin_end_threshold.setKeyboardTracking(False)
        self.spin_end_threshold.setMaximum(1.000000000000000)
        self.spin_end_threshold.setSingleStep(0.010000000000000)
        self.spin_end_threshold.setValue(0.600000000000000)

        self.gridLayout.addWidget(self.spin_end_threshold, 4, 3, 1, 1)

        self.combo_method = QComboBox(SongEventsOptions)
        self.combo_method.setObjectName(u"combo_method")

        self.gridLayout.addWidget(self.combo_method, 0, 1, 1, 2)


        self.retranslateUi(SongEventsOptions)

        QMetaObject.connectSlotsByName(SongEventsOptions)
    # setupUi

    def retranslateUi(self, SongEventsOptions):
        SongEventsOptions.setWindowTitle(QCoreApplication.translate("SongEventsOptions", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("SongEventsOptions", u"Minimum duration (ms)", None))
        self.label_4.setText(QCoreApplication.translate("SongEventsOptions", u"Method", None))
        self.label_2.setText(QCoreApplication.translate("SongEventsOptions", u"Ground truth tolerance criteria", None))
        self.label.setText(QCoreApplication.translate("SongEventsOptions", u"Detection tolerance criteria", None))
        self.label_9.setText(QCoreApplication.translate("SongEventsOptions", u"Activity level", None))
#if QT_CONFIG(tooltip)
        self.checkbox_isolate_events.setToolTip(QCoreApplication.translate("SongEventsOptions", u"<html><head/><body><p>Returns only isolated events instead of each subsampled time period </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkbox_isolate_events.setText(QCoreApplication.translate("SongEventsOptions", u"Isolate events", None))
        self.label_8.setText(QCoreApplication.translate("SongEventsOptions", u"End threshold", None))
    # retranslateUi

