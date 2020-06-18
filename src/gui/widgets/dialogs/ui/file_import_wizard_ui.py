# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_import_wizard.ui'
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


class Ui_FileImportWizard(object):
    def setupUi(self, FileImportWizard):
        if not FileImportWizard.objectName():
            FileImportWizard.setObjectName(u"FileImportWizard")
        FileImportWizard.setEnabled(True)
        FileImportWizard.resize(896, 665)
        self.page1 = QWizardPage()
        self.page1.setObjectName(u"page1")
        self.layoutWidget = QWidget(self.page1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 870, 461))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 11, 0, 1, 4)

        self.radio_site_auto = QRadioButton(self.layoutWidget)
        self.radio_site_info = QButtonGroup(FileImportWizard)
        self.radio_site_info.setObjectName(u"radio_site_info")
        self.radio_site_info.addButton(self.radio_site_auto)
        self.radio_site_auto.setObjectName(u"radio_site_auto")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_site_auto.sizePolicy().hasHeightForWidth())
        self.radio_site_auto.setSizePolicy(sizePolicy)
        self.radio_site_auto.setChecked(True)

        self.gridLayout.addWidget(self.radio_site_auto, 5, 0, 1, 4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.radio_rec_auto = QRadioButton(self.layoutWidget)
        self.radio_recorders = QButtonGroup(FileImportWizard)
        self.radio_recorders.setObjectName(u"radio_recorders")
        self.radio_recorders.addButton(self.radio_rec_auto)
        self.radio_rec_auto.setObjectName(u"radio_rec_auto")
        self.radio_rec_auto.setEnabled(True)
        sizePolicy.setHeightForWidth(self.radio_rec_auto.sizePolicy().hasHeightForWidth())
        self.radio_rec_auto.setSizePolicy(sizePolicy)
        self.radio_rec_auto.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radio_rec_auto)

        self.radio_rec_sm = QRadioButton(self.layoutWidget)
        self.radio_recorders.addButton(self.radio_rec_sm)
        self.radio_rec_sm.setObjectName(u"radio_rec_sm")
        sizePolicy.setHeightForWidth(self.radio_rec_sm.sizePolicy().hasHeightForWidth())
        self.radio_rec_sm.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.radio_rec_sm)

        self.radio_rec_am = QRadioButton(self.layoutWidget)
        self.radio_recorders.addButton(self.radio_rec_am)
        self.radio_rec_am.setObjectName(u"radio_rec_am")
        sizePolicy.setHeightForWidth(self.radio_rec_am.sizePolicy().hasHeightForWidth())
        self.radio_rec_am.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.radio_rec_am)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 4)

        self.checkbox_save_info = QCheckBox(self.layoutWidget)
        self.checkbox_save_info.setObjectName(u"checkbox_save_info")
        self.checkbox_save_info.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_save_info, 9, 0, 1, 4)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 3)

        self.input_src_path = QLineEdit(self.layoutWidget)
        self.input_src_path.setObjectName(u"input_src_path")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.input_src_path.sizePolicy().hasHeightForWidth())
        self.input_src_path.setSizePolicy(sizePolicy3)
        self.input_src_path.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.input_src_path, 1, 0, 1, 3)

        self.radio_folder = QRadioButton(self.layoutWidget)
        self.radio_is_folder = QButtonGroup(FileImportWizard)
        self.radio_is_folder.setObjectName(u"radio_is_folder")
        self.radio_is_folder.addButton(self.radio_folder)
        self.radio_folder.setObjectName(u"radio_folder")
        sizePolicy.setHeightForWidth(self.radio_folder.sizePolicy().hasHeightForWidth())
        self.radio_folder.setSizePolicy(sizePolicy)
        self.radio_folder.setChecked(True)

        self.gridLayout.addWidget(self.radio_folder, 0, 0, 1, 1)

        self.checkbox_subfolders = QCheckBox(self.layoutWidget)
        self.checkbox_subfolders.setObjectName(u"checkbox_subfolders")
        sizePolicy3.setHeightForWidth(self.checkbox_subfolders.sizePolicy().hasHeightForWidth())
        self.checkbox_subfolders.setSizePolicy(sizePolicy3)
        self.checkbox_subfolders.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_subfolders, 0, 2, 1, 2)

        self.site_manual = QWidget(self.layoutWidget)
        self.site_manual.setObjectName(u"site_manual")
        sizePolicy2.setHeightForWidth(self.site_manual.sizePolicy().hasHeightForWidth())
        self.site_manual.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.site_manual)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.site_manual)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_8)

        self.input_year = QLineEdit(self.site_manual)
        self.input_year.setObjectName(u"input_year")
        sizePolicy3.setHeightForWidth(self.input_year.sizePolicy().hasHeightForWidth())
        self.input_year.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.input_year)

        self.label = QLabel(self.site_manual)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.input_site = QLineEdit(self.site_manual)
        self.input_site.setObjectName(u"input_site")
        sizePolicy3.setHeightForWidth(self.input_site.sizePolicy().hasHeightForWidth())
        self.input_site.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.input_site)

        self.label_4 = QLabel(self.site_manual)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_4)

        self.input_plot = QLineEdit(self.site_manual)
        self.input_plot.setObjectName(u"input_plot")
        sizePolicy3.setHeightForWidth(self.input_plot.sizePolicy().hasHeightForWidth())
        self.input_plot.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.input_plot)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.site_manual, 8, 0, 1, 4)

        self.site_auto = QWidget(self.layoutWidget)
        self.site_auto.setObjectName(u"site_auto")
        sizePolicy2.setHeightForWidth(self.site_auto.sizePolicy().hasHeightForWidth())
        self.site_auto.setSizePolicy(sizePolicy2)
        self.gridLayout_2 = QGridLayout(self.site_auto)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.label_2 = QLabel(self.site_auto)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_5 = QLabel(self.site_auto)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.combo_idx_3 = QComboBox(self.site_auto)
        self.combo_idx_3.addItem("")
        self.combo_idx_3.addItem("")
        self.combo_idx_3.addItem("")
        self.combo_idx_3.setObjectName(u"combo_idx_3")
        sizePolicy.setHeightForWidth(self.combo_idx_3.sizePolicy().hasHeightForWidth())
        self.combo_idx_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.combo_idx_3)

        self.label_7 = QLabel(self.site_auto)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.combo_idx_2 = QComboBox(self.site_auto)
        self.combo_idx_2.addItem("")
        self.combo_idx_2.addItem("")
        self.combo_idx_2.addItem("")
        self.combo_idx_2.setObjectName(u"combo_idx_2")
        sizePolicy.setHeightForWidth(self.combo_idx_2.sizePolicy().hasHeightForWidth())
        self.combo_idx_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.combo_idx_2)

        self.label_6 = QLabel(self.site_auto)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.combo_idx_1 = QComboBox(self.site_auto)
        self.combo_idx_1.addItem("")
        self.combo_idx_1.addItem("")
        self.combo_idx_1.addItem("")
        self.combo_idx_1.setObjectName(u"combo_idx_1")
        sizePolicy.setHeightForWidth(self.combo_idx_1.sizePolicy().hasHeightForWidth())
        self.combo_idx_1.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.combo_idx_1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.site_auto, 7, 0, 1, 4)

        self.radio_site_manual = QRadioButton(self.layoutWidget)
        self.radio_site_info.addButton(self.radio_site_manual)
        self.radio_site_manual.setObjectName(u"radio_site_manual")
        self.radio_site_manual.setEnabled(False)

        self.gridLayout.addWidget(self.radio_site_manual, 6, 0, 1, 4)

        self.radio_file = QRadioButton(self.layoutWidget)
        self.radio_is_folder.addButton(self.radio_file)
        self.radio_file.setObjectName(u"radio_file")
        sizePolicy3.setHeightForWidth(self.radio_file.sizePolicy().hasHeightForWidth())
        self.radio_file.setSizePolicy(sizePolicy3)
        self.radio_file.setMinimumSize(QSize(0, 0))
        self.radio_file.setChecked(False)

        self.gridLayout.addWidget(self.radio_file, 0, 1, 1, 1)

        self.checkbox_load_info = QCheckBox(self.layoutWidget)
        self.checkbox_load_info.setObjectName(u"checkbox_load_info")
        self.checkbox_load_info.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_load_info, 10, 0, 1, 4)

        self.btn_browse_src = QPushButton(self.layoutWidget)
        self.btn_browse_src.setObjectName(u"btn_browse_src")
        sizePolicy.setHeightForWidth(self.btn_browse_src.sizePolicy().hasHeightForWidth())
        self.btn_browse_src.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_browse_src, 1, 3, 1, 1)

        FileImportWizard.addPage(self.page1)
        self.page2 = QWizardPage()
        self.page2.setObjectName(u"page2")
        self.gridLayoutWidget = QWidget(self.page2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 861, 501))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_status = QLabel(self.gridLayoutWidget)
        self.lbl_status.setObjectName(u"lbl_status")
        sizePolicy3.setHeightForWidth(self.lbl_status.sizePolicy().hasHeightForWidth())
        self.lbl_status.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.lbl_status, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.table_files = DataFrameTableView(self.gridLayoutWidget)
        self.table_files.setObjectName(u"table_files")
        self.table_files.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_files.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.table_files.setSortingEnabled(True)
        self.table_files.horizontalHeader().setStretchLastSection(True)
        self.table_files.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.table_files, 3, 0, 1, 1)

        FileImportWizard.addPage(self.page2)
        self.page3 = QWizardPage()
        self.page3.setObjectName(u"page3")
        self.gridLayoutWidget_2 = QWidget(self.page3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 861, 543))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 1, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 8, 0, 1, 2)

        self.checkbox_rename = QCheckBox(self.gridLayoutWidget_2)
        self.checkbox_rename.setObjectName(u"checkbox_rename")
        self.checkbox_rename.setChecked(True)

        self.gridLayout_4.addWidget(self.checkbox_rename, 3, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 2)

        self.move_options = QWidget(self.gridLayoutWidget_2)
        self.move_options.setObjectName(u"move_options")
        self.gridLayout_7 = QGridLayout(self.move_options)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.radio_new_folder = QRadioButton(self.move_options)
        self.radio_destination = QButtonGroup(FileImportWizard)
        self.radio_destination.setObjectName(u"radio_destination")
        self.radio_destination.addButton(self.radio_new_folder)
        self.radio_new_folder.setObjectName(u"radio_new_folder")
        self.radio_new_folder.setChecked(True)

        self.gridLayout_7.addWidget(self.radio_new_folder, 1, 0, 1, 1)

        self.radio_data_source = QRadioButton(self.move_options)
        self.radio_destination.addButton(self.radio_data_source)
        self.radio_data_source.setObjectName(u"radio_data_source")
        self.radio_data_source.setEnabled(False)
        self.radio_data_source.setChecked(False)

        self.gridLayout_7.addWidget(self.radio_data_source, 4, 0, 1, 1)

        self.combo_datasource = QComboBox(self.move_options)
        self.combo_datasource.setObjectName(u"combo_datasource")
        self.combo_datasource.setEnabled(False)

        self.gridLayout_7.addWidget(self.combo_datasource, 5, 0, 1, 4)

        self.label_12 = QLabel(self.move_options)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)

        self.checkbox_overwrite = QCheckBox(self.move_options)
        self.checkbox_overwrite.setObjectName(u"checkbox_overwrite")
        self.checkbox_overwrite.setChecked(True)

        self.gridLayout_7.addWidget(self.checkbox_overwrite, 6, 0, 1, 1)

        self.btn_browse_dest = QPushButton(self.move_options)
        self.btn_browse_dest.setObjectName(u"btn_browse_dest")
        sizePolicy.setHeightForWidth(self.btn_browse_dest.sizePolicy().hasHeightForWidth())
        self.btn_browse_dest.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.btn_browse_dest, 2, 3, 1, 1)

        self.input_dest_path = QLineEdit(self.move_options)
        self.input_dest_path.setObjectName(u"input_dest_path")

        self.gridLayout_7.addWidget(self.input_dest_path, 2, 0, 1, 3)

        self.label_14 = QLabel(self.move_options)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy5)

        self.gridLayout_7.addWidget(self.label_14, 3, 1, 1, 1)

        self.input_datasource = QLineEdit(self.move_options)
        self.input_datasource.setObjectName(u"input_datasource")
        self.input_datasource.setEnabled(False)

        self.gridLayout_7.addWidget(self.input_datasource, 3, 2, 1, 1)

        self.checkbox_new_datasource = QCheckBox(self.move_options)
        self.checkbox_new_datasource.setObjectName(u"checkbox_new_datasource")
        self.checkbox_new_datasource.setEnabled(False)
        sizePolicy.setHeightForWidth(self.checkbox_new_datasource.sizePolicy().hasHeightForWidth())
        self.checkbox_new_datasource.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.checkbox_new_datasource, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.move_options, 6, 0, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 3, 1, 1, 1)

        self.checkbox_move = QCheckBox(self.gridLayoutWidget_2)
        self.checkbox_move.setObjectName(u"checkbox_move")
        self.checkbox_move.setChecked(False)

        self.gridLayout_4.addWidget(self.checkbox_move, 5, 0, 1, 1)

        self.checkbox_link = QCheckBox(self.gridLayoutWidget_2)
        self.checkbox_link.setObjectName(u"checkbox_link")
        self.checkbox_link.setChecked(True)

        self.gridLayout_4.addWidget(self.checkbox_link, 4, 0, 1, 1)

        self.compression_options = QGroupBox(self.gridLayoutWidget_2)
        self.compression_options.setObjectName(u"compression_options")
        self.compression_options.setEnabled(True)
        self.gridLayout_5 = QGridLayout(self.compression_options)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.radio_zip = QRadioButton(self.compression_options)
        self.radio_compression = QButtonGroup(FileImportWizard)
        self.radio_compression.setObjectName(u"radio_compression")
        self.radio_compression.addButton(self.radio_zip)
        self.radio_zip.setObjectName(u"radio_zip")

        self.gridLayout_5.addWidget(self.radio_zip, 2, 2, 1, 1)

        self.radio_7z = QRadioButton(self.compression_options)
        self.radio_compression.addButton(self.radio_7z)
        self.radio_7z.setObjectName(u"radio_7z")
        self.radio_7z.setChecked(True)

        self.gridLayout_5.addWidget(self.radio_7z, 2, 1, 1, 1)

        self.label_10 = QLabel(self.compression_options)
        self.label_10.setObjectName(u"label_10")
        sizePolicy5.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy5)

        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)

        self.radio_tar = QRadioButton(self.compression_options)
        self.radio_compression.addButton(self.radio_tar)
        self.radio_tar.setObjectName(u"radio_tar")

        self.gridLayout_5.addWidget(self.radio_tar, 2, 3, 1, 1)

        self.checkbox_archive = QCheckBox(self.compression_options)
        self.checkbox_archive.setObjectName(u"checkbox_archive")

        self.gridLayout_5.addWidget(self.checkbox_archive, 1, 0, 1, 1)

        self.checkbox_flac = QCheckBox(self.compression_options)
        self.checkbox_flac.setObjectName(u"checkbox_flac")

        self.gridLayout_5.addWidget(self.checkbox_flac, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.compression_options, 7, 0, 1, 2)

        self.checkbox_reimport = QCheckBox(self.gridLayoutWidget_2)
        self.checkbox_reimport.setObjectName(u"checkbox_reimport")

        self.gridLayout_4.addWidget(self.checkbox_reimport, 2, 0, 1, 1)

        FileImportWizard.addPage(self.page3)
        self.page4 = QWizardPage()
        self.page4.setObjectName(u"page4")
        self.gridLayoutWidget_3 = QWidget(self.page4)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(9, -1, 851, 531))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_8.addWidget(self.label_13, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.details_console = QTextEdit(self.gridLayoutWidget_3)
        self.details_console.setObjectName(u"details_console")

        self.gridLayout_8.addWidget(self.details_console, 2, 0, 1, 1)

        FileImportWizard.addPage(self.page4)
        self.page5 = QWizardPage()
        self.page5.setObjectName(u"page5")
        self.gridLayoutWidget_4 = QWidget(self.page5)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 861, 521))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_removing = QLabel(self.gridLayoutWidget_4)
        self.lbl_removing.setObjectName(u"lbl_removing")
        self.lbl_removing.setEnabled(False)
        self.lbl_removing.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.lbl_removing, 1, 1, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.checkbox_done = QCheckBox(self.gridLayoutWidget_4)
        self.checkbox_done.setObjectName(u"checkbox_done")

        self.gridLayout_6.addWidget(self.checkbox_done, 8, 1, 1, 1)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_6.addItem(self.spacer, 7, 1, 1, 2)

        self.lbl_renaming = QLabel(self.gridLayoutWidget_4)
        self.lbl_renaming.setObjectName(u"lbl_renaming")
        self.lbl_renaming.setEnabled(False)

        self.gridLayout_6.addWidget(self.lbl_renaming, 2, 1, 1, 2)

        self.lbl_converting = QLabel(self.gridLayoutWidget_4)
        self.lbl_converting.setObjectName(u"lbl_converting")
        self.lbl_converting.setLayoutDirection(Qt.LeftToRight)
        self.lbl_converting.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.lbl_converting, 0, 1, 1, 2)

        self.progress_bar = QProgressBar(self.gridLayoutWidget_4)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.gridLayout_6.addWidget(self.progress_bar, 5, 1, 1, 2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_8, 4, 1, 1, 2)

        self.log_console = QTextEdit(self.gridLayoutWidget_4)
        self.log_console.setObjectName(u"log_console")

        self.gridLayout_6.addWidget(self.log_console, 6, 1, 1, 1)

        self.lbl_saving = QLabel(self.gridLayoutWidget_4)
        self.lbl_saving.setObjectName(u"lbl_saving")
        self.lbl_saving.setEnabled(False)

        self.gridLayout_6.addWidget(self.lbl_saving, 3, 1, 1, 1)

        FileImportWizard.addPage(self.page5)

        self.retranslateUi(FileImportWizard)

        self.combo_idx_2.setCurrentIndex(1)
        self.combo_idx_1.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(FileImportWizard)
    # setupUi

    def retranslateUi(self, FileImportWizard):
        FileImportWizard.setWindowTitle(QCoreApplication.translate("FileImportWizard", u"File import wizard", None))
        self.page1.setTitle(QCoreApplication.translate("FileImportWizard", u"Import files in the database", None))
        self.page1.setSubTitle(QCoreApplication.translate("FileImportWizard", u"Please select the files you want to import.", None))
        self.radio_site_auto.setText(QCoreApplication.translate("FileImportWizard", u"Automatically detect information from folder hierarchy. The 3 folders above the audio files will be used to extract the information", None))
        self.label_3.setText(QCoreApplication.translate("FileImportWizard", u"File type:", None))
        self.radio_rec_auto.setText(QCoreApplication.translate("FileImportWizard", u"Auto-detect", None))
        self.radio_rec_sm.setText(QCoreApplication.translate("FileImportWizard", u"SongMeter", None))
        self.radio_rec_am.setText(QCoreApplication.translate("FileImportWizard", u"Audiomoth", None))
        self.checkbox_save_info.setText(QCoreApplication.translate("FileImportWizard", u"Generate information file when parsing directories to allow for fast loading of directories", None))
        self.label_9.setText(QCoreApplication.translate("FileImportWizard", u"Each file requires information about site, year and plot:", None))
        self.radio_folder.setText(QCoreApplication.translate("FileImportWizard", u"Import a folder", None))
        self.checkbox_subfolders.setText(QCoreApplication.translate("FileImportWizard", u"Include subfolders", None))
        self.label_8.setText(QCoreApplication.translate("FileImportWizard", u"Year", None))
        self.label.setText(QCoreApplication.translate("FileImportWizard", u"Site", None))
        self.label_4.setText(QCoreApplication.translate("FileImportWizard", u"Plot", None))
        self.label_2.setText(QCoreApplication.translate("FileImportWizard", u"Define the order in which the information is stocked on the hard drive starting with the topmost folder:", None))
        self.label_5.setText(QCoreApplication.translate("FileImportWizard", u"Top folder", None))
        self.combo_idx_3.setItemText(0, QCoreApplication.translate("FileImportWizard", u"Year", None))
        self.combo_idx_3.setItemText(1, QCoreApplication.translate("FileImportWizard", u"Site", None))
        self.combo_idx_3.setItemText(2, QCoreApplication.translate("FileImportWizard", u"Plot", None))

        self.label_7.setText(QCoreApplication.translate("FileImportWizard", u"Subfolder 1", None))
        self.combo_idx_2.setItemText(0, QCoreApplication.translate("FileImportWizard", u"Year", None))
        self.combo_idx_2.setItemText(1, QCoreApplication.translate("FileImportWizard", u"Site", None))
        self.combo_idx_2.setItemText(2, QCoreApplication.translate("FileImportWizard", u"Plot", None))

        self.label_6.setText(QCoreApplication.translate("FileImportWizard", u"Subfolder 2", None))
        self.combo_idx_1.setItemText(0, QCoreApplication.translate("FileImportWizard", u"Year", None))
        self.combo_idx_1.setItemText(1, QCoreApplication.translate("FileImportWizard", u"Site", None))
        self.combo_idx_1.setItemText(2, QCoreApplication.translate("FileImportWizard", u"Plot", None))

        self.radio_site_manual.setText(QCoreApplication.translate("FileImportWizard", u"Manually enter the relevant information (does not work with folder import with subfolders as multiple sites could be imported this way)", None))
        self.radio_file.setText(QCoreApplication.translate("FileImportWizard", u"Import files", None))
        self.checkbox_load_info.setText(QCoreApplication.translate("FileImportWizard", u"Load information file instead of parsing all files if present", None))
        self.btn_browse_src.setText(QCoreApplication.translate("FileImportWizard", u"Browse", None))
        self.page2.setTitle(QCoreApplication.translate("FileImportWizard", u"Review selected files", None))
        self.page2.setSubTitle(QCoreApplication.translate("FileImportWizard", u"Here you can see what files have been selected and what information will be imported into the database", None))
        self.lbl_status.setText("")
        self.page3.setTitle(QCoreApplication.translate("FileImportWizard", u"File management options", None))
        self.page3.setSubTitle(QCoreApplication.translate("FileImportWizard", u"Please select additional import options", None))
        self.checkbox_rename.setText(QCoreApplication.translate("FileImportWizard", u"Rename files (files will be renamed with the following convention: SITE-ABBREV_PLOT_yyyy-MM-dd_hh:mm:ss)", None))
        self.label_11.setText(QCoreApplication.translate("FileImportWizard", u"<html><head/><body><p><span style=\" font-weight:600;\">IMPORTANT</span>: All .wac files (SongMeter SM2 files) will be converted to .wav files to allow for easy analysis. By default, these files will be<br/>created in the original folder and the original .wac files will be compressed in a zip archive.</p></body></html>", None))
        self.radio_new_folder.setText(QCoreApplication.translate("FileImportWizard", u"Select new destination folder", None))
        self.radio_data_source.setText(QCoreApplication.translate("FileImportWizard", u"Select existing data source", None))
        self.label_12.setText(QCoreApplication.translate("FileImportWizard", u"<b>Select destination folder</b>", None))
        self.checkbox_overwrite.setText(QCoreApplication.translate("FileImportWizard", u"Overwrite existing files", None))
        self.btn_browse_dest.setText(QCoreApplication.translate("FileImportWizard", u"Browse...", None))
        self.label_14.setText(QCoreApplication.translate("FileImportWizard", u"Data source name", None))
        self.checkbox_new_datasource.setText(QCoreApplication.translate("FileImportWizard", u"Add new destination as data source", None))
        self.checkbox_move.setText(QCoreApplication.translate("FileImportWizard", u"Move files", None))
        self.checkbox_link.setText(QCoreApplication.translate("FileImportWizard", u"Create links to files instead of renaming", None))
        self.compression_options.setTitle(QCoreApplication.translate("FileImportWizard", u"Compression options", None))
        self.radio_zip.setText(QCoreApplication.translate("FileImportWizard", u"ZIP", None))
        self.radio_7z.setText(QCoreApplication.translate("FileImportWizard", u"7z (Recommended)", None))
        self.label_10.setText(QCoreApplication.translate("FileImportWizard", u"Use the following compression format:", None))
        self.radio_tar.setText(QCoreApplication.translate("FileImportWizard", u"tar", None))
        self.checkbox_archive.setText(QCoreApplication.translate("FileImportWizard", u"Create a compressed archive of the files", None))
        self.checkbox_flac.setText(QCoreApplication.translate("FileImportWizard", u"Compress wav files to FLAC", None))
        self.checkbox_reimport.setText(QCoreApplication.translate("FileImportWizard", u"Re-import files that already exist in database", None))
        self.page4.setTitle(QCoreApplication.translate("FileImportWizard", u"Summary", None))
        self.page4.setSubTitle(QCoreApplication.translate("FileImportWizard", u"Please review the selected options", None))
        self.label_13.setText(QCoreApplication.translate("FileImportWizard", u"<html><head/><body><p>Please make sure everything is in order before clicking on <span style=\" font-style:italic;\">Finish</span> because changes <span style=\" font-weight:600;\">WILL BE IRREVERSIBLE !!!</span></p></body></html>", None))
        self.page5.setTitle(QCoreApplication.translate("FileImportWizard", u"Performing file manipulation and import", None))
        self.page5.setSubTitle(QCoreApplication.translate("FileImportWizard", u"We are now converting/moving/renaming and importing the selected files", None))
        self.lbl_removing.setText(QCoreApplication.translate("FileImportWizard", u"Compressing and removing wac files", None))
        self.checkbox_done.setText("")
        self.lbl_renaming.setText(QCoreApplication.translate("FileImportWizard", u"Renaming and moving audio files", None))
        self.lbl_converting.setText(QCoreApplication.translate("FileImportWizard", u"Converting WAC files to wav", None))
        self.lbl_saving.setText(QCoreApplication.translate("FileImportWizard", u"Saving files in database", None))
    # retranslateUi

