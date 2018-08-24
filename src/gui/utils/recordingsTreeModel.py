from PySide2.QtCore import Qt
from PySide2.QtGui import QStandardItem, QStandardItemModel


class RecordingsTreeModel(QStandardItemModel):
    def __init__(self, parent, recordings, categories=["site", "plot", "year"]):
        super(self.__class__, self).__init__(1, 0, parent)
        self.create_model(categories, recordings)

    def create_model(self, categories, recordings, parent=None):
        print("creating model!")
        groups = recordings.groupby(categories[0])
        for (entry, recs) in groups:
            item = self.create_item(entry)
            if len(categories) > 1:
                self.create_model(categories[1:], recs, item)
            else:
                self.add_recordings(recordings, item)
            if parent:
                parent.appendRow(item)
            else:
                self.appendRow(item)

    def create_item(self, name):
        result = QStandardItem(name)
        result.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        return result

    def add_recordings(self, recordings, parent):
        recordings.apply(self.add_recording, axis=1, parent=parent)

    def add_recording(self, recording, parent):
        item = self.create_item(recording["name"])
        item.setData(recording)
        parent.appendRow(item)
