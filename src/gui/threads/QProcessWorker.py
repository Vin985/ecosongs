import concurrent.futures
import time
import traceback

import analysis.indexes as indexes

from PySide2.QtCore import QObject, Signal
from gui.threads.QThreadWorker import QThreadWorker


class QPoolWorker(QThreadWorker):
    def __init__(self):
        super().__init__()
        self.max = 0
        self.progress = 0

    def apply_with_progress(self, collection, func, *args, **kwargs):
        self.max = len(collection)
        self.progress = 0
        start = time.time()
        futures = []
        res = []
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for item in collection:
                # TODO : make sure this is properly interrupted
                if self.thread().isInterruptionRequested():
                    return 1
                try:
                    futures.append(executor.submit(func, item, *args, **kwargs))
                except Exception as exc:
                    print("Oh no! An exception occured! " + str(exc))
                    print(traceback.format_exc())
            res = [self.get_result(future) for future in concurrent.futures.as_completed(futures)]
            res = list(filter(None, res))
        end = time.time()
        print("time elapsed: {}".format(end-start))
        return res

    def get_result(self, item):
        self.progress += 1
        self.update_progress.emit(int(self.progress/self.max * 100))
        try:
            res = item.result()
        except Exception as e:
            print("Oh no! An exception occured! " + str(e))
            print(traceback.format_exc())
            return None
        return res
