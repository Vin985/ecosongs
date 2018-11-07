from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel


class RecordingItem(QStandardItem):
    is_folder = False


class FolderItem(QStandardItem):
    is_folder = True


class RecordingsTreeModel(QStandardItemModel):
    def __init__(self, parent, recordings, categories=["site", "plot", "year"]):
        super(self.__class__, self).__init__(1, 0, parent)
        self.categories = categories
        self.clear()
        root = FolderItem("Audio")
        self.appendRow(root)
        recordings = recordings.sort_values(categories + ["date"])
        self.create_model(categories, recordings, parent=root)
        # self.insertColumn(1)

    def create_model(self, categories, recordings, path={}, parent=None):
        if not recordings.empty:
            category = categories[0]
            groups = recordings.groupby(category, sort=False)
            for (entry, recs) in groups:
                # Create path to the folder in a dict
                path[category] = entry
                # item is a folder. add path to it
                item = self.create_item(entry, path, folder=True)
                if len(categories) > 1:
                    self.create_model(categories[1:], recs, path.copy(), item)
                else:
                    # item is a recording. No path as whole recording will be in data
                    self.add_recordings(recordings, item)
                if parent:
                    parent.appendRow(item)
                    # print(parent.child(0, 0).text())
                else:
                    self.appendRow(item)

    def create_item(self, name, path=None, folder=False):
        if folder:
            item = FolderItem(name)
            icon_path = ":/tango/folder"
        else:
            item = RecordingItem(name)
            icon_path = ":/tango/audio"
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        # If item is a folder, set path as Data
        if path:
            item.setData(path)
        # set item icon
        icon = QIcon()
        icon.addPixmap(QPixmap(icon_path), QIcon.Normal, QIcon.Off)
        item.setIcon(icon)
        return item

    def add_recordings(self, recordings, parent):
        for row in recordings.itertuples(index=True):
            self.add_recording(row, parent)

    def add_recording(self, recording, parent):
        item = self.create_item(recording.name)
        # set whole line as data
        item.setData(recording._asdict())
        # if we want to add another column in tree
        # path = self.create_item(recording.path)
        # parent.appendRow([item, path])
        parent.appendRow(item)
