import pandas as pd

from db.dbmanager import DBManager


class HDF5Manager (DBManager):
    def __init__(self, name, path=None):
        self.store = pd.HDFStore(path + "/" + name + '.h5')

    def get_table(self, table):
        return self.store[table]

    def save_data(self, table, data, format="fixed", append=False):
        if append:
            self.store.append(table, data, format=format)
        else:
            self.store.put(table, data, format=format)
