from PySide2.QtWidgets import QDialog

from gui.widgets.menus.ui.progressdialog_ui import Ui_ProgressDialog


class ProgressDialog(QDialog, Ui_ProgressDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
