from PySide2.QtWidgets import QStackedWidget
from PySide2.QtCore import Signal


class PageStackedWidget(QStackedWidget):

    change_page = Signal(int, dict)

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.pages = {}

    def addWidget(self, widget):
        pos = super().addWidget(widget)
        widget_name = widget.objectName()
        if widget_name.endswith("_page"):
            widget_name = widget_name[:-5]
        self.pages[widget_name] = pos
        widget.change_page.connect(self.change_page_by_name)

    def change_page_by_name(self, name, opts):
        self.change_page.emit(self.pages[name], opts)
        # self.setCurrentIndex(self.pages[name])
