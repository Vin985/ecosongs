from PySide2.QtCore import QAbstractTableModel, QModelIndex, Qt


class DataFrameTableModel(QAbstractTableModel):
    display_columns = ["name", "date", "filepath", "recorder"]

    def __init__(self, df=None, parent=None):
        super(DataFrameTableModel, self).__init__(parent)

        if df is None:
            self.df = []
        else:
            self.df = df

    def rowCount(self, index=QModelIndex()):
        """ Returns the number of rows the model holds. """
        return self.df.shape[0]

    def columnCount(self, index=QModelIndex()):
        """ Returns the number of columns the model holds. """
        return self.df.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        """ Depending on the index and role given, return data. If not
            returning data, return None (PySide equivalent of QT's
            "invalid QVariant").
        """
        if index.isValid() and 0 <= index.row() < self.df.shape[0] and role == Qt.DisplayRole:
            return(self.df.iloc[index.row(), index.column()])

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """ Set the headers to be displayed. """
        if role != Qt.DisplayRole:
            return None

        if not self.df.shape[0]:
            return None

        return(self.df.columns.values[section])

    # def insertRows(self, position, rows=1, index=QModelIndex()):
    #     """ Insert a row into the model. """
    #     self.beginInsertRows(QModelIndex(), position, position + rows - 1)
    #
    #     for row in range(rows):
    #         self.addresses.insert(position + row, {"name": "", "address": ""})
    #
    #     self.endInsertRows()
    #     return True
    #
    # def removeRows(self, position, rows=1, index=QModelIndex()):
    #     """ Remove a row from the model. """
    #     self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
    #
    #     del self.addresses[position:position+rows]
    #
    #     self.endRemoveRows()
    #     return True
    #
    # def setData(self, index, value, role=Qt.EditRole):
    #     """ Adjust the data (set it to <value>) depending on the given
    #         index and role.
    #     """
    #     if role != Qt.EditRole:
    #         return False
    #
    #     if index.isValid() and 0 <= index.row() < len(self.addresses):
    #         address = self.addresses[index.row()]
    #         if index.column() == 0:
    #             address["name"] = value
    #         elif index.column() == 1:
    #             address["address"] = value
    #         else:
    #             return False
    #
    #         self.dataChanged.emit(index, index, 0)
    #         return True
    #
    #     return False
    #
    # def flags(self, index):
    #     """ Set the item flags at the given index. Seems like we're
    #         implementing this function just to see how it's done, as we
    #         manually adjust each tableView to have NoEditTriggers.
    #     """
    #     if not index.isValid():
    #         return Qt.ItemIsEnabled
    #     return Qt.ItemFlags(QAbstractTableModel.flags(self, index) |
    #                         Qt.ItemIsEditable)
