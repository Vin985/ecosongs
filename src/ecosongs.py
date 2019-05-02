import logging
import sys
import os

from PySide2.QtWidgets import QApplication

import db.dbutils as dbutils
from analysis.image import ImageGenerator
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

    def load_recordings(self, indexes, spec_opts=None):
        settings = Settings()
        spec_opts = spec_opts or settings.spectrogram_settings()
        return self.tables.recordings.load_recordings(indexes, spec_opts)

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
                {"database": "ecosongs", "db_type": "feather", "path": "db"})

        self.dbmanager = dbutils.get_db_manager(**db_opts)
        self.imgen = ImageGenerator(settings.image_settings())
        self.tables = TableManager(self.dbmanager)


if __name__ == '__main__':
    import sys
    # logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    app = Ecosongs(sys.argv)
    ui = EcosongsUI()
    ui.showMaximized()
    sys.exit(app.exec_())
