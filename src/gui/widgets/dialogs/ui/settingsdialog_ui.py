# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsdialog.ui',
# licensing of 'settingsdialog.ui' applies.
#
# Created: Wed Jan  2 14:34:46 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(776, 703)
        self.gridLayout = QtWidgets.QGridLayout(SettingsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(SettingsDialog)
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
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.menu_categories = QtWidgets.QListWidget(SettingsDialog)
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

        self.retranslateUi(SettingsDialog)
        self.menu_pages.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtWidgets.QApplication.translate("SettingsDialog", "Dialog", None, -1))
        __sortingEnabled = self.menu_categories.isSortingEnabled()
        self.menu_categories.setSortingEnabled(False)
        self.menu_categories.item(0).setText(QtWidgets.QApplication.translate("SettingsDialog", "General", None, -1))
        self.menu_categories.item(1).setText(QtWidgets.QApplication.translate("SettingsDialog", "Spectrogram", None, -1))
        self.menu_categories.item(2).setText(QtWidgets.QApplication.translate("SettingsDialog", "Indexes", None, -1))
        self.menu_categories.setSortingEnabled(__sortingEnabled)

from gui.widgets.menus.spectrogramsettings import SpectrogramSettings
