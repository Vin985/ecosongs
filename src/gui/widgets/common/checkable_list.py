import sys

from PySide2.QtWidgets import QApplication

from PySide2.QtWidgets import QListWidget, QListWidgetItem
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor, QPalette


class CheckableList(QListWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.palette = QPalette()
        self.selected = set()
        self.from_click = False
        self.linkEvents()

    def linkEvents(self):
        self.itemDoubleClicked.connect(self.select_item)
        # self.itemPressed.connect(self.select_item)
        self.itemChanged.connect(self.update_selected)

    def update_selected(self, item):
        if item.checkState() == Qt.Checked:
            self.selected.add(item.text())
        else:
            if item.text() in self.selected:
                self.selected.remove(item.text())
        print(self.selected)

    def select_item(self, item):
        self.revert_item_state(item)

    def revert_item_state(self, item):
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)

    def addItems(self, items, checked=False):
        for i in items:
            item = QListWidgetItem(i, parent=self)
            self.addItem(item)
            state = Qt.Checked if checked else Qt.Unchecked
            item.setCheckState(state)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test_list = ["toto", "tutu", "hello", "world"]
    cl = CheckableList()
    cl.addItems(test_list, True)
    cl.show()
    app.exec_()
