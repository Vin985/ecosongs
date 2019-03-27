import time

from PySide2.QtCore import Qt, QThread, Signal, Slot
from PySide2.QtWidgets import QDialog

from gui.widgets.audio.QAudioAnalyzer import QAudioAnalyzer


class AnalyzerDialog(QDialog):

    cancelling = Signal()

    def __init__(self, recordings, parent=None):
        super().__init__(parent=parent)
        self.audio_analyzer = QAudioAnalyzer(recordings)
        self.worker_thread = QThread()
        self.started = 0
        self.init_thread()

    def link_events(self):
        self.btn_start.clicked.connect(self.start)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_close.clicked.connect(self.close_dialog)

        self.audio_analyzer.progressed.connect(self.update_progress,
                                               type=Qt.BlockingQueuedConnection)
        self.audio_analyzer.logging.connect(self.log, type=Qt.BlockingQueuedConnection)
        self.audio_analyzer.computing.connect(self.computing, type=Qt.BlockingQueuedConnection)

        self.audio_analyzer.done.connect(self.process_results)

        self.cancelling.connect(self.audio_analyzer.cancel_tasks, type=Qt.DirectConnection)
        # Navigation: change page when icon is clicked
        # self.menu_categories.currentRowChanged.connect(self.menu_pages.setCurrentIndex)

    def init_thread(self):
        self.audio_analyzer.moveToThread(self.worker_thread)
        self.worker_thread.finished.connect(self.audio_analyzer.deleteLater)
        self.finished.connect(self.worker_thread.quit)
        self.destroyed.connect(self.worker_thread.quit)
        self.worker_thread.start()

    @Slot()
    def cancel(self):
        if self.started:
            self.cancelling.emit()
        else:
            self.reject()

    def reset_progress(self):
        self.progress_bar.setEnabled(True)
        self.progress_bar.setValue(0)

    @Slot()
    def computing(self):
        self.reset_progress()
        self.btn_start.setEnabled(False)

    @Slot()
    def update_progress(self, progress):
        print(progress)
        self.progress_bar.setValue(progress)

    @Slot()
    def log(self, text):
        self.lbl_progress.setText(text)

    @Slot()
    def process_results(self):
        self.btn_close.show()
        self.btn_start.hide()
        self.btn_cancel.hide()
        self.update_progress(100)
        # self.progress_bas.setEnabled(False)
        self.log("Processed %d recordings in %0.3f seconds" %
                 (len(self.audio_analyzer.recordings), (time.time() - self.started)))

    @Slot()
    def close_dialog(self):
        self.accept()

    @Slot()
    def start(self):
        pass
