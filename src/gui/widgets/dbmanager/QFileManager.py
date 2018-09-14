
import os

import pandas as pd
from utils.filemanager import FileManager

from audio.recording import Recording
from gui.utils.settings import Settings
from PySide2.QtCore import QObject, Signal
from PySide2.QtGui import qApp


class QFileManager(QObject, FileManager):
    logging = Signal(str, bool)
    filesLoaded = Signal()
    logging = Signal(str)
    update_progress = Signal(int)

    def __init__(self):
        QObject.__init__(self)
        settings = Settings()
        FileManager.__init__(self, sites=settings.sites_path)

    def log(self, text):
        self.logging.emit(text)

    def files_loaded(self):
        # TODO: change to use persistence model
        # qApp.save_data("recordings", self.file_infos, format="t")
        self.filesLoaded.emit()

    def apply_with_progress(self, collection, func, *args, **kwargs):
        print(collection)
        nitems = len(collection)
        current = 0
        for item in collection:
            if self.thread().isInterruptionRequested():
                return (1)
            func(item, *args, **kwargs)
            current += 1
            self.update_progress.emit(current/nitems * 100)

    def files_to_wav(self):
        # self.open_archive()
        self.apply_with_progress(self.to_wav, self.file_to_wav)
        # self.close_archive()

    def remove_wac(self):
        self.apply_with_progress(self.to_wav, os.remove)

    def rename_files(self):
        cols = self.file_infos.loc[:, ["path", "old_name", "name"]]
        new_paths = [self.get_new_path(*row) for row in cols.itertuples(index=False)]
        tmp = list(zip(self.file_infos.loc[:, "path"], new_paths))
        print(tmp)
        self.apply_with_progress(tmp,
                                 self.rename_file_tuple)

    def save_recordings(self):
        # TODO: append to existing recordings
        to_save = self.file_infos.loc[:, Recording.COLUMNS]
        to_save["date"] = pd.to_datetime(to_save["date"])
        qApp.save_data("recordings", to_save, format="table")

    def get_new_path(self, path, old, new):
        new_path = path.replace(old, new)
        if self.dest_dir:
            new_path = path.replace(self.root_dir, self.dest_dir)
        return(new_path)
