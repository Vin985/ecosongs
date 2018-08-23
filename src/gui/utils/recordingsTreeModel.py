from PySide2.QtCore import Qt
from PySide2.QtGui import QStandardItem, QStandardItemModel


class RecordingsTreeModel(QStandardItemModel):
    def __init__(self, parent, recordings):
        super(self.__class__, self).__init__(1, 0, parent)
        self.recordings = recordings
        self.create_model()

    def create_model(self):
        print("creating model!")
        years = self.recordings.groupby(["year"])
        last_entry = None
        for (year, recordings) in years:
            print(year)
            last_entry = self.create_year(year)
            self.appendRow(last_entry)
        print(years)
        print(years.groups)
        pass

    def create_year(self, year):
        result = QStandardItem(year)
        result.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        return result

    def create_site(self):
        pass

    def create_recording(self):
        pass
