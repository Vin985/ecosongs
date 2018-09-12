import os

from utils.wacconverter import WacConverter

from PySide2.QtCore import QObject, Signal


class FileHandler(QObject, WacConverter):
    logging = Signal(str)
    update_progress = Signal(int)

    def __init__(self, root="", dest=""):
        QObject.__init__(self)
        WacConverter.__init__(self, root, dest)

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

    def files_to_wav(self, files):
        # self.open_archive()
        self.apply_to_files(files, self.file_to_wav)
        # self.close_archive()
        # nfiles = len(self.files)
        # current = 0
        # for fn in self.files:
        #     if self.thread().isInterruptionRequested():
        #         return (1)
        #     self.file_to_wav(fn)
        #     current += 1
        #     self.update_progress.emit(current/nfiles * 100)

    def remove_wac(self, files):
        self.apply_to_files(files, os.remove)
        # nfiles = len(self.files)
        # current = 0
        # for fn in self.files:
        #     if self.thread().isInterruptionRequested():
        #         return (1)
        #     os.remove(fn)
        #     current += 1
        #     self.update_progress.emit(current/nfiles * 100)

    def rename_files(self, old, new):
        self.apply_to_files(zip(old, new), self.rename_file_tuple)

    def rename_file_tuple(self, tuple):
        os.rename(*tuple)
        # nfiles = len(self.files)
        # current = 0
        # for fn in self.files:
        #     if self.thread().isInterruptionRequested():
        #         return (1)
        #     os.remove(fn)
        #     current += 1
        #     self.update_progress.emit(current/nfiles * 100)

    def log(self, text):
        self.logging.emit(text)
