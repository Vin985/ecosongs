#!/usr/bin/env python
import pandas as pd

from gui.ecosongsUI import EcosongsUI
from PySide2.QtWidgets import QApplication


class Ecosongs(QApplication):
    # TODO: externalize using persistence class
    def load_data(self):
        try:
            self.recordings = self.storage["recordings"]
        except KeyError:
            self.recordings

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
        self.storage = pd.HDFStore('db/ecosongs.h5')


if __name__ == '__main__':
    import sys
    app = Ecosongs(sys.argv)
    ui = EcosongsUI()
    ui.showMaximized()
    sys.exit(app.exec_())
