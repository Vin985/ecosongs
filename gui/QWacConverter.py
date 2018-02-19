import os
import re
import time

from utils.wacconverter import WacConverter
from wac2wav import wac2wav

from PySide2 import QtCore


class QWacConverter(WacConverter, QtCore.QThread):
    converting = QtCore.Signal(str, bool)
    started = QtCore.Signal()

    def __init__(self, qconsole, root="", dest="", files=[]):
        QtCore.QThread.__init__(self)
        super().__init__(root, dest, files)
        self.console = qconsole

    def __del__(self):
        self.wait()

    def run(self):
        self.started.emit()
        self.files_to_wav()

    def files_to_wav(self):
        for fn in self.files:
            if self.isInterruptionRequested():
                return (1)
            self.file_to_wav(fn)

    def log(self, text):
        self.converting.emit(text, True)
