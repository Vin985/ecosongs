import logging
import time

import pandas as pd
from PySide2.QtCore import QObject, Signal, Slot

import analysis.detection.song_detector as song_detector
import analysis.indexes as indexes
from gui.threads.ParallelWorker import ParallelWorker


class ThreadWorker(QObject, ParallelWorker):
    logging = Signal(str)
    progressed = Signal(int)
    computing = Signal()
    done = Signal()

    def __init__(self):
        QObject.__init__(self)
        ParallelWorker.__init__(self)

    def log(self, text):
        self.logging.emit(text)

    @Slot()
    def cancel_tasks(self):
        print("in cancel tasks")
        self.terminate_tasks()
        self.results = pd.DataFrame(self.results)
        self.done.emit()
        self.thread().requestInterruption()

    def update_progress(self, step=1):
        if self.with_progress:
            self.progress += step
            print("progress: " + str(self.progress))
            self.progressed.emit(int(self.progress/self.nitems * 100))
