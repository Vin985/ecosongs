from utils.wacconverter import WacConverter

from PySide2 import QtCore


class QWCThread(QtCore.QThread, WacConverter):
    converting = QtCore.Signal(str, bool)
    started = QtCore.Signal()

    def __init__(self, root="", dest="", files=[]):
        QtCore.QThread.__init__(self)
        super(WacConverter, self).__init__().__init__(root, dest, files)

    def __del__(self):
        self.wait()

    def run(self):
        self.started.emit()
        self.open_archive()
        self.files_to_wav()
        self.close_archive()
        self.remove_wac()

    def files_to_wav(self):
        for fn in self.files:
            if self.isInterruptionRequested():
                return (1)
            self.file_to_wav(fn)

    def log(self, text):
        self.converting.emit(text, False)
