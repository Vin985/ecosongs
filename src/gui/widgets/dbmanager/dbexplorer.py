from PySide2.QtGui import qApp
from PySide2.QtWidgets import QWidget

from gui.utils.dataframeTableModel import DataFrameTableModel
from gui.widgets.dbmanager.fileimport import FileImport
from gui.widgets.dbmanager.ui.dbexplorer_ui import Ui_DBExplorer


class DBExplorer(QWidget, Ui_DBExplorer):
    def __init__(self, recordings=None):
        super().__init__()
        self.setupUi(self)
        self.current_table = None
        recordings = qApp.get_recordings()

        self.rowsFound.setText(
            "{0} recording(s) found!".format(len(recordings)))
        self.linkEvents()
        self.addAction(self.action_ACI)
        self.init_table_selector()
        self.initTableView()

    def linkEvents(self):
        self.dbImportButton.clicked.connect(self.showImportWindow)
        self.comboBox_table.currentIndexChanged.connect(self.display_table)
        self.btn_export.clicked.connect(self.export_table)

    def init_table_selector(self):
        tables = qApp.tables.list_tables()
        for table in tables:
            display_name = table.replace("_", " ")
            self.comboBox_table.addItem(display_name, table)

    def initTableView(self):
        if qApp.get_recordings().empty:
            self.dbTable.setEnabled(False)
        else:
            # model["date"] = model["date"].dt.strftime("%Y-%m-%d %H:%M:%S")
            # self.setTableModel(qApp.get_recordings())
            self.dbTable.resizeColumnsToContents()

    def export_table(self):
        self.current_table.to_feather(
            self.comboBox_table.currentText() + ".feather")

    def display_table(self, index):
        table = self.comboBox_table.itemData(index)
        model = qApp.tables.get_table(table).df
        self.setTableModel(model)
        self.current_table = model

    def setTableModel(self, data):
        model = DataFrameTableModel(data)
        self.dbTable.setModel(model)
        # proxyModel = QSortFilterProxyModel()
        # proxyModel.setSourceModel(model)
        # self.dbTable.setModel(proxyModel)

    def refresh_table(self):
        self.setTableModel(qApp.get_recordings())
        print("aaaah refreshing!!!")

    def showImportWindow(self):
        self.file_import = FileImport()
        self.file_import.finished.connect(self.refresh_table)
        self.file_import.show()
