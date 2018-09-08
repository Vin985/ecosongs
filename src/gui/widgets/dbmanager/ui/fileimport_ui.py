# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileimport.ui',
# licensing of 'fileimport.ui' applies.
#
# Created: Fri Sep  7 14:52:00 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1530708810518
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FileImport(object):
    def setupUi(self, FileImport):
        FileImport.setObjectName("FileImport")
        FileImport.setEnabled(True)
        FileImport.resize(896, 665)
        self.page1 = QtWidgets.QWizardPage()
        self.page1.setObjectName("page1")
        self.layoutWidget = QtWidgets.QWidget(self.page1)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 870, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(10, -1, 10, -1)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.input_src_path = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_src_path.sizePolicy().hasHeightForWidth())
        self.input_src_path.setSizePolicy(sizePolicy)
        self.input_src_path.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.input_src_path.setObjectName("input_src_path")
        self.gridLayout.addWidget(self.input_src_path, 1, 0, 1, 3)
        self.radio_folder = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_folder.sizePolicy().hasHeightForWidth())
        self.radio_folder.setSizePolicy(sizePolicy)
        self.radio_folder.setChecked(True)
        self.radio_folder.setObjectName("radio_folder")
        self.radio_is_folder = QtWidgets.QButtonGroup(FileImport)
        self.radio_is_folder.setObjectName("radio_is_folder")
        self.radio_is_folder.addButton(self.radio_folder)
        self.gridLayout.addWidget(self.radio_folder, 0, 0, 1, 1)
        self.radio_file = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_file.sizePolicy().hasHeightForWidth())
        self.radio_file.setSizePolicy(sizePolicy)
        self.radio_file.setMinimumSize(QtCore.QSize(0, 0))
        self.radio_file.setChecked(False)
        self.radio_file.setObjectName("radio_file")
        self.radio_is_folder.addButton(self.radio_file)
        self.gridLayout.addWidget(self.radio_file, 0, 1, 1, 1)
        self.btn_browse_src = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_browse_src.sizePolicy().hasHeightForWidth())
        self.btn_browse_src.setSizePolicy(sizePolicy)
        self.btn_browse_src.setObjectName("btn_browse_src")
        self.gridLayout.addWidget(self.btn_browse_src, 1, 3, 1, 1)
        self.site_manual = QtWidgets.QWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.site_manual.sizePolicy().hasHeightForWidth())
        self.site_manual.setSizePolicy(sizePolicy)
        self.site_manual.setObjectName("site_manual")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.site_manual)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.site_manual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.input_year = QtWidgets.QLineEdit(self.site_manual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_year.sizePolicy().hasHeightForWidth())
        self.input_year.setSizePolicy(sizePolicy)
        self.input_year.setObjectName("input_year")
        self.horizontalLayout.addWidget(self.input_year)
        self.label = QtWidgets.QLabel(self.site_manual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.input_site = QtWidgets.QLineEdit(self.site_manual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_site.sizePolicy().hasHeightForWidth())
        self.input_site.setSizePolicy(sizePolicy)
        self.input_site.setObjectName("input_site")
        self.horizontalLayout.addWidget(self.input_site)
        self.label_4 = QtWidgets.QLabel(self.site_manual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.input_plot = QtWidgets.QLineEdit(self.site_manual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_plot.sizePolicy().hasHeightForWidth())
        self.input_plot.setSizePolicy(sizePolicy)
        self.input_plot.setObjectName("input_plot")
        self.horizontalLayout.addWidget(self.input_plot)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.site_manual, 8, 0, 1, 4)
        self.site_auto = QtWidgets.QWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.site_auto.sizePolicy().hasHeightForWidth())
        self.site_auto.setSizePolicy(sizePolicy)
        self.site_auto.setObjectName("site_auto")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.site_auto)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.combo_idx_3 = QtWidgets.QComboBox(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_idx_3.sizePolicy().hasHeightForWidth())
        self.combo_idx_3.setSizePolicy(sizePolicy)
        self.combo_idx_3.setObjectName("combo_idx_3")
        self.combo_idx_3.addItem("")
        self.combo_idx_3.addItem("")
        self.combo_idx_3.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_idx_3)
        self.label_7 = QtWidgets.QLabel(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.combo_idx_2 = QtWidgets.QComboBox(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_idx_2.sizePolicy().hasHeightForWidth())
        self.combo_idx_2.setSizePolicy(sizePolicy)
        self.combo_idx_2.setObjectName("combo_idx_2")
        self.combo_idx_2.addItem("")
        self.combo_idx_2.addItem("")
        self.combo_idx_2.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_idx_2)
        self.label_6 = QtWidgets.QLabel(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.combo_idx_1 = QtWidgets.QComboBox(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_idx_1.sizePolicy().hasHeightForWidth())
        self.combo_idx_1.setSizePolicy(sizePolicy)
        self.combo_idx_1.setObjectName("combo_idx_1")
        self.combo_idx_1.addItem("")
        self.combo_idx_1.addItem("")
        self.combo_idx_1.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_idx_1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.site_auto, 7, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 4)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 0, 1, 4)
        self.radio_site_auto = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_site_auto.sizePolicy().hasHeightForWidth())
        self.radio_site_auto.setSizePolicy(sizePolicy)
        self.radio_site_auto.setChecked(True)
        self.radio_site_auto.setObjectName("radio_site_auto")
        self.radio_site_info = QtWidgets.QButtonGroup(FileImport)
        self.radio_site_info.setObjectName("radio_site_info")
        self.radio_site_info.addButton(self.radio_site_auto)
        self.gridLayout.addWidget(self.radio_site_auto, 5, 0, 1, 4)
        self.radio_site_manual = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_site_manual.setEnabled(False)
        self.radio_site_manual.setObjectName("radio_site_manual")
        self.radio_site_info.addButton(self.radio_site_manual)
        self.gridLayout.addWidget(self.radio_site_manual, 6, 0, 1, 4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setMargin(5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.radio_rec_auto = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_rec_auto.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_rec_auto.sizePolicy().hasHeightForWidth())
        self.radio_rec_auto.setSizePolicy(sizePolicy)
        self.radio_rec_auto.setChecked(True)
        self.radio_rec_auto.setObjectName("radio_rec_auto")
        self.radio_recorders = QtWidgets.QButtonGroup(FileImport)
        self.radio_recorders.setObjectName("radio_recorders")
        self.radio_recorders.addButton(self.radio_rec_auto)
        self.horizontalLayout_3.addWidget(self.radio_rec_auto)
        self.radio_rec_sm = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_rec_sm.sizePolicy().hasHeightForWidth())
        self.radio_rec_sm.setSizePolicy(sizePolicy)
        self.radio_rec_sm.setObjectName("radio_rec_sm")
        self.radio_recorders.addButton(self.radio_rec_sm)
        self.horizontalLayout_3.addWidget(self.radio_rec_sm)
        self.radio_rec_am = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_rec_am.sizePolicy().hasHeightForWidth())
        self.radio_rec_am.setSizePolicy(sizePolicy)
        self.radio_rec_am.setObjectName("radio_rec_am")
        self.radio_recorders.addButton(self.radio_rec_am)
        self.horizontalLayout_3.addWidget(self.radio_rec_am)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 4)
        self.checkbox_subfolders = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_subfolders.sizePolicy().hasHeightForWidth())
        self.checkbox_subfolders.setSizePolicy(sizePolicy)
        self.checkbox_subfolders.setChecked(True)
        self.checkbox_subfolders.setObjectName("checkbox_subfolders")
        self.gridLayout.addWidget(self.checkbox_subfolders, 0, 2, 1, 2)
        FileImport.addPage(self.page1)
        self.page2 = QtWidgets.QWizardPage()
        self.page2.setObjectName("page2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 861, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_status = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_status.sizePolicy().hasHeightForWidth())
        self.lbl_status.setSizePolicy(sizePolicy)
        self.lbl_status.setText("")
        self.lbl_status.setObjectName("lbl_status")
        self.gridLayout_3.addWidget(self.lbl_status, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
        self.table_files = QtWidgets.QTableView(self.gridLayoutWidget)
        self.table_files.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_files.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.table_files.setSortingEnabled(True)
        self.table_files.setObjectName("table_files")
        self.table_files.horizontalHeader().setStretchLastSection(True)
        self.table_files.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.table_files, 3, 0, 1, 1)
        FileImport.addPage(self.page2)
        self.page3 = QtWidgets.QWizardPage()
        self.page3.setObjectName("page3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 861, 531))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem6, 1, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem7, 5, 0, 1, 3)
        self.checkbox_rename = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkbox_rename.setChecked(True)
        self.checkbox_rename.setObjectName("checkbox_rename")
        self.gridLayout_4.addWidget(self.checkbox_rename, 2, 0, 1, 1)
        self.checkbox_move = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkbox_move.setChecked(True)
        self.checkbox_move.setObjectName("checkbox_move")
        self.gridLayout_4.addWidget(self.checkbox_move, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 3)
        self.widget_2 = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.button_browse_dest = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_browse_dest.sizePolicy().hasHeightForWidth())
        self.button_browse_dest.setSizePolicy(sizePolicy)
        self.button_browse_dest.setObjectName("button_browse_dest")
        self.gridLayout_7.addWidget(self.button_browse_dest, 5, 4, 1, 1)
        self.input_dest_path = QtWidgets.QLineEdit(self.widget_2)
        self.input_dest_path.setObjectName("input_dest_path")
        self.gridLayout_7.addWidget(self.input_dest_path, 5, 0, 1, 4)
        self.radio_data_source = QtWidgets.QRadioButton(self.widget_2)
        self.radio_data_source.setEnabled(False)
        self.radio_data_source.setChecked(False)
        self.radio_data_source.setObjectName("radio_data_source")
        self.radio_destination = QtWidgets.QButtonGroup(FileImport)
        self.radio_destination.setObjectName("radio_destination")
        self.radio_destination.addButton(self.radio_data_source)
        self.gridLayout_7.addWidget(self.radio_data_source, 2, 0, 1, 1)
        self.checkbox_new_datasource = QtWidgets.QCheckBox(self.widget_2)
        self.checkbox_new_datasource.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_new_datasource.sizePolicy().hasHeightForWidth())
        self.checkbox_new_datasource.setSizePolicy(sizePolicy)
        self.checkbox_new_datasource.setObjectName("checkbox_new_datasource")
        self.gridLayout_7.addWidget(self.checkbox_new_datasource, 6, 0, 1, 1)
        self.combo_datasource = QtWidgets.QComboBox(self.widget_2)
        self.combo_datasource.setEnabled(False)
        self.combo_datasource.setObjectName("combo_datasource")
        self.gridLayout_7.addWidget(self.combo_datasource, 3, 0, 1, 4)
        self.radio_new_folder = QtWidgets.QRadioButton(self.widget_2)
        self.radio_new_folder.setChecked(True)
        self.radio_new_folder.setObjectName("radio_new_folder")
        self.radio_destination.addButton(self.radio_new_folder)
        self.gridLayout_7.addWidget(self.radio_new_folder, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)
        self.input_datasource = QtWidgets.QLineEdit(self.widget_2)
        self.input_datasource.setEnabled(False)
        self.input_datasource.setObjectName("input_datasource")
        self.gridLayout_7.addWidget(self.input_datasource, 6, 2, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 6, 1, 1, 1)
        self.checkbox_overwrite = QtWidgets.QCheckBox(self.widget_2)
        self.checkbox_overwrite.setChecked(True)
        self.checkbox_overwrite.setObjectName("checkbox_overwrite")
        self.gridLayout_7.addWidget(self.checkbox_overwrite, 7, 0, 1, 1)
        self.radio_current_folder = QtWidgets.QRadioButton(self.widget_2)
        self.radio_current_folder.setObjectName("radio_current_folder")
        self.radio_destination.addButton(self.radio_current_folder)
        self.gridLayout_7.addWidget(self.radio_current_folder, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_2, 3, 0, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 2, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
        self.groupBox.setEnabled(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radio_zip = QtWidgets.QRadioButton(self.groupBox)
        self.radio_zip.setObjectName("radio_zip")
        self.radio_compression = QtWidgets.QButtonGroup(FileImport)
        self.radio_compression.setObjectName("radio_compression")
        self.radio_compression.addButton(self.radio_zip)
        self.gridLayout_5.addWidget(self.radio_zip, 2, 2, 1, 1)
        self.radio_7z = QtWidgets.QRadioButton(self.groupBox)
        self.radio_7z.setChecked(True)
        self.radio_7z.setObjectName("radio_7z")
        self.radio_compression.addButton(self.radio_7z)
        self.gridLayout_5.addWidget(self.radio_7z, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)
        self.checkbox_flac = QtWidgets.QCheckBox(self.groupBox)
        self.checkbox_flac.setObjectName("checkbox_flac")
        self.gridLayout_5.addWidget(self.checkbox_flac, 0, 0, 1, 2)
        self.checkbox_archive = QtWidgets.QCheckBox(self.groupBox)
        self.checkbox_archive.setObjectName("checkbox_archive")
        self.gridLayout_5.addWidget(self.checkbox_archive, 1, 0, 1, 2)
        self.radio_tar = QtWidgets.QRadioButton(self.groupBox)
        self.radio_tar.setObjectName("radio_tar")
        self.radio_compression.addButton(self.radio_tar)
        self.gridLayout_5.addWidget(self.radio_tar, 2, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 4, 0, 1, 3)
        FileImport.addPage(self.page3)
        self.page4 = QtWidgets.QWizardPage()
        self.page4.setObjectName("page4")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.page4)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(9, -1, 851, 531))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_8.addWidget(self.label_13, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem9, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget_3)
        self.progressBar.setEnabled(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_8.addWidget(self.progressBar, 3, 0, 1, 1)
        self.log_console = QtWidgets.QTextEdit(self.gridLayoutWidget_3)
        self.log_console.setObjectName("log_console")
        self.gridLayout_8.addWidget(self.log_console, 2, 0, 1, 1)
        FileImport.addPage(self.page4)

        self.retranslateUi(FileImport)
        self.combo_idx_2.setCurrentIndex(1)
        self.combo_idx_1.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(FileImport)

    def retranslateUi(self, FileImport):
        FileImport.setWindowTitle(QtWidgets.QApplication.translate("FileImport", "File import wizard", None, -1))
        self.page1.setTitle(QtWidgets.QApplication.translate("FileImport", "Import files in the database", None, -1))
        self.page1.setSubTitle(QtWidgets.QApplication.translate("FileImport", "Please select the files you want to import.", None, -1))
        self.radio_folder.setText(QtWidgets.QApplication.translate("FileImport", "Import a folder", None, -1))
        self.radio_file.setText(QtWidgets.QApplication.translate("FileImport", "Import files", None, -1))
        self.btn_browse_src.setText(QtWidgets.QApplication.translate("FileImport", "Browse", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("FileImport", "Year", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("FileImport", "Site", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("FileImport", "Plot", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("FileImport", "Define the order in which the information is stocked on the hard drive starting with the topmost folder:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("FileImport", "Top folder", None, -1))
        self.combo_idx_3.setItemText(0, QtWidgets.QApplication.translate("FileImport", "Year", None, -1))
        self.combo_idx_3.setItemText(1, QtWidgets.QApplication.translate("FileImport", "Site", None, -1))
        self.combo_idx_3.setItemText(2, QtWidgets.QApplication.translate("FileImport", "Plot", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("FileImport", "Subfolder 1", None, -1))
        self.combo_idx_2.setItemText(0, QtWidgets.QApplication.translate("FileImport", "Year", None, -1))
        self.combo_idx_2.setItemText(1, QtWidgets.QApplication.translate("FileImport", "Site", None, -1))
        self.combo_idx_2.setItemText(2, QtWidgets.QApplication.translate("FileImport", "Plot", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("FileImport", "Subfolder 2", None, -1))
        self.combo_idx_1.setItemText(0, QtWidgets.QApplication.translate("FileImport", "Year", None, -1))
        self.combo_idx_1.setItemText(1, QtWidgets.QApplication.translate("FileImport", "Site", None, -1))
        self.combo_idx_1.setItemText(2, QtWidgets.QApplication.translate("FileImport", "Plot", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("FileImport", "Each file requires information about site, year and plot:", None, -1))
        self.radio_site_auto.setText(QtWidgets.QApplication.translate("FileImport", "Automatically detect information from folder hierarchy. The 3 folders above the audio files will be used to extract the information", None, -1))
        self.radio_site_manual.setText(QtWidgets.QApplication.translate("FileImport", "Manually enter the relevant information (does not work with folder import with subfolders as multiple sites could be imported this way)", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("FileImport", "File type:", None, -1))
        self.radio_rec_auto.setText(QtWidgets.QApplication.translate("FileImport", "Auto-detect", None, -1))
        self.radio_rec_sm.setText(QtWidgets.QApplication.translate("FileImport", "SongMeter", None, -1))
        self.radio_rec_am.setText(QtWidgets.QApplication.translate("FileImport", "Audiomoth", None, -1))
        self.checkbox_subfolders.setText(QtWidgets.QApplication.translate("FileImport", "Include subfolders", None, -1))
        self.page2.setTitle(QtWidgets.QApplication.translate("FileImport", "Review selected files", None, -1))
        self.page2.setSubTitle(QtWidgets.QApplication.translate("FileImport", "Here you can see what files have been selected and what information will be imported into the database", None, -1))
        self.page3.setTitle(QtWidgets.QApplication.translate("FileImport", "File management options", None, -1))
        self.page3.setSubTitle(QtWidgets.QApplication.translate("FileImport", "Please select additional import options", None, -1))
        self.checkbox_rename.setText(QtWidgets.QApplication.translate("FileImport", "Rename files", None, -1))
        self.checkbox_move.setText(QtWidgets.QApplication.translate("FileImport", "Move files", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("FileImport", "<html><head/><body><p><span style=\" font-weight:600;\">IMPORTANT</span>: All .wac files (SongMeter SM2 files) will be converted to .wav files to allow for easy analysis. By default, these files will be<br/>created in the original folder and the original .wac files will be compressed in a zip archive.</p></body></html>", None, -1))
        self.button_browse_dest.setText(QtWidgets.QApplication.translate("FileImport", "Browse...", None, -1))
        self.radio_data_source.setText(QtWidgets.QApplication.translate("FileImport", "Select existing data source", None, -1))
        self.checkbox_new_datasource.setText(QtWidgets.QApplication.translate("FileImport", "Add new destination as data source", None, -1))
        self.radio_new_folder.setText(QtWidgets.QApplication.translate("FileImport", "Select new destination folder", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("FileImport", "<b>Select destination folder</b>", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("FileImport", "Data source name", None, -1))
        self.checkbox_overwrite.setText(QtWidgets.QApplication.translate("FileImport", "Overwrite existing files", None, -1))
        self.radio_current_folder.setText(QtWidgets.QApplication.translate("FileImport", "Use current folder", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("FileImport", "Compression options", None, -1))
        self.radio_zip.setText(QtWidgets.QApplication.translate("FileImport", "ZIP", None, -1))
        self.radio_7z.setText(QtWidgets.QApplication.translate("FileImport", "7z (Recommended)", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("FileImport", "Use the following compression format:", None, -1))
        self.checkbox_flac.setText(QtWidgets.QApplication.translate("FileImport", "Compress wav files to FLAC", None, -1))
        self.checkbox_archive.setText(QtWidgets.QApplication.translate("FileImport", "Create a compressed archive of the files", None, -1))
        self.radio_tar.setText(QtWidgets.QApplication.translate("FileImport", "tar", None, -1))
        self.page4.setTitle(QtWidgets.QApplication.translate("FileImport", "Summary", None, -1))
        self.page4.setSubTitle(QtWidgets.QApplication.translate("FileImport", "Please review the selected options", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("FileImport", "<html><head/><body><p>Please make sure everything is in order before clicking on <span style=\" font-style:italic;\">Finish</span> because changes <span style=\" font-weight:600;\">WILL BE IRREVERSIBLE !!!</span></p></body></html>", None, -1))

