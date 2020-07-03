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
        SongEventsOptions.resize(482, 141)
        self.gridLayout_2 = QGridLayout(SongEventsOptions)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(SongEventsOptions)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)

        self.spin_end_threshold = QDoubleSpinBox(SongEventsOptions)
        self.spin_end_threshold.setObjectName(u"spin_end_threshold")
        self.spin_end_threshold.setKeyboardTracking(False)
        self.spin_end_threshold.setMaximum(1.000000000000000)
        self.spin_end_threshold.setSingleStep(0.010000000000000)
        self.spin_end_threshold.setValue(0.600000000000000)

        self.gridLayout_2.addWidget(self.spin_end_threshold, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer, 9, 0, 1, 2)

        self.label_8 = QLabel(SongEventsOptions)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)

        self.label_7 = QLabel(SongEventsOptions)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_4 = QLabel(SongEventsOptions)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.spin_activity = QDoubleSpinBox(SongEventsOptions)
        self.spin_activity.setObjectName(u"spin_activity")
        self.spin_activity.setKeyboardTracking(False)
        self.spin_activity.setMaximum(1.000000000000000)
        self.spin_activity.setSingleStep(0.010000000000000)
        self.spin_activity.setValue(0.950000000000000)

        self.gridLayout_2.addWidget(self.spin_activity, 4, 1, 1, 1)

        self.combo_method = QComboBox(SongEventsOptions)
        self.combo_method.setObjectName(u"combo_method")

        self.gridLayout_2.addWidget(self.combo_method, 0, 1, 1, 1)

        self.spin_min_duration = QDoubleSpinBox(SongEventsOptions)
        self.spin_min_duration.setObjectName(u"spin_min_duration")
        self.spin_min_duration.setKeyboardTracking(False)
        self.spin_min_duration.setDecimals(0)
        self.spin_min_duration.setMaximum(10000.000000000000000)
        self.spin_min_duration.setSingleStep(1.000000000000000)
        self.spin_min_duration.setValue(300.000000000000000)

        self.gridLayout_2.addWidget(self.spin_min_duration, 7, 1, 1, 1)

        self.checkbox_isolate_events = QCheckBox(SongEventsOptions)
        self.checkbox_isolate_events.setObjectName(u"checkbox_isolate_events")
        self.checkbox_isolate_events.setEnabled(True)

        self.gridLayout_2.addWidget(self.checkbox_isolate_events, 8, 0, 1, 2)


        self.retranslateUi(SongEventsOptions)

        QMetaObject.connectSlotsByName(SongEventsOptions)
    # setupUi

    def retranslateUi(self, SongEventsOptions):
        SongEventsOptions.setWindowTitle(QCoreApplication.translate("SongEventsOptions", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("SongEventsOptions", u"Activity level", None))
        self.label_8.setText(QCoreApplication.translate("SongEventsOptions", u"End threshold", None))
        self.label_7.setText(QCoreApplication.translate("SongEventsOptions", u"Minimum duration (ms)", None))
        self.label_4.setText(QCoreApplication.translate("SongEventsOptions", u"Method", None))
#if QT_CONFIG(tooltip)
        self.checkbox_isolate_events.setToolTip(QCoreApplication.translate("SongEventsOptions", u"<html><head/><body><p>Returns only isolated events instead of each subsampled time period </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkbox_isolate_events.setText(QCoreApplication.translate("SongEventsOptions", u"Isolate events", None))
    # retranslateUi

