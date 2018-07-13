# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbexplorer.ui',
# licensing of 'dbexplorer.ui' applies.
#
# Created: Fri Jul 13 17:36:34 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1530708810518
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DBExplorer(object):
    def setupUi(self, DBExplorer):
        DBExplorer.setObjectName("DBExplorer")
        DBExplorer.resize(1075, 564)
        self.gridLayout = QtWidgets.QGridLayout(DBExplorer)
        self.gridLayout.setObjectName("gridLayout")
        self.dbOptions = QtWidgets.QGroupBox(DBExplorer)
        self.dbOptions.setObjectName("dbOptions")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dbOptions)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dbLoadButton = QtWidgets.QPushButton(self.dbOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbLoadButton.sizePolicy().hasHeightForWidth())
        self.dbLoadButton.setSizePolicy(sizePolicy)
        self.dbLoadButton.setObjectName("dbLoadButton")
        self.gridLayout_2.addWidget(self.dbLoadButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.dbOptions, 0, 0, 1, 1)
        self.dbTable = QtWidgets.QTableView(DBExplorer)
        self.dbTable.setEnabled(True)
        self.dbTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dbTable.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.dbTable.setSortingEnabled(True)
        self.dbTable.setWordWrap(True)
        self.dbTable.setObjectName("dbTable")
        self.dbTable.horizontalHeader().setStretchLastSection(True)
        self.dbTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.dbTable, 2, 0, 1, 1)
        self.rowsFound = QtWidgets.QLabel(DBExplorer)
        self.rowsFound.setObjectName("rowsFound")
        self.gridLayout.addWidget(self.rowsFound, 1, 0, 1, 1)

        self.retranslateUi(DBExplorer)
        QtCore.QMetaObject.connectSlotsByName(DBExplorer)

    def retranslateUi(self, DBExplorer):
        DBExplorer.setWindowTitle(QtWidgets.QApplication.translate("DBExplorer", "Form", None, -1))
        self.dbOptions.setTitle(QtWidgets.QApplication.translate("DBExplorer", "Database Explorer", None, -1))
        self.dbLoadButton.setText(QtWidgets.QApplication.translate("DBExplorer", "Load file(s) into database", None, -1))
        self.rowsFound.setText(QtWidgets.QApplication.translate("DBExplorer", "TextLabel", None, -1))

