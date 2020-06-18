# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_table_options.ui'
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

from gui.widgets.common.table.dataframe_table_view import DataFrameTableView
from gui.widgets.common.file_chooser import FileChooser


class Ui_ImportTableOptions(object):
    def setupUi(self, ImportTableOptions):
        if not ImportTableOptions.objectName():
            ImportTableOptions.setObjectName(u"ImportTableOptions")
        ImportTableOptions.resize(650, 514)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImportTableOptions.sizePolicy().hasHeightForWidth())
        ImportTableOptions.setSizePolicy(sizePolicy)
        ImportTableOptions.setMinimumSize(QSize(650, 450))
        self.gridLayout = QGridLayout(ImportTableOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_status = QLabel(ImportTableOptions)
        self.lbl_status.setObjectName(u"lbl_status")

        self.gridLayout.addWidget(self.lbl_status, 5, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radio_update = QRadioButton(ImportTableOptions)
        self.radiogroup_update = QButtonGroup(ImportTableOptions)
        self.radiogroup_update.setObjectName(u"radiogroup_update")
        self.radiogroup_update.addButton(self.radio_update)
        self.radio_update.setObjectName(u"radio_update")
        self.radio_update.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radio_update)

        self.radio_replace = QRadioButton(ImportTableOptions)
        self.radiogroup_update.addButton(self.radio_replace)
        self.radio_replace.setObjectName(u"radio_replace")

        self.horizontalLayout_2.addWidget(self.radio_replace)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)

        self.label_3 = QLabel(ImportTableOptions)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)

        self.table_loaded = DataFrameTableView(ImportTableOptions)
        self.table_loaded.setObjectName(u"table_loaded")
        self.table_loaded.setSortingEnabled(True)
        self.table_loaded.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.table_loaded, 6, 0, 1, 2)

        self.label = QLabel(ImportTableOptions)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.file_chooser = FileChooser(ImportTableOptions)
        self.file_chooser.setObjectName(u"file_chooser")

        self.gridLayout.addWidget(self.file_chooser, 2, 0, 1, 2)

        self.merged_table = QWidget(ImportTableOptions)
        self.merged_table.setObjectName(u"merged_table")
        self.merged_table.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.merged_table)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.merged_table)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.table_to_import = DataFrameTableView(self.merged_table)
        self.table_to_import.setObjectName(u"table_to_import")
        self.table_to_import.setSortingEnabled(True)
        self.table_to_import.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.table_to_import)


        self.gridLayout.addWidget(self.merged_table, 7, 0, 1, 2)

        self.checkbox_overwrite = QCheckBox(ImportTableOptions)
        self.checkbox_overwrite.setObjectName(u"checkbox_overwrite")

        self.gridLayout.addWidget(self.checkbox_overwrite, 4, 0, 1, 1)


        self.retranslateUi(ImportTableOptions)

        QMetaObject.connectSlotsByName(ImportTableOptions)
    # setupUi

    def retranslateUi(self, ImportTableOptions):
        ImportTableOptions.setWindowTitle(QCoreApplication.translate("ImportTableOptions", u"Form", None))
        self.lbl_status.setText(QCoreApplication.translate("ImportTableOptions", u"This table was loaded:", None))
#if QT_CONFIG(tooltip)
        self.radio_update.setToolTip(QCoreApplication.translate("ImportTableOptions", u"Existing rows will be replaced and missing rows will be added", None))
#endif // QT_CONFIG(tooltip)
        self.radio_update.setText(QCoreApplication.translate("ImportTableOptions", u"Update existing table", None))
#if QT_CONFIG(tooltip)
        self.radio_replace.setToolTip(QCoreApplication.translate("ImportTableOptions", u"The existing table will be replaced", None))
#endif // QT_CONFIG(tooltip)
        self.radio_replace.setText(QCoreApplication.translate("ImportTableOptions", u"Replace existing table", None))
        self.label_3.setText(QCoreApplication.translate("ImportTableOptions", u"Warning: depending on the size of the imported table, this action could require a lot of memory", None))
        self.label.setText(QCoreApplication.translate("ImportTableOptions", u"Importing table: ", None))
        self.label_2.setText(QCoreApplication.translate("ImportTableOptions", u"After merging columns, the following table will be imported:", None))
        self.checkbox_overwrite.setText(QCoreApplication.translate("ImportTableOptions", u"Replace existing entries", None))
    # retranslateUi

