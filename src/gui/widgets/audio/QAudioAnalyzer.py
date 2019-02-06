from gui.threads.QPoolWorker import QPoolWorker
import analysis.indexes as indexes
from PySide2.QtCore import Signal


class QAudioAnalyzer(QPoolWorker):

    computing_index = Signal(str)

    def __init__(self):
        super().__init__()

    def compute_index(self, recordings, index_type, *args, **kwargs):
        # self.computing_index.emit("")
        res = self.apply_with_progress(recordings,
                                       indexes.compute_index,
                                       index_type=index_type,
                                       *args, **kwargs)
        return res
