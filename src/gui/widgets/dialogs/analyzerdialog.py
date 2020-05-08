
from PySide2.QtCore import Slot

from gui.widgets.dialogs.workers.audio_analyzer_worker import AudioAnalyzerWorker
from gui.widgets.dialogs.progressdialog import ProgressDialog


class AnalyzerDialog(ProgressDialog):

    def __init__(self, recordings, parent=None):
        super().__init__(parent=parent)
        self.worker = AudioAnalyzerWorker(recordings)

    @Slot()
    def process_results(self):
        super().process_results()
        # self.progress_bas.setEnabled(False)
        nrecs = len(self.worker.recordings)
        self.log("Processed %d recordings in %0.3f seconds (%0.3fs/recording)" %
                 (nrecs, self.duration, self.duration / nrecs))
