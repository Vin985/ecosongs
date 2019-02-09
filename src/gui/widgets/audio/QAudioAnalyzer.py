import time

import analysis.detection.song_detector as song_detector
from PySide2.QtCore import Signal

import analysis.indexes as indexes
from gui.threads.QParallelWorker import QParallelWorker

from analysis.detection.lib.tf_classifier import HOP_LENGTH, TFClassifier


class QAudioAnalyzer(QParallelWorker):

    computing_index = Signal(str)

    def __init__(self):
        super().__init__()

    def compute_index(self, recordings, index_type, *args, spec_opts=None, **kwargs):
        # self.computing_index.emit("")
        start = time.time()
        # TODO: change initializer to be able to use more indexes
        # TODO: put chunksize as option
        chunksize = int(len(recordings)/20)
        if chunksize < 1:
            chunksize = 1
        res = self.map(recordings,
                       indexes.mp_compute_index_chunk,
                       initializer=indexes.mp_initialize_index,
                       initargs=(index_type, spec_opts),
                       multiprocess=True,
                       chunksize_percent=20,
                       *args, **kwargs)
        end = time.time()
        print("Action took: " + str(end - start))
        return res

    def detect_songs(self, recordings, options, weight_file, detection_options,
                     *args, **kwargs):
        chunksize = int(len(recordings)/20)
        if chunksize < 1:
            chunksize = 1
        res = self.map(recordings,
                       song_detector.mp_detect_songs,
                       initializer=song_detector.mp_initialize_detector,
                       initargs=(options, weight_file, detection_options),
                       multiprocess=True,
                       chunksize=chunksize,
                       *args, **kwargs)
        return res

    def detect_songs2(self, recordings, options, weight_file, detection_options,
                      *args, **kwargs):
        chunksize = int(len(recordings)/20)
        if chunksize < 1:
            chunksize = 1
        classifier = TFClassifier(options, weight_file)
        res = self.map(recordings,
                       song_detector.detect_songs,
                       classifier=classifier,
                       detection_options=detection_options,
                       * args, **kwargs)
        return res
