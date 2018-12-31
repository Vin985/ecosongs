# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsmenu.ui',
# licensing of 'settingsmenu.ui' applies.
#
# Created: Mon Dec 31 15:38:31 2018
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SettingsMenu(object):
    def setupUi(self, SettingsMenu):
        SettingsMenu.setObjectName("SettingsMenu")
        SettingsMenu.resize(776, 703)
        self.gridLayout = QtWidgets.QGridLayout(SettingsMenu)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(SettingsMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu_pages = QtWidgets.QStackedWidget(self.widget)
        self.menu_pages.setObjectName("menu_pages")
        self.general_settings = QtWidgets.QWidget()
        self.general_settings.setObjectName("general_settings")
        self.menu_pages.addWidget(self.general_settings)
        self.spectro_settings = SpectrogramSettings()
        self.spectro_settings.setObjectName("spectro_settings")
        self.menu_pages.addWidget(self.spectro_settings)
        self.index_settings = QtWidgets.QWidget()
        self.index_settings.setObjectName("index_settings")
        self.menu_pages.addWidget(self.index_settings)
        self.verticalLayout.addWidget(self.menu_pages)
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsMenu)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.menu_categories = QtWidgets.QListWidget(SettingsMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_categories.sizePolicy().hasHeightForWidth())
        self.menu_categories.setSizePolicy(sizePolicy)
        self.menu_categories.setObjectName("menu_categories")
        QtWidgets.QListWidgetItem(self.menu_categories)
        QtWidgets.QListWidgetItem(self.menu_categories)
        QtWidgets.QListWidgetItem(self.menu_categories)
        self.gridLayout.addWidget(self.menu_categories, 0, 0, 1, 1)

        self.retranslateUi(SettingsMenu)
        self.menu_pages.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsMenu.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SettingsMenu.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsMenu)

    def retranslateUi(self, SettingsMenu):
        SettingsMenu.setWindowTitle(QtWidgets.QApplication.translate("SettingsMenu", "Dialog", None, -1))
        __sortingEnabled = self.menu_categories.isSortingEnabled()
        self.menu_categories.setSortingEnabled(False)
        self.menu_categories.item(0).setText(QtWidgets.QApplication.translate("SettingsMenu", "General", None, -1))
        self.menu_categories.item(1).setText(QtWidgets.QApplication.translate("SettingsMenu", "Spectrogram", None, -1))
        self.menu_categories.item(2).setText(QtWidgets.QApplication.translate("SettingsMenu", "Indexes", None, -1))
        self.menu_categories.setSortingEnabled(__sortingEnabled)

from gui.widgets.menus.spectrogramsettings import SpectrogramSettings
