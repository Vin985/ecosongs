import logging
import sys

from PySide2.QtWidgets import QApplication

from db import dbutils
from db.tablemanager import TableManager
from gui.ecosongsUI import EcosongsUI
from gui.utils.settings import Settings

# # print(os.environ['LD_LIBRARY_PATH'])
#
# print(sys.version)
# print(sys.path)


class Ecosongs(QApplication):

    def get_recordings(self, df=True):
        if df:
            return self.tables.recordings.df
        return self.tables.recordings.recordings

    def load_recordings(self, indexes):
        return self.tables.recordings.load_recordings(indexes)

    def __init__(self, argv):
        super().__init__(argv)
        self.setOrganizationName("ecosongs")
        self.setOrganizationDomain("CRCEco")
        self.setApplicationName("ecosongs")
        settings = Settings()

        db_opts = settings.group_to_dict("database")
        if not db_opts:
            print("adding database defaults")
            db_opts.update(
                {"database": "ecosongs", "db_type": "feather", "path": "/mnt/win/UMoncton/Doctorat/dev/ecosongs/src/db"})

        self.dbmanager = dbutils.get_db_manager(**db_opts)
        self.tables = TableManager(self.dbmanager)


if __name__ == '__main__':

    # logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    app = Ecosongs(sys.argv)
    ui = EcosongsUI()
    ui.showMaximized()
    sys.exit(app.exec_())
