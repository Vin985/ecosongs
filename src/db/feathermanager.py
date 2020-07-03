import pathlib
import pandas as pd

import feather

from db.dbmanager import DBManager


class FeatherManager(DBManager):

    NAME = "feather"
    FILE_EXTENSION = ".feather"

    def __init__(self, path, **kwargs):
        super().__init__()
        self.db_root = path + "/feather/"

    def get_table(self, table=None, path=None):
        if path is None and table is None:
            raise AttributeError("Please provide either table name or path to table")
        if path is None:
            path = self.db_root + table + self.FILE_EXTENSION
        path = pathlib.Path(path)
        if path.exists():
            data = feather.read_dataframe(path)
        else:
            data = pd.DataFrame()
        return data

    def save(self, table, data):
        self.export_table(data, self.db_root + table + self.FILE_EXTENSION)
        # if not os.path.exists(self.db_root):
        #     os.makedirs(self.db_root)
        # data.reset_index(inplace=True, drop=True)
        # data.to_feather(self.db_root + table + self.FILE_EXTENSION)

    def update(self, table, data):
        self.save(table, data)

    def delete(self, table, data):
        raise NotImplementedError("Function not implemented for this DB manager")

    def export_table(self, data, dest_path):
        dest_path = pathlib.Path(dest_path)
        if not dest_path.parent.exists():
            dest_path.parent.mkdir(parents=True)
        data.reset_index(inplace=True, drop=True)
        data.to_feather(dest_path)
