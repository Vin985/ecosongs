
import pandas as pd
import time
import os

from PySide2.QtCore import Slot

import analysis.detection.song_detector as song_detector
import analysis.indexes as indexes
from gui.threads.thread_worker import ThreadWorker


class AudioAnalyzerWorker(ThreadWorker):

    ANALYSIS = {"ACI": "compute_index",
                "detection": "detect_songs"}

    def __init__(self, recordings):
        super().__init__()
        self.recordings = recordings or []
        self.session_id = time.time()
        self.result_count = 0

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
        save_intermediate_results = self.options.get(
            "save_intermediate_results", True)
        callback = None
        if save_intermediate_results:
            callback = self.save_intermediate
        self.perform_analysis(song_detector.mp_detect_songs_chunk,
                              initializer=song_detector.mp_initialize_detector,
                              initargs=self.options["initargs"],
                              callback=callback)

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

    def save_intermediate(self, results):
        if results:
            print("saving intermediate results")
            db_path = qApp.dbmanager.db_root
            tmp_path = os.path.join(db_path, str(self.session_id))
            res = pd.concat(results)
            res.reset_index(inplace=True)
            if not os.path.exists(tmp_path):
                os.makedirs(tmp_path)
            res.to_feather(os.path.join(
                tmp_path, "tmp_result_" + str(self.result_count) + ".feather"))
            self.result_count += 1
        return results
