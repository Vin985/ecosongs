import os

import feather

from db.dbmanager import DBManager


class FeatherManager(DBManager):
    def __init__(self, path, **kwargs):
        super().__init__()
        self.db_root = path + "/feather/"

    def get_table(self, table):
        data = feather.read_dataframe(self.db_root + table + ".feather")
        data.set_index("id", drop=False, inplace=True)
        return data

    def save(self, table, data):
        if not os.path.exists(self.db_root):
            os.makedirs(self.db_root)
        data.reset_index(inplace=True, drop=True)
        data.to_feather(self.db_root + table + ".feather")

    def update(self, table, data):
        self.save(table, data)

    def delete(self, table, data):
        raise NotImplementedError(
            "Function not implemented for this DB manager")
