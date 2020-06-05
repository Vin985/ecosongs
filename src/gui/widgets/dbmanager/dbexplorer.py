
#import resource

from gui.utils.dataframeTableModel import DataFrameTableModel
from gui.widgets.dbmanager.ui.dbexplorer_ui import Ui_DBExplorer
from gui.widgets.common.page_widget import PageWidget


class DBExplorer(PageWidget, Ui_DBExplorer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_dialog = None
        self.linkEvents()
        self.addAction(self.action_ACI)
        self.init_table_selector()

    # def enter_page(self):
    #     print(self.comboBox_table.currentIndex())
    #     self.display_table(self.comboBox_table.currentIndex())
    #     print('dbexplorer4: Memory usage: %s (kb)' %
    #           resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

    # def leave_page(self):
    #     self.setTableModel(None)

    def linkEvents(self):
        self.combo_table.currentIndexChanged.connect(self.display_table)
        self.btn_export.clicked.connect(self.export_table)

    def init_table_selector(self):
        tables = qApp.tables.list_tables()
        for table in tables:
            display_name = table.replace("_", " ")
            self.combo_table.addItem(display_name, table)
        self.display_table(self.combo_table.currentIndex())

    def export_table(self):
        # TODO use dbmanager instead
        index = self.combo_table.currentIndex()
        if index:
            table = self.combo_table.itemData(index)
            from gui.widgets.dialogs.export_table_dialog import ExportTableDialog
            self.action_dialog = ExportTableDialog(table, parent=self)
            self.action_dialog.setModal(True)
            self.action_dialog.show()

    def display_table(self, index):
        model = []
        text = ""
        if index:
            if not self.btn_export.isEnabled():
                self.btn_export.setEnabled(True)
            table = self.combo_table.itemData(index)
            model = qApp.tables.get_table(table).df
            text = "{0} entries(s) found!".format(len(model))
        else:
            self.btn_export.setEnabled(False)

        self.setTableModel(model)
        self.rowsFound.setText(text)

    def setTableModel(self, data):
        model = DataFrameTableModel(data)
        self.dbTable.setModel(model)
        # proxyModel = QSortFilterProxyModel()
        # proxyModel.setSourceModel(model)
        # self.dbTable.setModel(proxyModel)

    def refresh_table(self):
        pass
