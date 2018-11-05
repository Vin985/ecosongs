
from PySide2.QtCore import QObject, Signal


class QThreadWorker(QObject):
    logging = Signal(str)
    update_progress = Signal(int)

    def __init__(self):
        QObject.__init__(self)

    def log(self, text):
        self.logging.emit(text)

    def apply_with_progress(self, collection, func, *args, **kwargs):
        nitems = len(collection)
        current = 0
        for item in collection:
            if self.thread().isInterruptionRequested():
                return (1)
            func(item, *args, **kwargs)
            current += 1
            self.update_progress.emit(current/nitems * 100)
