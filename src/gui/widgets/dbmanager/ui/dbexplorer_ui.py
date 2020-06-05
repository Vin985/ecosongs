# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dbexplorer.ui'
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


class Ui_DBExplorer(object):
    def setupUi(self, DBExplorer):
        if not DBExplorer.objectName():
            DBExplorer.setObjectName(u"DBExplorer")
        DBExplorer.resize(1075, 564)
        DBExplorer.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.action_ACI = QAction(DBExplorer)
        self.action_ACI.setObjectName(u"action_ACI")
        icon = QIcon()
        icon.addFile(u":/tango/audio", QSize(), QIcon.Normal, QIcon.On)
        self.action_ACI.setIcon(icon)
        self.gridLayout = QGridLayout(DBExplorer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dbOptions = QGroupBox(DBExplorer)
        self.dbOptions.setObjectName(u"dbOptions")
        self.gridLayout_2 = QGridLayout(self.dbOptions)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_table = QLabel(self.dbOptions)
        self.lbl_table.setObjectName(u"lbl_table")

        self.horizontalLayout.addWidget(self.lbl_table)

        self.combo_table = QComboBox(self.dbOptions)
        self.combo_table.addItem("")
        self.combo_table.setObjectName(u"combo_table")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_table.sizePolicy().hasHeightForWidth())
        self.combo_table.setSizePolicy(sizePolicy)
        self.combo_table.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.combo_table)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_export = QPushButton(self.dbOptions)
        self.btn_export.setObjectName(u"btn_export")

        self.horizontalLayout.addWidget(self.btn_export)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 3)


        self.gridLayout.addWidget(self.dbOptions, 0, 0, 1, 1)

        self.dbTable = QTableView(DBExplorer)
        self.dbTable.setObjectName(u"dbTable")
        self.dbTable.setEnabled(True)
        self.dbTable.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.dbTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.dbTable.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.dbTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dbTable.setSortingEnabled(True)
        self.dbTable.horizontalHeader().setStretchLastSection(True)
        self.dbTable.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.dbTable, 2, 0, 1, 1)

        self.rowsFound = QLabel(DBExplorer)
        self.rowsFound.setObjectName(u"rowsFound")

        self.gridLayout.addWidget(self.rowsFound, 1, 0, 1, 1)


        self.retranslateUi(DBExplorer)

        QMetaObject.connectSlotsByName(DBExplorer)
    # setupUi

    def retranslateUi(self, DBExplorer):
        DBExplorer.setWindowTitle(QCoreApplication.translate("DBExplorer", u"Form", None))
        self.action_ACI.setText(QCoreApplication.translate("DBExplorer", u"Calculate ACI", None))
#if QT_CONFIG(tooltip)
        self.action_ACI.setToolTip(QCoreApplication.translate("DBExplorer", u"hello world!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_ACI.setShortcut(QCoreApplication.translate("DBExplorer", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
        self.dbOptions.setTitle(QCoreApplication.translate("DBExplorer", u"Database Explorer", None))
        self.lbl_table.setText(QCoreApplication.translate("DBExplorer", u"Select table to display", None))
        self.combo_table.setItemText(0, QCoreApplication.translate("DBExplorer", u"-- Select a table to display --", None))

        self.btn_export.setText(QCoreApplication.translate("DBExplorer", u"Export table", None))
        self.rowsFound.setText(QCoreApplication.translate("DBExplorer", u"TextLabel", None))
    # retranslateUi

