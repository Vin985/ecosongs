from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel


class RecordingsTreeModel(QStandardItemModel):
    def __init__(self, parent, recordings, categories=["site", "plot", "year"]):
        super(self.__class__, self).__init__(1, 0, parent)
        self.clear()
        self.create_model(categories, recordings)
        # self.insertColumn(1)

    def create_model(self, categories, recordings, path={}, parent=None):
        category = categories[0]
        groups = recordings.groupby(category)
        for (entry, recs) in groups:
            # Create path to the folder in a dict
            path[category] = entry
            # item is a folder. add path to it
            item = self.create_item(entry, path, folder=True)
            if len(categories) > 1:
                self.create_model(categories[1:], recs, path, item)
            else:
                # item is a recording. No path as whole recording will be in data
                self.add_recordings(recordings, item)
            if parent:
                parent.appendRow(item)
            else:
                self.appendRow(item)

    def create_item(self, name, path=None, folder=False):
        result = QStandardItem(name)
        result.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        # If item is a folder, set path as Data
        if path:
            result.setData(path)
        icon = QIcon()
        if folder:
            icon_path = ":/tango/folder"
        else:
            icon_path = ":/tango/audio"
        icon.addPixmap(QPixmap(icon_path), QIcon.Normal, QIcon.Off)
        result.setIcon(icon)
        return result

    def add_recordings(self, recordings, parent):
        for row in recordings.itertuples(index=False):
            self.add_recording(row, parent)

    def add_recording(self, recording, parent):
        item = self.create_item(recording.name)
        # set whole line as data
        item.setData(recording)
        # if we want to add another column in tree
        # path = self.create_item(recording.path)
        # parent.appendRow([item, path])
        parent.appendRow(item)
