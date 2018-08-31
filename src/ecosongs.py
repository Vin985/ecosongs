#!/usr/bin/env python
import pandas as pd

import db.dbutils as dbutils
from gui.ecosongsUI import EcosongsUI
from gui.utils.settings import Settings
from PySide2.QtWidgets import QApplication


class Ecosongs(QApplication):
    # TODO be more specific in name functions
    def load_data(self):
        try:
            self.recordings = self.dbmanager.get_table("recordings")
        except KeyError:
            self.recordings

    def save_data(self, table, data, *args, **kwargs):
        self.dbmanager.save_data(table, data, *args, **kwargs)

    def get_recordings(self):
        if self.recordings.empty:
            self.load_data()
        return self.recordings

    def __init__(self, argv):
        super(self.__class__, self).__init__(argv)
        self.setOrganizationName("ecosongs")
        self.setOrganizationDomain("CRCEco")
        self.setApplicationName("ecosongs")
        self.recordings = pd.DataFrame()
        settings = Settings()
        self.dbmanager = dbutils.get_db_manager(database=settings.db_name,
                                                type=settings.db_type,
                                                path=settings.db_path)


if __name__ == '__main__':
    import sys
    app = Ecosongs(sys.argv)
    ui = EcosongsUI()
    ui.showMaximized()
    sys.exit(app.exec_())
