from analyse.indexes import ACITable
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
        # TODO: change the way this is loaded
        # use text to display as data
        self.comboBox_table.addItem("Recordings", "Recording")
        self.comboBox_table.addItem("ACI", "ACI")

    def linkEvents(self):
        self.dbImportButton.clicked.connect(self.showImportWindow)
        self.comboBox_table.currentIndexChanged.connect(self.display_table)
        self.btn_export.clicked.connect(self.export_table)

    def export_table(self):
        self.current_table.to_feather(self.comboBox_table.currentText() + ".feather")

    def display_table(self, index):
        table = self.comboBox_table.itemData(index)
        if table == "Recording":
            model = qApp.get_recordings()
        elif table == "ACI":
            model = ACITable(dbmanager=qApp.dbmanager).df
        self.setTableModel(model)
        self.current_table = model

    def initTableView(self):
        if qApp.get_recordings().empty:
            self.dbTable.setEnabled(False)
        else:
            # model["date"] = model["date"].dt.strftime("%Y-%m-%d %H:%M:%S")
            # self.setTableModel(qApp.get_recordings())
            self.dbTable.resizeColumnsToContents()

    def setTableModel(self, data):
        model = DataFrameTableModel(data)
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(model)
        self.dbTable.setModel(proxyModel)

    def refresh_table(self):
        self.setTableModel(qApp.get_recordings())
        print("aaaah refreshing!!!")

    def showImportWindow(self):
        self.file_import = FileImport()
        self.file_import.finished.connect(self.refresh_table)
        self.file_import.show()
