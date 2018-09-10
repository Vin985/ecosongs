import os

from utils.wacconverter import WacConverter

from PySide2.QtCore import QObject, Signal


class FileHandler(QObject, WacConverter):
    logging = Signal(str)
    update_progress = Signal(int)

    def __init__(self, root="", dest="", files=[]):
        QObject.__init__(self)
        WacConverter.__init__(self, root, dest, files)

    def files_to_wav(self):
        nfiles = len(self.files)
        current = 0
        for fn in self.files:
            if self.thread().isInterruptionRequested():
                return (1)
            self.file_to_wav(fn)
            current += 1
            self.update_progress.emit(current/nfiles * 100)

    def remove_wac(self):
        nfiles = len(self.files)
        current = 0
        for fn in self.files:
            if self.thread().isInterruptionRequested():
                return (1)
            os.remove(fn)
            current += 1
            self.update_progress.emit(current/nfiles * 100)

    def log(self, text):
        self.logging.emit(text)
