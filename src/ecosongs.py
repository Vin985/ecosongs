#!/usr/bin/env python
import pandas as pd

from gui.ecosongsUI import EcosongsUI
# from PySide2.QtCore import QFile, QTextStream
from PySide2.QtWidgets import QApplication
from sqlalchemy import create_engine


class Ecosongs(QApplication):
    # TODO: externalize using persistence class
    def load_data(self):
        # self.data = RecordingModel.select()
        # self.recordings = pd.read_sql_table("recordings", self.dbengine, parse_dates={"date": "%Y-%m-%d %H:%M:%S"})
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
        self.recordings = pd.DataFrame()
        self.dbengine = create_engine("sqlite:///db/ecosongs.db")
        self.storage = pd.HDFStore('db/ecosongs.h5')


if __name__ == '__main__':
    import sys
    app = Ecosongs(sys.argv)

    # f = QFile("gui/resources/qss/custom.qss")
    # f.open(QFile.ReadOnly)
    # res = QTextStream(f).readAll()
    # print(res)
    # app.setStyleSheet(res)
    ui = EcosongsUI()  # We set the form to be our ExampleApp (design)
    ui.showMaximized()
    sys.exit(app.exec_())
