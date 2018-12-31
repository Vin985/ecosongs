# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ecosongs.ui',
# licensing of 'ecosongs.ui' applies.
#
# Created: Mon Dec 31 14:53:44 2018
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Ecosongs(object):
    def setupUi(self, Ecosongs):
        Ecosongs.setObjectName("Ecosongs")
        Ecosongs.resize(1057, 657)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ecosongs.sizePolicy().hasHeightForWidth())
        Ecosongs.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Ecosongs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pages = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy)
        self.pages.setAutoFillBackground(False)
        self.pages.setStyleSheet("QListView{\n"
"      show-decoration-selected: 1; \n"
"    outline:none;\n"
"}\n"
"QListView::item {\n"
"    border: 1 outset rgb(136, 138, 133);\n"
"    border-radius: 2;\n"
"    background-color: rgb(238, 238, 236);\n"
"    padding: 5 5 5 5;\n"
"    margin:0 2 2 2;\n"
"    width:75;\n"
"/*background-color:blue;*/\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"    selection-background-color: green;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}\n"
"\n"
"QListView::text:selected {\n"
"    border:none;\n"
"}")
        self.pages.setObjectName("pages")
        self.db_page = DBExplorer()
        self.db_page.setAutoFillBackground(True)
        self.db_page.setObjectName("db_page")
        self.pages.addWidget(self.db_page)
        self.audio_page = AudioManager()
        self.audio_page.setObjectName("audio_page")
        self.pages.addWidget(self.audio_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pages.addWidget(self.page)
        self.horizontalLayout.addWidget(self.pages)
        self.sidebar = QtWidgets.QListWidget(self.centralwidget)
        self.sidebar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMaximumSize(QtCore.QSize(93, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.sidebar.setFont(font)
        self.sidebar.setAutoFillBackground(False)
        self.sidebar.setStyleSheet("QListView{\n"
"      show-decoration-selected: 1; \n"
"    outline:none;\n"
"}\n"
"QListView::item {\n"
"    border: 1 outset rgb(136, 138, 133);\n"
"    border-radius: 2;\n"
"    background-color: rgb(238, 238, 236);\n"
"    padding: 5 5 5 5;\n"
"    margin:0 2 2 2;\n"
"    width:75;\n"
"/*background-color:blue;*/\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"    selection-background-color: green;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}\n"
"\n"
"QListView::text:selected {\n"
"    border:none;\n"
"}")
        self.sidebar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sidebar.setLineWidth(0)
        self.sidebar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sidebar.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.sidebar.setProperty("showDropIndicator", False)
        self.sidebar.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sidebar.setIconSize(QtCore.QSize(48, 48))
        self.sidebar.setFlow(QtWidgets.QListView.TopToBottom)
        self.sidebar.setViewMode(QtWidgets.QListView.IconMode)
        self.sidebar.setWordWrap(True)
        self.sidebar.setObjectName("sidebar")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tango/db-manager"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtWidgets.QListWidgetItem(self.sidebar)
        item.setIcon(icon)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tango/audio"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtWidgets.QListWidgetItem(self.sidebar)
        item.setIcon(icon1)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tango/analysis"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtWidgets.QListWidgetItem(self.sidebar)
        item.setIcon(icon2)
        self.horizontalLayout.addWidget(self.sidebar)
        Ecosongs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ecosongs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1057, 23))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_tools = QtWidgets.QMenu(self.menubar)
        self.menu_tools.setObjectName("menu_tools")
        self.menu_analyses = QtWidgets.QMenu(self.menubar)
        self.menu_analyses.setObjectName("menu_analyses")
        self.menu_recording = QtWidgets.QMenu(self.menubar)
        self.menu_recording.setObjectName("menu_recording")
        self.menu_calculate = QtWidgets.QMenu(self.menu_recording)
        self.menu_calculate.setObjectName("menu_calculate")
        Ecosongs.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ecosongs)
        self.statusbar.setObjectName("statusbar")
        Ecosongs.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Ecosongs)
        self.toolBar.setObjectName("toolBar")
        Ecosongs.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.aAbout = QtWidgets.QAction(Ecosongs)
        self.aAbout.setObjectName("aAbout")
        self.aHelp = QtWidgets.QAction(Ecosongs)
        self.aHelp.setObjectName("aHelp")
        self.aOpen = QtWidgets.QAction(Ecosongs)
        self.aOpen.setObjectName("aOpen")
        self.aExit = QtWidgets.QAction(Ecosongs)
        self.aExit.setObjectName("aExit")
        self.aSave = QtWidgets.QAction(Ecosongs)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/tango/document-save"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aSave.setIcon(icon3)
        self.aSave.setObjectName("aSave")
        self.wac2wav = QtWidgets.QAction(Ecosongs)
        self.wac2wav.setObjectName("wac2wav")
        self.aSetwd = QtWidgets.QAction(Ecosongs)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/tango/document-open"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aSetwd.setIcon(icon4)
        self.aSetwd.setObjectName("aSetwd")
        self.aOpen_db = QtWidgets.QAction(Ecosongs)
        self.aOpen_db.setObjectName("aOpen_db")
        self.aSave_db = QtWidgets.QAction(Ecosongs)
        self.aSave_db.setObjectName("aSave_db")
        self.aExport_db = QtWidgets.QAction(Ecosongs)
        self.aExport_db.setObjectName("aExport_db")
        self.action_ACI = QtWidgets.QAction(Ecosongs)
        self.action_ACI.setObjectName("action_ACI")
        self.action_details = QtWidgets.QAction(Ecosongs)
        self.action_details.setObjectName("action_details")
        self.action_2wav = QtWidgets.QAction(Ecosongs)
        self.action_2wav.setObjectName("action_2wav")
        self.aSettings = QtWidgets.QAction(Ecosongs)
        self.aSettings.setObjectName("aSettings")
        self.aSpecScale = QtWidgets.QAction(Ecosongs)
        self.aSpecScale.setCheckable(True)
        self.aSpecScale.setObjectName("aSpecScale")
        self.menu_file.addAction(self.aSetwd)
        self.menu_file.addAction(self.aOpen)
        self.menu_file.addAction(self.aSave)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.aOpen_db)
        self.menu_file.addAction(self.aSave_db)
        self.menu_file.addAction(self.aExport_db)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.aExit)
        self.menu_help.addAction(self.aHelp)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.aAbout)
        self.menu_tools.addAction(self.wac2wav)
        self.menu_tools.addAction(self.aSettings)
        self.menu_calculate.addAction(self.action_ACI)
        self.menu_recording.addAction(self.menu_calculate.menuAction())
        self.menu_recording.addSeparator()
        self.menu_recording.addAction(self.action_2wav)
        self.menu_recording.addAction(self.action_details)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_analyses.menuAction())
        self.menubar.addAction(self.menu_recording.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.toolBar.addAction(self.aSetwd)
        self.toolBar.addAction(self.aSave)
        self.toolBar.addAction(self.aSpecScale)

        self.retranslateUi(Ecosongs)
        self.pages.setCurrentIndex(1)
        self.sidebar.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Ecosongs)

    def retranslateUi(self, Ecosongs):
        Ecosongs.setWindowTitle(QtWidgets.QApplication.translate("Ecosongs", "MainWindow", None, -1))
        __sortingEnabled = self.sidebar.isSortingEnabled()
        self.sidebar.setSortingEnabled(False)
        self.sidebar.item(0).setText(QtWidgets.QApplication.translate("Ecosongs", "Database Manager", None, -1))
        self.sidebar.item(1).setText(QtWidgets.QApplication.translate("Ecosongs", "Audio", None, -1))
        self.sidebar.item(2).setText(QtWidgets.QApplication.translate("Ecosongs", "Analysis", None, -1))
        self.sidebar.setSortingEnabled(__sortingEnabled)
        self.menu_file.setTitle(QtWidgets.QApplication.translate("Ecosongs", "File", None, -1))
        self.menu_help.setTitle(QtWidgets.QApplication.translate("Ecosongs", "Help", None, -1))
        self.menu_tools.setTitle(QtWidgets.QApplication.translate("Ecosongs", "Tools", None, -1))
        self.menu_analyses.setTitle(QtWidgets.QApplication.translate("Ecosongs", "Analyses", None, -1))
        self.menu_recording.setTitle(QtWidgets.QApplication.translate("Ecosongs", "Recording", None, -1))
        self.menu_calculate.setTitle(QtWidgets.QApplication.translate("Ecosongs", "Calculate...", None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("Ecosongs", "toolBar", None, -1))
        self.aAbout.setText(QtWidgets.QApplication.translate("Ecosongs", "About", None, -1))
        self.aHelp.setText(QtWidgets.QApplication.translate("Ecosongs", "Help", None, -1))
        self.aOpen.setText(QtWidgets.QApplication.translate("Ecosongs", "Open File(s)", None, -1))
        self.aExit.setText(QtWidgets.QApplication.translate("Ecosongs", "Exit", None, -1))
        self.aSave.setText(QtWidgets.QApplication.translate("Ecosongs", "Save", None, -1))
        self.aSave.setShortcut(QtWidgets.QApplication.translate("Ecosongs", "Ctrl+S", None, -1))
        self.wac2wav.setText(QtWidgets.QApplication.translate("Ecosongs", "Convert WAC files", None, -1))
        self.aSetwd.setText(QtWidgets.QApplication.translate("Ecosongs", "Choose working folder", None, -1))
        self.aOpen_db.setText(QtWidgets.QApplication.translate("Ecosongs", "Load database", None, -1))
        self.aSave_db.setText(QtWidgets.QApplication.translate("Ecosongs", "Save database", None, -1))
        self.aExport_db.setText(QtWidgets.QApplication.translate("Ecosongs", "Export database", None, -1))
        self.action_ACI.setText(QtWidgets.QApplication.translate("Ecosongs", "Acoustic Complexity Index (ACI)", None, -1))
        self.action_details.setText(QtWidgets.QApplication.translate("Ecosongs", "Show Details", None, -1))
        self.action_2wav.setText(QtWidgets.QApplication.translate("Ecosongs", "Convert to wav", None, -1))
        self.aSettings.setText(QtWidgets.QApplication.translate("Ecosongs", "Settings", None, -1))
        self.aSpecScale.setText(QtWidgets.QApplication.translate("Ecosongs", "Select spectrogram scale", None, -1))

from gui.widgets.audio.audiomanager import AudioManager
from gui.widgets.dbmanager.dbexplorer import DBExplorer
from . import ecosongs_rc
