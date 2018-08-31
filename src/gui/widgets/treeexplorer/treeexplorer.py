
from gui.utils.recordingsTreeModel import RecordingsTreeModel
from gui.widgets.treeexplorer.ui.treeexplorer_ui import Ui_TreeExplorer
from PySide2.QtCore import Signal
from PySide2.QtGui import qApp
from PySide2.QtWidgets import QMenu, QWidget


class TreeExplorer(QWidget, Ui_TreeExplorer):

    show_recording_details = Signal(list)
    show_folder_details = Signal(list)
    compute_ACI = Signal()

    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        recordings = qApp.get_recordings()
        self.tree_view.setModel(RecordingsTreeModel(self.tree_view, recordings))
        self.link_events()
        self.tree_view.addAction(self.action_ACI)
        # self.treeView.setRootIsDecorated(False)
        # self.treeView.setUniformRowHeights(True)
        # self.treeView.setHeaderHidden(True)

    def link_events(self):
        # self.tree_view.activated.connect(self.item_selected)
        self.action_ACI.triggered.connect(self.compute_ACI)
        self.tree_view.customContextMenuRequested.connect(self.context_menu)
        self.tree_view.selectionModel().selectionChanged.connect(self.tree_selection_changed)

    def tree_selection_changed(self, new, old):
        # TODO: setting to enable/disable display on each selection change
        index = new.indexes()[0]
        item = index.model().itemFromIndex(index)
        if item.hasChildren():
            # item is folder
            self.show_folder_details.emit(item.data())
        else:
            # item is recording
            self.show_recording_details.emit(item.data())

    # def item_selected(self):
    #     index = self.tree_view.selectedIndexes()[0]
    #     item = index.model().itemFromIndex(index)
    #     if item.hasChildren():
    #         # item is folder
    #         self.show_folder_details.emit(item.data())
    #     else:
    #         # file
    #         self.show_recording_details.emit(item.data())
    #     print("item selected: ")
    #     print(item.data())

    def compute_ACI(self):
        self.compute_ACI.emit()

    def context_menu(self):
        print("context")

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.action_ACI)
        menu.exec_(event.globalPos())
