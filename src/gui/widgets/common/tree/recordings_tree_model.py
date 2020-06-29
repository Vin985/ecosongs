from PySide2.QtCore import Qt
from PySide2.QtGui import (
    QIcon,
    QPixmap,
    QStandardItem,
    QStandardItemModel,
    QBrush,
    QColor,
)


class RecordingItem(QStandardItem):
    is_folder = False


class FolderItem(QStandardItem):
    is_folder = True


class RecordingsTreeModel(QStandardItemModel):

    BG_GREEN = QBrush(QColor("#a8f79a"))
    BG_WHITE = QBrush(QColor("#ffffff"))
    BG_RED = QBrush(QColor("#ffa3a3"))
    BG_ORANGE = QBrush(QColor("#f6e777"))

    FOLDER_ICON_PATH = ":/tango/folder"
    AUDIO_ICON_PATH = ":/tango/audio"

    TYPE_FOLDER = "folder"
    TYPE_AUDIO = "audio"

    DEFAULT_CATEGORIES = ["site", "plot", "year"]

    def __init__(self, parent, recordings, categories=None):
        super().__init__(1, 0, parent)
        self.df = recordings
        categories = categories or self.DEFAULT_CATEGORIES
        self.clear()
        self.icons = self.create_icons()
        root = FolderItem("Audio")
        self.default_background = root.background()
        self.appendRow(root)
        if not recordings.empty:
            recordings = recordings.sort_values(categories + ["date"])
        self.create_model(categories, recordings, parent=root)
        # self.insertColumn(1)

    def create_icons(self):
        folder_icon = QIcon()
        folder_icon.addPixmap(QPixmap(self.FOLDER_ICON_PATH), QIcon.Normal, QIcon.Off)

        audio_icon = QIcon()
        audio_icon.addPixmap(QPixmap(self.AUDIO_ICON_PATH), QIcon.Normal, QIcon.Off)
        icons = {"folder": folder_icon, "audio": audio_icon}
        return icons

    def create_model(self, categories, recordings, path=None, parent=None):
        path = path or {}
        if not recordings.empty:
            category = categories[0]
            groups = recordings.groupby(category, sort=False, observed=True)
            for (entry, recs) in groups:
                # Create path to the folder in a dict
                path[category] = entry
                # item is a folder. add path to it
                item = self.create_item(entry, self.TYPE_FOLDER, path)
                if len(categories) > 1:
                    self.create_model(categories[1:], recs, path.copy(), item)
                else:
                    # item is a recording. No path as whole recording will be in data
                    self.add_recordings(recs, item)
                if parent:
                    parent.appendRow(item)
                    # print(parent.child(0, 0).text())
                else:
                    self.appendRow(item)

    def create_item(self, name, item_type, path=None):
        if item_type == self.TYPE_FOLDER:
            item = FolderItem(name)
        else:
            item = RecordingItem(name)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        # If item is a folder, set path as Data
        if path:
            item.setData(path)
        # set item icon
        item.setIcon(self.icons[item_type])
        return item

    def add_recordings(self, recordings, parent):
        for row in recordings.itertuples(index=True):
            self.add_recording(row, parent)

    def add_recording(self, recording, parent):
        item = self.create_item(recording.name, self.TYPE_AUDIO)
        # set whole line as data
        item.setData(recording._asdict())
        # if we want to add another column in tree
        # path = self.create_item(recording.path)
        # parent.appendRow([item, path])
        parent.appendRow(item)

    def check_predictions(self, prediction_list, item=None):
        if item is None:
            item = self.item(0, 0)
        have_predictions = 0
        if item.is_folder:
            for i in range(0, item.rowCount()):
                child = item.child(i, 0)
                have_predictions += self.check_predictions(prediction_list, child)
                if have_predictions > 0:
                    if have_predictions == item.rowCount():
                        item.setBackground(self.BG_GREEN)
                        return 1
                    else:
                        item.setBackground(self.BG_ORANGE)
                else:
                    item.setBackground(self.default_background)
        else:
            if item.data()["id"] in prediction_list:
                item.setBackground(self.BG_GREEN)
                return 1
            else:
                item.setBackground(self.default_background)
                return 0
        return 0

    def reset_background(self):
        pass
