
from PySide2.QtCore import Slot

from gui.threads.thread_worker import ThreadWorker


class SensitivityWorker(ThreadWorker):
    def __init__(self, recordings, tags, predictions):
        super().__init__()
        self.recordings = recordings
        self.tags = tags
        self.predictions = predictions

        # self.perform_analysis(indexes.mp_compute_index_chunk,
        #                       initializer=indexes.mp_initialize_index,
        #                       initargs=(index_type, self.options["initargs"]))

    # @Slot()
    # def detect_songs(self):
    #     self.perform_analysis(song_detector.mp_detect_songs_chunk,
    #                           initializer=song_detector.mp_initialize_detector,
    #                           initargs=self.options["initargs"])
    @Slot()
    def perform_analysis(self):
        print("launching sensitivity analysis")
        print(self.options)

        # self.results = []
        # self.computing.emit()
        # if self.recordings:
        #     # TODO: put chunksize as option
        #     self.map(self.recordings, function, *args, **kwargs)
        # # self.results = pd.DataFrame(self.results)
        # self.done.emit()

    # def test(self, result):
    #     print("in test callback")
    #     print(result)
    #     return result
