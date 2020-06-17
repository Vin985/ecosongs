from PySide2.QtWidgets import QTableView
from PySide2.QtCore import QSortFilterProxyModel

from gui.widgets.common.table.dataframe_table_model import DataFrameTableModel


class DataFrameTableView(QTableView):

    def setModel(self, df):
        model = DataFrameTableModel(df)
        # proxyModel = QSortFilterProxyModel()
        # proxyModel.setSourceModel(model)
        super().setModel(model)
