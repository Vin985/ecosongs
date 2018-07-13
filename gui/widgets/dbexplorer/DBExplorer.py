from db.models import RecordingModel
from gui.widgets.dbexplorer.dbexplorer_ui import Ui_DBExplorer
from gui.widgets.dbexplorer.recordingsTableModel import RecordingsTableModel
from PySide2.QtWidgets import QAbstractItemView, QWidget


class DBExplorer(QWidget, Ui_DBExplorer):
    def __init__(self, recordings=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        if not recordings:
            recordings = self.loadRecordings()

        self.rowsFound.setText(
            "{0} recording(s) found!".format(len(recordings)))
        self.tableModel = RecordingsTableModel(recordings)
        self.initTableView()

    def initTableView(self):
        if not self.tableModel.rowCount():
            self.dbTable.setEnabled(False)
        else:
            self.dbTable.setModel(self.tableModel)
            self.dbTable.resizeColumnsToContents()

    def loadRecordings(self):
        return(RecordingModel.select())
