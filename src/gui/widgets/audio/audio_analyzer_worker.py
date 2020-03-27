
from PySide2.QtCore import Slot

import analysis.detection.song_detector as song_detector
import analysis.indexes as indexes
from gui.threads.thread_worker import ThreadWorker


class AudioAnalyzerWorker(ThreadWorker):

    def __init__(self, recordings):
        super().__init__()
        self.recordings = recordings or []

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
        self.done.emit()
