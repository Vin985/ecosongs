#!/usr/bin/env python
import db.dbutils as dbutils
from analyse.image import ImageGenerator
from analyse.spectrogram import SpectrogramGenerator
from audio.recording import Recordings
from gui.ecosongsUI import EcosongsUI
from gui.utils.settings import Settings
from PySide2.QtWidgets import QApplication


class Ecosongs(QApplication):

    def save_data(self, table, data, *args, **kwargs):
        self.dbmanager.save_data(table, data, *args, **kwargs)

    def get_recordings(self):
        return self.recordings.df

    def __init__(self, argv):
        super(self.__class__, self).__init__(argv)
        self.setOrganizationName("ecosongs")
        self.setOrganizationDomain("CRCEco")
        self.setApplicationName("ecosongs")
        settings = Settings()
        self.dbmanager = dbutils.get_db_manager(database=settings.db_name,
                                                type=settings.db_type,
                                                path=settings.db_path)
        self.recordings = Recordings(dbmanager=self.dbmanager)
        self.specgen = SpectrogramGenerator(settings.spectrogram_settings())
        self.imgen = ImageGenerator(settings.image_settings())


if __name__ == '__main__':
    import sys
    app = Ecosongs(sys.argv)
    ui = EcosongsUI()
    ui.showMaximized()
    sys.exit(app.exec_())
