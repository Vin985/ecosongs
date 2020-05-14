# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tag_import_options.ui'
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


class Ui_TagImportOptions(object):
    def setupUi(self, TagImportOptions):
        if TagImportOptions.objectName():
            TagImportOptions.setObjectName(u"TagImportOptions")
        TagImportOptions.resize(400, 300)
        self.gridLayout = QGridLayout(TagImportOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(TagImportOptions)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 3)

        self.label_3 = QLabel(TagImportOptions)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_2 = QLabel(TagImportOptions)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.input_extensions = QLineEdit(TagImportOptions)
        self.input_extensions.setObjectName(u"input_extensions")

        self.gridLayout.addWidget(self.input_extensions, 3, 2, 1, 1)

        self.label = QLabel(TagImportOptions)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.input_tag_folder = QLineEdit(TagImportOptions)
        self.input_tag_folder.setObjectName(u"input_tag_folder")

        self.gridLayout.addWidget(self.input_tag_folder, 1, 2, 1, 1)

        self.checkbox_save = QCheckBox(TagImportOptions)
        self.checkbox_save.setObjectName(u"checkbox_save")
        self.checkbox_save.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_save, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 3)

        self.input_suffix = QLineEdit(TagImportOptions)
        self.input_suffix.setObjectName(u"input_suffix")

        self.gridLayout.addWidget(self.input_suffix, 2, 2, 1, 1)

        self.checkbox_overwrite = QCheckBox(TagImportOptions)
        self.checkbox_overwrite.setObjectName(u"checkbox_overwrite")
        self.checkbox_overwrite.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_overwrite, 5, 1, 1, 2)


        self.retranslateUi(TagImportOptions)

        QMetaObject.connectSlotsByName(TagImportOptions)
    # setupUi

    def retranslateUi(self, TagImportOptions):
        TagImportOptions.setWindowTitle(QCoreApplication.translate("TagImportOptions", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("TagImportOptions", u"Tag import options", None))
        self.label_3.setText(QCoreApplication.translate("TagImportOptions", u"Extensions", None))
        self.label_2.setText(QCoreApplication.translate("TagImportOptions", u"Tag file suffix", None))
#if QT_CONFIG(tooltip)
        self.input_extensions.setToolTip(QCoreApplication.translate("TagImportOptions", u"<html><head/><body><p>List all valid extensions, separated with a semi-colon (<span style=\" font-weight:600;\">;</span>).<span style=\" font-weight:600;\"> Note:</span>The trailing dot (<span style=\" font-weight:600;\">.</span>) must be included. Different case of a similar extension should also be included. Ex: .csv;.CSV</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.input_extensions.setText(QCoreApplication.translate("TagImportOptions", u".csv", None))
        self.label.setText(QCoreApplication.translate("TagImportOptions", u"Tags folder name", None))
        self.input_tag_folder.setText(QCoreApplication.translate("TagImportOptions", u"labels", None))
        self.checkbox_save.setText(QCoreApplication.translate("TagImportOptions", u"Save results", None))
        self.input_suffix.setText(QCoreApplication.translate("TagImportOptions", u"-sceneRect", None))
        self.checkbox_overwrite.setText(QCoreApplication.translate("TagImportOptions", u"Overwrite_results", None))
    # retranslateUi

