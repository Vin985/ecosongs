import logging

import db.dbutils as dbutils
from analyse.image import ImageGenerator
from audio.recording import RecordingTable
from gui.ecosongsUI import EcosongsUI
from gui.utils.settings import Settings
from PySide2.QtWidgets import QApplication


class Ecosongs(QApplication):

    def get_recordings(self, df=True):
        if df:
            return self.recordings.df
        else:
            return self.recordings.recordings

    def load_recordings(self, indexes):
        return self.recordings.load_recordings(indexes)

    def __init__(self, argv):
        super(self.__class__, self).__init__(argv)
        self.setOrganizationName("ecosongs")
        self.setOrganizationDomain("CRCEco")
        self.setApplicationName("ecosongs")
        settings = Settings()
        self.dbmanager = dbutils.get_db_manager(database=settings.db_name,
                                                type=settings.db_type,
                                                path=settings.db_path)
        self.recordings = RecordingTable(dbmanager=self.dbmanager)
        self.imgen = ImageGenerator(settings.image_settings())


if __name__ == '__main__':
    import sys
    #logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    app = Ecosongs(sys.argv)
    ui = EcosongsUI()
    ui.showMaximized()
    sys.exit(app.exec_())
