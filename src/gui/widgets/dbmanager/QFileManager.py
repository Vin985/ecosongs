
import os
import time

import pandas as pd
from PySide2.QtCore import QObject, Signal
from PySide2.QtGui import qApp

from audio.recording import Recording
from gui.threads.ParallelWorker import ParallelWorker
from gui.utils.settings import Settings
from utils.filemanager import FileManager


class QFileManager(QObject, ParallelWorker, FileManager):
    filesLoaded = Signal()

    converting = Signal()
    removing = Signal()
    renaming = Signal()
    saving = Signal()
    tosave = Signal()
    logging = Signal(str)
    progressed = Signal(int)

    def log(self, text):
        self.logging.emit(text)

    def update_progress(self, step=1):
        if self.with_progress:
            self.progress += step
            print("progress: " + str(self.progress))
            self.progressed.emit(int(self.progress / self.nitems * 100))

    def __init__(self):
        QObject.__init__(self)
        ParallelWorker.__init__(self)
        settings = Settings()
        FileManager.__init__(self, sites=settings.sites_path)
        self.options["multiprocess"] = False

    def import_files(self):
        self.converting.emit()
        self.files_to_wav()
        self.remove_wac()
        self.rename_files()
        self.save_recordings()

    def files_loaded(self):
        # TODO: change to use persistence model
        # qApp.save_data("recordings", self.file_infos, format="t")
        self.filesLoaded.emit()

    def files_to_wav(self):
        self.converting.emit()
        # self.open_archive()
        self.map(self.to_wav, self.file_to_wav)
        # self.close_archive()

    def remove_wac(self):
        self.removing.emit()
        return
        self.map(self.to_wav, os.remove)

    def rename_files(self, create_links=True):
        # TODO: add checkbox test in option files
        self.renaming.emit()
        if self.options["create_links"]:
            self.create_links()
        return
        cols = self.file_infos.loc[:, ["path", "old_name", "name"]]
        new_paths = [self.get_new_path(*row) for row in cols.itertuples(index=False)]
        tmp = list(zip(self.file_infos.loc[:, "path"], new_paths))
        self.map(tmp, self.rename_file_tuple)

    def save_recordings(self):
        self.saving.emit()
        print("saving")
        # TODO: append to existing recordings
        to_save = self.file_infos.loc[:, self.file_infos.columns.intersection(Recording.COLUMNS)]
        to_save["date"] = pd.to_datetime(to_save["date"])
        self.to_save = to_save
        self.tosave.emit()
        # TODO: check duplicates
        # qApp.recordings.append(to_save, save=True)

    def get_new_path(self, path, old, new):
        new_path = path.replace(old, new)
        if self.dest_dir:
            new_path = path.replace(self.root_dir, self.dest_dir)
        return(new_path)
