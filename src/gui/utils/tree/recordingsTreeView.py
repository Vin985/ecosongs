
from gui.utils.tree.recordingsTreeModel import RecordingsTreeModel
from PySide2.QtCore import Signal
from PySide2.QtGui import qApp
from PySide2.QtWidgets import QMenu, QTreeView, QWidget

# DEPRECATED: useless, replace with cassical tree view


class RecordingsTreeView(QTreeView):

    show_recording_details = Signal(list)
    show_folder_details = Signal(list)
    compute_ACI = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        recordings = qApp.get_recordings()
        # Change to treeview
        self.setModel(RecordingsTreeModel(self, recordings))
        self.link_events()

    def link_events(self):
        self.selectionModel().selectionChanged.connect(self.tree_selection_changed)

    def tree_selection_changed(self, new, old):
        # TODO: setting to enable/disable display on each selection change
        # TODO: handle multiple selection
        index = new.indexes()[0]
        item = index.model().itemFromIndex(index)
        if item.hasChildren():
            # item is folder
            self.show_folder_details.emit(item.data())
        else:
            # item is recording
            self.show_recording_details.emit(item.data())
