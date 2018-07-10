# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ecosongs.ui',
# licensing of 'ecosongs.ui' applies.
#
# Created: Tue Jul 10 16:14:04 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1530708810518
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Ecosongs(object):
    def setupUi(self, Ecosongs):
        Ecosongs.setObjectName("Ecosongs")
        Ecosongs.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(Ecosongs)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(-20, 10, 1221, 841))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.left_panel = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_panel.sizePolicy().hasHeightForWidth())
        self.left_panel.setSizePolicy(sizePolicy)
        self.left_panel.setObjectName("left_panel")
        self.center_panel = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center_panel.sizePolicy().hasHeightForWidth())
        self.center_panel.setSizePolicy(sizePolicy)
        self.center_panel.setObjectName("center_panel")
        self.right_panel = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_panel.sizePolicy().hasHeightForWidth())
        self.right_panel.setSizePolicy(sizePolicy)
        self.right_panel.setTabPosition(QtWidgets.QTabWidget.East)
        self.right_panel.setObjectName("right_panel")
        self.right_panelPage1 = QtWidgets.QWidget()
        self.right_panelPage1.setObjectName("right_panelPage1")
        self.right_panel.addTab(self.right_panelPage1, "")
        Ecosongs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ecosongs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuAnalyses = QtWidgets.QMenu(self.menubar)
        self.menuAnalyses.setObjectName("menuAnalyses")
        Ecosongs.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ecosongs)
        self.statusbar.setObjectName("statusbar")
        Ecosongs.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(Ecosongs)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(Ecosongs)
        self.actionHelp.setObjectName("actionHelp")
        self.actionOpen_File_s = QtWidgets.QAction(Ecosongs)
        self.actionOpen_File_s.setObjectName("actionOpen_File_s")
        self.actionExit = QtWidgets.QAction(Ecosongs)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(Ecosongs)
        self.actionSave.setObjectName("actionSave")
        self.actionConvert_to_wac = QtWidgets.QAction(Ecosongs)
        self.actionConvert_to_wac.setObjectName("actionConvert_to_wac")
        self.actionChoose_working_folder = QtWidgets.QAction(Ecosongs)
        self.actionChoose_working_folder.setObjectName("actionChoose_working_folder")
        self.actionOpen_database = QtWidgets.QAction(Ecosongs)
        self.actionOpen_database.setObjectName("actionOpen_database")
        self.actionSave_database = QtWidgets.QAction(Ecosongs)
        self.actionSave_database.setObjectName("actionSave_database")
        self.actionExport_database = QtWidgets.QAction(Ecosongs)
        self.actionExport_database.setObjectName("actionExport_database")
        self.menuFile.addAction(self.actionChoose_working_folder)
        self.menuFile.addAction(self.actionOpen_File_s)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_database)
        self.menuFile.addAction(self.actionSave_database)
        self.menuFile.addAction(self.actionExport_database)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionConvert_to_wac)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalyses.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Ecosongs)
        QtCore.QMetaObject.connectSlotsByName(Ecosongs)

    def retranslateUi(self, Ecosongs):
        Ecosongs.setWindowTitle(QtWidgets.QApplication.translate("Ecosongs", "MainWindow", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("Ecosongs", "File", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("Ecosongs", "Help", None, -1))
        self.menuTools.setTitle(QtWidgets.QApplication.translate("Ecosongs", "Tools", None, -1))
        self.menuAnalyses.setTitle(QtWidgets.QApplication.translate("Ecosongs", "Analyses", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("Ecosongs", "About", None, -1))
        self.actionHelp.setText(QtWidgets.QApplication.translate("Ecosongs", "Help", None, -1))
        self.actionOpen_File_s.setText(QtWidgets.QApplication.translate("Ecosongs", "Open File(s)", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("Ecosongs", "Exit", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("Ecosongs", "Save", None, -1))
        self.actionSave.setShortcut(QtWidgets.QApplication.translate("Ecosongs", "Ctrl+S", None, -1))
        self.actionConvert_to_wac.setText(QtWidgets.QApplication.translate("Ecosongs", "Convert WAC files", None, -1))
        self.actionChoose_working_folder.setText(QtWidgets.QApplication.translate("Ecosongs", "Choose working folder", None, -1))
        self.actionOpen_database.setText(QtWidgets.QApplication.translate("Ecosongs", "Load database", None, -1))
        self.actionSave_database.setText(QtWidgets.QApplication.translate("Ecosongs", "Save database", None, -1))
        self.actionExport_database.setText(QtWidgets.QApplication.translate("Ecosongs", "Export database", None, -1))
