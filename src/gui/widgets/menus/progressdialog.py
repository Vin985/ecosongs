import time

from PySide2.QtCore import Qt, QThread, Signal, Slot
from PySide2.QtWidgets import QDialog

from gui.widgets.menus.ui.progressdialog_ui import Ui_ProgressDialog


class ProgressDialog(QDialog, Ui_ProgressDialog):

    cancelling = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.started = 0
        self.worker_thread = QThread()
        self._worker = None
        self.duration = 0

    @property
    def worker(self):
        return self._worker

    @worker.setter
    def worker(self, worker):
        if worker:
            self._worker = worker
            self.init_thread()

    def link_events(self):
        self.btn_start.clicked.connect(self.start)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_close.clicked.connect(self.close_dialog)

        if self.worker:
            self.worker.progressed.connect(self.update_progress,
                                           type=Qt.BlockingQueuedConnection)
            self.worker.logging.connect(
                self.log, type=Qt.BlockingQueuedConnection)
            self.worker.computing.connect(
                self.computing, type=Qt.BlockingQueuedConnection)

            self.worker.done.connect(self.process_results)

            self.cancelling.connect(
                self.worker.cancel_tasks, type=Qt.DirectConnection)

    def init_thread(self):
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.finished.connect(self.worker.deleteLater)
        self.finished.connect(self.worker_thread.quit)
        self.destroyed.connect(self.worker_thread.quit)
        self.worker_thread.start()

    @Slot()
    def cancel(self):
        if self.started:
            self.cancelling.emit()
            self.started = 0
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
        self.duration = (time.time() - self.started)

    @Slot()
    def close_dialog(self):
        self.accept()

    @Slot()
    def start(self):
        pass
