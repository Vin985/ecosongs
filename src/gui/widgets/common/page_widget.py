from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal


class PageWidget(QWidget):

    change_page = Signal(str, dict)

    def leave_page(self):
        pass

    def enter_page(self, opts):
        pass

    def option_changed(self, option):
        pass
