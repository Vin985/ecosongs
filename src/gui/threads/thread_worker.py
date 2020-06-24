import traceback
import pandas as pd
from PySide2.QtCore import QObject, Signal, Slot

from gui.threads.parallel_worker import ParallelWorker


class ThreadWorker(QObject, ParallelWorker):
    logging = Signal(str)
    progressed = Signal(int)
    computing = Signal()
    computing_done = Signal()
    done = Signal()
    error = Signal(str)
    results_saved = Signal()
    cancelled = Signal()

    def __init__(self):
        QObject.__init__(self)
        ParallelWorker.__init__(self)
        print(self.thread())

    def log(self, text):
        self.logging.emit(text)

    def start_task(self):
        try:
            self.results = []
            self.computing.emit()
            self.perform_task()
            self.computing_done.emit()
            if self.options["save"]:
                self.save_results()
                self.results_saved.emit()
        except Exception:
            print(traceback.format_exc())
            self.error.emit(traceback.format_exc())
        self.done.emit()

    @Slot()
    def cancel_tasks(self):
        print("in cancel tasks")
        self.terminate_tasks()
        self.results = pd.DataFrame(self.results)
        self.cancelled.emit()
        self.thread().requestInterruption()

    def update_progress(self, step=1):
        if self.with_progress:
            self.progress += step
            print("progress: " + str(self.progress))
            self.progressed.emit(int(self.progress / self.nitems * 100))

    def perform_task(self):
        pass

    def save_results(self):
        pass
