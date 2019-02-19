import logging

from PySide2.QtWidgets import QApplication

import db.dbutils as dbutils
from analysis.image import ImageGenerator
from audio.recording import RecordingTable
from db.feathermanager import FeatherManager
from gui.ecosongsUI import EcosongsUI
from gui.utils.settings import Settings


class Ecosongs(QApplication):

    def get_recordings(self, df=True):
        if df:
            return self.recordings.df
        return self.recordings.recordings

    def load_recordings(self, indexes, spec_opts=None):
        settings = Settings()
        spec_opts = spec_opts or settings.spectrogram_settings()
        return self.recordings.load_recordings(indexes, spec_opts)

    def __init__(self, argv):
        super().__init__(argv)
        self.setOrganizationName("ecosongs")
        self.setOrganizationDomain("CRCEco")
        self.setApplicationName("ecosongs")
        settings = Settings()
        self.dbmanager = dbutils.get_db_manager(database=settings.db_name,
                                                type=settings.db_type,
                                                path=settings.db_path)
        # TODO: replace everything with feather?
        self.feather_manager = FeatherManager("db/feather")
        self.recordings = RecordingTable(dbmanager=self.dbmanager)
        self.imgen = ImageGenerator(settings.image_settings())


if __name__ == '__main__':
    import sys
    # logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    app = Ecosongs(sys.argv)
    ui = EcosongsUI()
    ui.showMaximized()
    sys.exit(app.exec_())
