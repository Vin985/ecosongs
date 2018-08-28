from PySide2.QtCore import QAbstractTableModel, QModelIndex, Qt


class RecordingsTableModel(QAbstractTableModel):
    display_columns = ["name", "date", "filepath", "type"]

    def __init__(self, recordings=None, parent=None):
        super(RecordingsTableModel, self).__init__(parent)

        if recordings is None:
            self.recordings = []
        else:
            self.recordings = recordings

    def rowCount(self, index=QModelIndex()):
        """ Returns the number of rows the model holds. """
        return len(self.recordings)

    def columnCount(self, index=QModelIndex()):
        """ Returns the number of columns the model holds. """
        return (len(self.display_columns))

    def data(self, index, role=Qt.DisplayRole):
        """ Depending on the index and role given, return data. If not
            returning data, return None (PySide equivalent of QT's
            "invalid QVariant").
        """
        if not index.isValid():
            return None

        if not 0 <= index.row() < len(self.recordings):
            return None

        if role == Qt.DisplayRole:
            recording = self.recordings[index.row()]
            return(getattr(recording, self.display_columns[index.column()]))

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """ Set the headers to be displayed. """
        if role != Qt.DisplayRole:
            return None

        if not len(self.recordings):
            return None

        return(self.display_columns[section])

        if orientation == Qt.Horizontal:
            if section == 0:
                return "Name"
            elif section == 1:
                return "Type"

        return None

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
