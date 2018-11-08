import pandas as pd

from db.dbmanager import DBManager


class HDF5Manager (DBManager):
    def __init__(self, name, path=None):
        self.store = pd.HDFStore(path + "/" + name + '.h5')
        # TODO: add to settings? Make it more flexible
        self.format = "table"

    def get_table(self, table):
        return self.store[table]

    def save(self, table, data, update=False):
        # Ignore update for the time being as we dont append rows
        self.store.put(table, data, format=self.format)

    # def update(self, table, data):
    #     self.store.append(table, data, format=self.format)
