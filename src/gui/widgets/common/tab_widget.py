from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal


class TabWidget(QWidget):

    change_tab = Signal(str, dict)

    def enter_tab(self, opts):
        pass

    def leave_tab(self):
        pass
