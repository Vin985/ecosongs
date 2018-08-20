# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileimport.ui',
# licensing of 'fileimport.ui' applies.
#
# Created: Sun Aug 19 23:51:38 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1530708810518
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FileImport(object):
    def setupUi(self, FileImport):
        FileImport.setObjectName("FileImport")
        FileImport.resize(896, 597)
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
        self.idx_2 = QtWidgets.QComboBox(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idx_2.sizePolicy().hasHeightForWidth())
        self.idx_2.setSizePolicy(sizePolicy)
        self.idx_2.setObjectName("idx_2")
        self.idx_2.addItem("")
        self.idx_2.addItem("")
        self.idx_2.addItem("")
        self.horizontalLayout_2.addWidget(self.idx_2)
        self.label_7 = QtWidgets.QLabel(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.idx_1 = QtWidgets.QComboBox(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idx_1.sizePolicy().hasHeightForWidth())
        self.idx_1.setSizePolicy(sizePolicy)
        self.idx_1.setObjectName("idx_1")
        self.idx_1.addItem("")
        self.idx_1.addItem("")
        self.idx_1.addItem("")
        self.horizontalLayout_2.addWidget(self.idx_1)
        self.label_6 = QtWidgets.QLabel(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.idx_3 = QtWidgets.QComboBox(self.site_auto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idx_3.sizePolicy().hasHeightForWidth())
        self.idx_3.setSizePolicy(sizePolicy)
        self.idx_3.setObjectName("idx_3")
        self.idx_3.addItem("")
        self.idx_3.addItem("")
        self.idx_3.addItem("")
        self.horizontalLayout_2.addWidget(self.idx_3)
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 861, 451))
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
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 851, 451))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_4.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radio_compression = QtWidgets.QButtonGroup(FileImport)
        self.radio_compression.setObjectName("radio_compression")
        self.radio_compression.addButton(self.radioButton_3)
        self.gridLayout_5.addWidget(self.radioButton_3, 4, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radio_compression.addButton(self.radioButton_2)
        self.gridLayout_5.addWidget(self.radioButton_2, 3, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radio_compression.addButton(self.radioButton)
        self.gridLayout_5.addWidget(self.radioButton, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 0, 0, 1, 2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_5.addWidget(self.checkBox_4, 1, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 2, 0, 1, 3)
        FileImport.addPage(self.page3)
        self.page4 = QtWidgets.QWizardPage()
        self.page4.setObjectName("page4")
        FileImport.addPage(self.page4)

        self.retranslateUi(FileImport)
        self.idx_1.setCurrentIndex(1)
        self.idx_3.setCurrentIndex(2)
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
        self.idx_2.setItemText(0, QtWidgets.QApplication.translate("FileImport", "Year", None, -1))
        self.idx_2.setItemText(1, QtWidgets.QApplication.translate("FileImport", "Site", None, -1))
        self.idx_2.setItemText(2, QtWidgets.QApplication.translate("FileImport", "Plot", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("FileImport", "Subfolder 1", None, -1))
        self.idx_1.setItemText(0, QtWidgets.QApplication.translate("FileImport", "Year", None, -1))
        self.idx_1.setItemText(1, QtWidgets.QApplication.translate("FileImport", "Site", None, -1))
        self.idx_1.setItemText(2, QtWidgets.QApplication.translate("FileImport", "Plot", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("FileImport", "Subfolder 2", None, -1))
        self.idx_3.setItemText(0, QtWidgets.QApplication.translate("FileImport", "Year", None, -1))
        self.idx_3.setItemText(1, QtWidgets.QApplication.translate("FileImport", "Site", None, -1))
        self.idx_3.setItemText(2, QtWidgets.QApplication.translate("FileImport", "Plot", None, -1))
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
        self.checkBox_2.setText(QtWidgets.QApplication.translate("FileImport", "Overwrite existing files", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("FileImport", "Move and rename files", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("FileImport", "Compression options", None, -1))
        self.radioButton_3.setText(QtWidgets.QApplication.translate("FileImport", "tar", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("FileImport", "ZIP", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("FileImport", "7z (Recommended)", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("FileImport", "Use the following compression format:", None, -1))
        self.checkBox_3.setText(QtWidgets.QApplication.translate("FileImport", "Compress wav files to FLAC", None, -1))
        self.checkBox_4.setText(QtWidgets.QApplication.translate("FileImport", "Create a compressed archive of the files", None, -1))

