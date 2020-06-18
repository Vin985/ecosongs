import time

from PySide2.QtCore import Qt, QThread, Signal, Slot
from PySide2.QtWidgets import QDialog

from gui.widgets.dialogs.ui.progressdialog_ui import Ui_ProgressDialog


class ProgressDialog(QDialog, Ui_ProgressDialog):

    cancelling = Signal()
    launch_task = Signal()
    save_results = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.started = 0
        self.worker_thread = QThread()
        self._worker = None
        self.duration = 0
        self.options_widget = None
        self.btn_close.hide()
        self.log_message = ""
        self.lbl_message.setHidden(True)
        self.lbl_error.setHidden(True)
        self.adjustSize()

    def init_options_widget(self, widget):
        self.options_widget = widget
        self.content_layout.addWidget(self.options_widget)

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
            self.launch_task.connect(self.worker.start_task, type=Qt.QueuedConnection)
            self.worker.computing.connect(
                self.computing, type=Qt.BlockingQueuedConnection
            )
            self.worker.progressed.connect(
                self.update_progress, type=Qt.BlockingQueuedConnection
            )

            self.worker.logging.connect(self.log, type=Qt.BlockingQueuedConnection)
            self.cancelling.connect(self.worker.cancel_tasks, type=Qt.DirectConnection)

            self.worker.computing_done.connect(
                self.computing_done, type=Qt.BlockingQueuedConnection
            )
            self.worker.results_saved.connect(
                self.results_saved, type=Qt.BlockingQueuedConnection
            )
            self.worker.done.connect(self.task_done, type=Qt.BlockingQueuedConnection)
            self.worker.error.connect(self.log_error)

    def init_thread(self):
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.finished.connect(self.worker.deleteLater)
        self.finished.connect(self.worker_thread.quit)
        self.destroyed.connect(self.worker_thread.quit)
        self.worker_thread.start()

    @Slot()
    def start(self):
        print("clicking start")
        self.init_task()
        self.launch_task.emit()
        self.started = time.time()

    @Slot()
    def cancel(self):
        if self.started:
            self.cancelling.emit()
            self.started = 0
        else:
            self.reject()

    @Slot()
    def close_dialog(self):
        self.accept()

    @Slot()
    def computing(self):
        self.reset_progress()
        self.btn_start.setEnabled(False)
        self.log("Computing...")

    def computing_done(self):
        self.update_progress(100)
        self.duration = time.time() - self.started
        self.log_message = self.duration_message()
        self.log()

    def duration_message(self):
        text = "Performed task in %0.3f seconds" % (self.duration)
        if self.worker.options["save"]:
            text += ". Saving results, please wait..."
        return text

    @Slot()
    def update_progress(self, progress):
        self.progress_bar.setValue(progress)

    @Slot()
    def log(self, text=None):
        self.lbl_message.setHidden(False)
        text = text or self.log_message
        self.lbl_message.setText(text)

    @Slot()
    def log_error(self, text=None):
        self.lbl_error.setHidden(False)
        text = text or self.log_message
        self.lbl_error.setText(text)

    @Slot()
    def task_done(self):
        self.btn_close.show()
        self.btn_start.hide()
        self.btn_cancel.hide()
        self.log_message += " Done!"
        self.log()

    def results_saved(self):
        pass

    def init_task(self):
        self.worker.options = self.options_widget.get_options()

    def reset_progress(self):
        self.progress_bar.setEnabled(True)
        self.progress_bar.setValue(0)
