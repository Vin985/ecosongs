import os

import feather

from db.dbmanager import DBManager


class FeatherManager(DBManager):
    def __init__(self, path):
        super().__init__()
        self.db_root = path + "/"

    def get_table(self, table):
        return feather.read_dataframe(self.db_root + table + ".feather")

    def save(self, table, data, update=False):
        if not os.path.exists(self.db_root):
            os.makedirs(self.db_root)
        data.to_feather(self.db_root + table + ".feather")
