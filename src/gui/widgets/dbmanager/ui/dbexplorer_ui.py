# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbexplorer.ui',
# licensing of 'dbexplorer.ui' applies.
#
# Created: Wed Nov  7 23:14:36 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1530708810518
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DBExplorer(object):
    def setupUi(self, DBExplorer):
        DBExplorer.setObjectName("DBExplorer")
        DBExplorer.resize(1075, 564)
        DBExplorer.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.gridLayout = QtWidgets.QGridLayout(DBExplorer)
        self.gridLayout.setObjectName("gridLayout")
        self.dbOptions = QtWidgets.QGroupBox(DBExplorer)
        self.dbOptions.setObjectName("dbOptions")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dbOptions)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dbImportButton = QtWidgets.QPushButton(self.dbOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbImportButton.sizePolicy().hasHeightForWidth())
        self.dbImportButton.setSizePolicy(sizePolicy)
        self.dbImportButton.setObjectName("dbImportButton")
        self.gridLayout_2.addWidget(self.dbImportButton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.btn_export = QtWidgets.QPushButton(self.dbOptions)
        self.btn_export.setObjectName("btn_export")
        self.gridLayout_2.addWidget(self.btn_export, 0, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_table = QtWidgets.QLabel(self.dbOptions)
        self.lbl_table.setObjectName("lbl_table")
        self.horizontalLayout.addWidget(self.lbl_table)
        self.comboBox_table = QtWidgets.QComboBox(self.dbOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_table.sizePolicy().hasHeightForWidth())
        self.comboBox_table.setSizePolicy(sizePolicy)
        self.comboBox_table.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_table.setObjectName("comboBox_table")
        self.horizontalLayout.addWidget(self.comboBox_table)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 5)
        self.gridLayout.addWidget(self.dbOptions, 0, 0, 1, 1)
        self.dbTable = QtWidgets.QTableView(DBExplorer)
        self.dbTable.setEnabled(True)
        self.dbTable.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.dbTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dbTable.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.dbTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.dbTable.setSortingEnabled(True)
        self.dbTable.setObjectName("dbTable")
        self.dbTable.horizontalHeader().setStretchLastSection(True)
        self.dbTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.dbTable, 2, 0, 1, 1)
        self.rowsFound = QtWidgets.QLabel(DBExplorer)
        self.rowsFound.setObjectName("rowsFound")
        self.gridLayout.addWidget(self.rowsFound, 1, 0, 1, 1)
        self.action_ACI = QtWidgets.QAction(DBExplorer)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tango/audio"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_ACI.setIcon(icon)
        self.action_ACI.setObjectName("action_ACI")

        self.retranslateUi(DBExplorer)
        QtCore.QMetaObject.connectSlotsByName(DBExplorer)

    def retranslateUi(self, DBExplorer):
        DBExplorer.setWindowTitle(QtWidgets.QApplication.translate("DBExplorer", "Form", None, -1))
        self.dbOptions.setTitle(QtWidgets.QApplication.translate("DBExplorer", "Database Explorer", None, -1))
        self.dbImportButton.setText(QtWidgets.QApplication.translate("DBExplorer", "Import file(s) into database", None, -1))
        self.btn_export.setText(QtWidgets.QApplication.translate("DBExplorer", "Export database", None, -1))
        self.lbl_table.setText(QtWidgets.QApplication.translate("DBExplorer", "Select table to display", None, -1))
        self.rowsFound.setText(QtWidgets.QApplication.translate("DBExplorer", "TextLabel", None, -1))
        self.action_ACI.setText(QtWidgets.QApplication.translate("DBExplorer", "Calculate ACI", None, -1))
        self.action_ACI.setToolTip(QtWidgets.QApplication.translate("DBExplorer", "hello world!", None, -1))
        self.action_ACI.setShortcut(QtWidgets.QApplication.translate("DBExplorer", "Alt+A", None, -1))

