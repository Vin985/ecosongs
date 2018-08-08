from db.models import RecordingModel
from gui.widgets.dbmanager.fileimport import FileImport
from gui.widgets.dbmanager.recordingsTableModel import RecordingsTableModel
from gui.widgets.dbmanager.ui.dbexplorer_ui import Ui_DBExplorer
from PySide2.QtWidgets import QWidget


class DBExplorer(QWidget, Ui_DBExplorer):
    def __init__(self, recordings=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        if not recordings:
            recordings = self.loadRecordings()

        self.file_import = FileImport()

        self.rowsFound.setText(
            "{0} recording(s) found!".format(len(recordings)))
        self.tableModel = RecordingsTableModel(recordings)
        self.initTableView()
        self.linkEvents()

    def linkEvents(self):
        self.dbImportButton.clicked.connect(self.showImportWindow)

    def initTableView(self):
        if not self.tableModel.rowCount():
            self.dbTable.setEnabled(False)
        else:
            self.dbTable.setModel(self.tableModel)
            self.dbTable.resizeColumnsToContents()

    def loadRecordings(self):
        return(RecordingModel.select())

    def showImportWindow(self):
        self.file_import.show()
