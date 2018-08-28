# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treeexplorer.ui',
# licensing of 'treeexplorer.ui' applies.
#
# Created: Tue Aug 28 10:14:07 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1530708810518
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TreeExplorer(object):
    def setupUi(self, TreeExplorer):
        TreeExplorer.setObjectName("TreeExplorer")
        TreeExplorer.resize(610, 456)
        self.gridLayout = QtWidgets.QGridLayout(TreeExplorer)
        self.gridLayout.setObjectName("gridLayout")
        self.tree_view = QtWidgets.QTreeView(TreeExplorer)
        self.tree_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tree_view.setUniformRowHeights(True)
        self.tree_view.setSortingEnabled(True)
        self.tree_view.setHeaderHidden(True)
        self.tree_view.setObjectName("tree_view")
        self.tree_view.header().setVisible(False)
        self.gridLayout.addWidget(self.tree_view, 0, 0, 1, 1)
        self.action_ACI = QtWidgets.QAction(TreeExplorer)
        self.action_ACI.setObjectName("action_ACI")
        self.action_see_details = QtWidgets.QAction(TreeExplorer)
        self.action_see_details.setObjectName("action_see_details")

        self.retranslateUi(TreeExplorer)
        QtCore.QMetaObject.connectSlotsByName(TreeExplorer)

    def retranslateUi(self, TreeExplorer):
        TreeExplorer.setWindowTitle(QtWidgets.QApplication.translate("TreeExplorer", "Form", None, -1))
        self.action_ACI.setText(QtWidgets.QApplication.translate("TreeExplorer", "Compute ACI", None, -1))
        self.action_see_details.setText(QtWidgets.QApplication.translate("TreeExplorer", "See Details", None, -1))

