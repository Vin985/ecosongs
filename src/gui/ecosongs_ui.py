# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ecosongs.ui'
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

from gui.widgets.dbmanager.dbexplorer import DBExplorer
from gui.widgets.audio.audiomanager import AudioManager
from gui.widgets.analysis.analysis import Analysis

from  . import ecosongs_rc

class Ui_Ecosongs(object):
    def setupUi(self, Ecosongs):
        if Ecosongs.objectName():
            Ecosongs.setObjectName(u"Ecosongs")
        Ecosongs.resize(1057, 657)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ecosongs.sizePolicy().hasHeightForWidth())
        Ecosongs.setSizePolicy(sizePolicy)
        self.aAbout = QAction(Ecosongs)
        self.aAbout.setObjectName(u"aAbout")
        self.aHelp = QAction(Ecosongs)
        self.aHelp.setObjectName(u"aHelp")
        self.aOpen = QAction(Ecosongs)
        self.aOpen.setObjectName(u"aOpen")
        self.aExit = QAction(Ecosongs)
        self.aExit.setObjectName(u"aExit")
        self.aSave = QAction(Ecosongs)
        self.aSave.setObjectName(u"aSave")
        icon = QIcon()
        icon.addFile(u":/tango/document-save", QSize(), QIcon.Normal, QIcon.Off)
        self.aSave.setIcon(icon)
        self.wac2wav = QAction(Ecosongs)
        self.wac2wav.setObjectName(u"wac2wav")
        self.aSetwd = QAction(Ecosongs)
        self.aSetwd.setObjectName(u"aSetwd")
        icon1 = QIcon()
        icon1.addFile(u":/tango/document-open", QSize(), QIcon.Normal, QIcon.Off)
        self.aSetwd.setIcon(icon1)
        self.aOpen_db = QAction(Ecosongs)
        self.aOpen_db.setObjectName(u"aOpen_db")
        self.aSave_db = QAction(Ecosongs)
        self.aSave_db.setObjectName(u"aSave_db")
        self.aExport_db = QAction(Ecosongs)
        self.aExport_db.setObjectName(u"aExport_db")
        self.action_ACI = QAction(Ecosongs)
        self.action_ACI.setObjectName(u"action_ACI")
        self.action_details = QAction(Ecosongs)
        self.action_details.setObjectName(u"action_details")
        self.action_2wav = QAction(Ecosongs)
        self.action_2wav.setObjectName(u"action_2wav")
        self.aSettings = QAction(Ecosongs)
        self.aSettings.setObjectName(u"aSettings")
        self.aSpecScale = QAction(Ecosongs)
        self.aSpecScale.setObjectName(u"aSpecScale")
        self.aSpecScale.setCheckable(True)
        self.centralwidget = QWidget(Ecosongs)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setAutoFillBackground(True)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(6)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy2)
        self.pages.setAutoFillBackground(False)
        self.pages.setStyleSheet(u"QListView{\n"
"  	show-decoration-selected: 1; \n"
"	outline:none;\n"
"}\n"
"QListView::item {\n"
"	border: 1 outset rgb(136, 138, 133);\n"
"	border-radius: 2;\n"
"	background-color: rgb(238, 238, 236);\n"
"	padding: 5 5 5 5;\n"
"	margin:0 2 2 2;\n"
"	width:75;\n"
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
"	selection-background-color: green;\n"
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
        self.db_page = DBExplorer()
        self.db_page.setObjectName(u"db_page")
        self.db_page.setAutoFillBackground(True)
        self.pages.addWidget(self.db_page)
        self.audio_page = AudioManager()
        self.audio_page.setObjectName(u"audio_page")
        self.pages.addWidget(self.audio_page)
        self.analysis_page = Analysis()
        self.analysis_page.setObjectName(u"analysis_page")
        self.pages.addWidget(self.analysis_page)

        self.horizontalLayout.addWidget(self.pages)

        self.sidebar = QListWidget(self.centralwidget)
        icon2 = QIcon()
        icon2.addFile(u":/tango/db-manager", QSize(), QIcon.Normal, QIcon.Off)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        __qlistwidgetitem = QListWidgetItem(self.sidebar)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setFont(font);
        __qlistwidgetitem.setIcon(icon2);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        icon3 = QIcon()
        icon3.addFile(u":/tango/audio", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.sidebar)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1.setFont(font);
        __qlistwidgetitem1.setIcon(icon3);
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        icon4 = QIcon()
        icon4.addFile(u":/tango/analysis", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.sidebar)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2.setFont(font);
        __qlistwidgetitem2.setIcon(icon4);
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setEnabled(True)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMaximumSize(QSize(93, 16777215))
        self.sidebar.setFont(font)
        self.sidebar.setAutoFillBackground(False)
        self.sidebar.setStyleSheet(u"QListView{\n"
"  	show-decoration-selected: 1; \n"
"	outline:none;\n"
"}\n"
"QListView::item {\n"
"	border: 1 outset rgb(136, 138, 133);\n"
"	border-radius: 2;\n"
"	background-color: rgb(238, 238, 236);\n"
"	padding: 5 5 5 5;\n"
"	margin:0 2 2 2;\n"
"	width:75;\n"
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
"	selection-background-color: green;\n"
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
        self.sidebar.setFrameShape(QFrame.NoFrame)
        self.sidebar.setLineWidth(0)
        self.sidebar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sidebar.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.sidebar.setProperty("showDropIndicator", False)
        self.sidebar.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sidebar.setIconSize(QSize(48, 48))
        self.sidebar.setFlow(QListView.TopToBottom)
        self.sidebar.setViewMode(QListView.IconMode)
        self.sidebar.setWordWrap(True)

        self.horizontalLayout.addWidget(self.sidebar)

        Ecosongs.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Ecosongs)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1057, 21))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_tools = QMenu(self.menubar)
        self.menu_tools.setObjectName(u"menu_tools")
        self.menu_analyses = QMenu(self.menubar)
        self.menu_analyses.setObjectName(u"menu_analyses")
        self.menu_recording = QMenu(self.menubar)
        self.menu_recording.setObjectName(u"menu_recording")
        self.menu_calculate = QMenu(self.menu_recording)
        self.menu_calculate.setObjectName(u"menu_calculate")
        Ecosongs.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Ecosongs)
        self.statusbar.setObjectName(u"statusbar")
        Ecosongs.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(Ecosongs)
        self.toolBar.setObjectName(u"toolBar")
        Ecosongs.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_analyses.menuAction())
        self.menubar.addAction(self.menu_recording.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
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
        self.menu_recording.addAction(self.menu_calculate.menuAction())
        self.menu_recording.addSeparator()
        self.menu_recording.addAction(self.action_2wav)
        self.menu_recording.addAction(self.action_details)
        self.menu_calculate.addAction(self.action_ACI)
        self.toolBar.addAction(self.aSetwd)
        self.toolBar.addAction(self.aSave)
        self.toolBar.addAction(self.aSpecScale)

        self.retranslateUi(Ecosongs)

        self.pages.setCurrentIndex(1)
        self.sidebar.setCurrentRow(1)


        QMetaObject.connectSlotsByName(Ecosongs)
    # setupUi

    def retranslateUi(self, Ecosongs):
        Ecosongs.setWindowTitle(QCoreApplication.translate("Ecosongs", u"MainWindow", None))
        self.aAbout.setText(QCoreApplication.translate("Ecosongs", u"About", None))
        self.aHelp.setText(QCoreApplication.translate("Ecosongs", u"Help", None))
        self.aOpen.setText(QCoreApplication.translate("Ecosongs", u"Open File(s)", None))
        self.aExit.setText(QCoreApplication.translate("Ecosongs", u"Exit", None))
        self.aSave.setText(QCoreApplication.translate("Ecosongs", u"Save", None))
#if QT_CONFIG(shortcut)
        self.aSave.setShortcut(QCoreApplication.translate("Ecosongs", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.wac2wav.setText(QCoreApplication.translate("Ecosongs", u"Convert WAC files", None))
        self.aSetwd.setText(QCoreApplication.translate("Ecosongs", u"Choose working folder", None))
        self.aOpen_db.setText(QCoreApplication.translate("Ecosongs", u"Load database", None))
        self.aSave_db.setText(QCoreApplication.translate("Ecosongs", u"Save database", None))
        self.aExport_db.setText(QCoreApplication.translate("Ecosongs", u"Export database", None))
        self.action_ACI.setText(QCoreApplication.translate("Ecosongs", u"Acoustic Complexity Index (ACI)", None))
        self.action_details.setText(QCoreApplication.translate("Ecosongs", u"Show Details", None))
        self.action_2wav.setText(QCoreApplication.translate("Ecosongs", u"Convert to wav", None))
        self.aSettings.setText(QCoreApplication.translate("Ecosongs", u"Settings", None))
        self.aSpecScale.setText(QCoreApplication.translate("Ecosongs", u"Select spectrogram scale", None))

        __sortingEnabled = self.sidebar.isSortingEnabled()
        self.sidebar.setSortingEnabled(False)
        ___qlistwidgetitem = self.sidebar.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Ecosongs", u"Database Manager", None));
        ___qlistwidgetitem1 = self.sidebar.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Ecosongs", u"Audio", None));
        ___qlistwidgetitem2 = self.sidebar.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Ecosongs", u"Analysis", None));
        self.sidebar.setSortingEnabled(__sortingEnabled)

        self.menu_file.setTitle(QCoreApplication.translate("Ecosongs", u"File", None))
        self.menu_help.setTitle(QCoreApplication.translate("Ecosongs", u"Help", None))
        self.menu_tools.setTitle(QCoreApplication.translate("Ecosongs", u"Tools", None))
        self.menu_analyses.setTitle(QCoreApplication.translate("Ecosongs", u"Analyses", None))
        self.menu_recording.setTitle(QCoreApplication.translate("Ecosongs", u"Recording", None))
        self.menu_calculate.setTitle(QCoreApplication.translate("Ecosongs", u"Calculate...", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("Ecosongs", u"toolBar", None))
    # retranslateUi

