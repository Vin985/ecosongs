from db.models import RecordingModel
from gui.utils.dataframeTableModel import DataFrameTableModel
from gui.widgets.dbmanager.fileimport import FileImport
from gui.widgets.dbmanager.ui.dbexplorer_ui import Ui_DBExplorer
from PySide2.QtCore import QSortFilterProxyModel
from PySide2.QtGui import qApp
from PySide2.QtWidgets import QWidget


class DBExplorer(QWidget, Ui_DBExplorer):
    def __init__(self, recordings=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        recordings = qApp.get_recordings()

        self.rowsFound.setText(
            "{0} recording(s) found!".format(len(recordings)))
        self.initTableView()
        self.linkEvents()
        self.addAction(self.action_ACI)

    def linkEvents(self):
        self.dbImportButton.clicked.connect(self.showImportWindow)

    def import_files(self):
        print("importing files")

    def initTableView(self):
        if qApp.get_recordings().empty:
            self.dbTable.setEnabled(False)
        else:
            model = qApp.get_recordings()
            model["date"] = model["date"].dt.strftime("%Y-%m-%d %H:%M:%S")
            model = DataFrameTableModel(model)
            proxyModel = QSortFilterProxyModel()
            proxyModel.setSourceModel(model)
            self.dbTable.setModel(proxyModel)
            self.dbTable.resizeColumnsToContents()

    def loadRecordings(self):
        return(RecordingModel.select())

    def showImportWindow(self):
        self.file_import = FileImport()
        self.file_import.accepted.connect(self.import_files)
        self.file_import.show()
