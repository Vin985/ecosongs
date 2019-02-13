import logging
import time

import pandas as pd
from PySide2.QtCore import QObject, Signal, Slot

import analysis.detection.song_detector as song_detector
import analysis.indexes as indexes
from gui.threads.ParallelWorker import ParallelWorker


class QAudioAnalyzer(QObject, ParallelWorker):
    logging = Signal(str)
    progressed = Signal(int)
    computing = Signal()
    done = Signal()

    def __init__(self, recordings):
        QObject.__init__(self)
        ParallelWorker.__init__(self)
        self.recordings = recordings or []

    def log(self, text):
        self.logging.emit(text)

    @Slot()
    def cancel_tasks(self):
        print("in cancel tasks")
        self.terminate_tasks()
        self.results = pd.DataFrame(self.results)
        self.done.emit()

    def update_progress(self, step=1):
        if self.with_progress:
            self.progress += step
            print("progress: " + str(self.progress))
            self.progressed.emit(int(self.progress/self.nitems * 100))

    @Slot()
    def compute_index(self, index_type):
        self.perform_analysis(indexes.mp_compute_index_chunk,
                              initializer=indexes.mp_initialize_index,
                              initargs=(index_type, self.options["initargs"]))

    @Slot()
    def detect_songs(self):
        self.perform_analysis(song_detector.mp_detect_songs_chunk,
                              initializer=song_detector.mp_initialize_detector,
                              initargs=self.options["initargs"])

    def perform_analysis(self, function, *args, **kwargs):
        self.results = []
        self.computing.emit()
        if self.recordings:
            # TODO: put chunksize as option
            self.map(self.recordings, function, *args, **kwargs)
        self.results = pd.DataFrame(self.results)
        self.done.emit()
