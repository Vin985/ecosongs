import time

from PySide2.QtCore import Qt, QThread, Slot
from PySide2.QtWidgets import QDialog

from gui.widgets.audio.QAudioAnalyzer import QAudioAnalyzer


class AnalyzerDialog(QDialog):
    def __init__(self, recordings):
        super().__init__()
        self.audio_analyzer = QAudioAnalyzer(recordings)
        self.worker_thread = QThread()
        self.started = 0
        self.init_thread()

    def link_events(self):
        self.audio_analyzer.progressed.connect(self.update_progress,
                                               type=Qt.BlockingQueuedConnection)
        self.audio_analyzer.logging.connect(self.log, type=Qt.BlockingQueuedConnection)
        self.audio_analyzer.computing.connect(self.computing, type=Qt.BlockingQueuedConnection)
        self.audio_analyzer.done.connect(self.process_results, type=Qt.BlockingQueuedConnection)
        # Navigation: change page when icon is clicked
        # self.menu_categories.currentRowChanged.connect(self.menu_pages.setCurrentIndex)

    def init_thread(self):
        self.audio_analyzer.moveToThread(self.worker_thread)
        self.worker_thread.finished.connect(self.audio_analyzer.deleteLater)
        self.finished.connect(self.worker_thread.quit)
        self.destroyed.connect(self.worker_thread.quit)
        self.worker_thread.start()

    @Slot()
    def update_progress(self, progress):
        print(progress)
        self.progress_bar.setValue(progress)

    @Slot()
    def log(self, text):
        print(text)

    @Slot()
    def computing(self):
        pass

    @Slot()
    def process_results(self):
        self.btn_close.show()
        self.btn_start.hide()
        self.btn_cancel.hide()
        self.log("Processed %d recordings in %0.3f seconds" %
                 (len(self.audio_analyzer.recordings), (time.time() - self.started)))

    @Slot()
    def close_dialog(self):
        self.accept()
