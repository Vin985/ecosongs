
import pandas as pd

from PySide2.QtCore import qApp, Slot

import analysis.detection.song_detector as song_detector
import analysis.indexes as indexes
from gui.threads.thread_worker import ThreadWorker


class AudioAnalyzerWorker(ThreadWorker):

    ANALYSIS = {"ACI": "compute_index",
                "detection": "detect_songs"}

    def __init__(self, recordings):
        super().__init__()
        self.recordings = recordings or []

    def perform_task(self):
        if self.options["analysis"]:
            func = getattr(self, self.ANALYSIS[self.options["analysis"]])
            func()

    def compute_index(self):
        index_type = self.options["index_type"]
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
        if self.recordings:
            self.map(self.recordings, function, *args, **kwargs)

    def save_results(self):
        res = self.results
        if res and self.options["save"]:
            events = pd.concat(res)
            activity_table = qApp.tables.activity_predictions
            activity_table.add(events, save=True,
                               replace=self.options["overwrite"])
