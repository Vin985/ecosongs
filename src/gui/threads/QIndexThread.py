import concurrent.futures
import time
import traceback

import analysis.indexes as indexes
from PySide2 import QtCore


class QIndexThread(QtCore.QThread):
    # TODO: change index class for better communication
    computing = QtCore.Signal(str, bool)
    started = QtCore.Signal()
    progression = QtCore.Signal(int)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        self.started.emit()
        self.max = len(self.recordings)
        self.progress = 0
        # TODO: change for other indexes
        start = time.time()
        futures = []
        with concurrent.futures.ProcessPoolExecutor() as executor:
            # futures = executor.map(ACI, self.recordings)
            # self.res = [self.get_result_map(aci) for aci in futures]
            # submit solution
            for rec in self.recordings:
                try:
                    futures.append(executor.submit(indexes.compute_index,
                                                   type="ACI",
                                                   recording=rec,
                                                   spec_opts=self.spec_opts))
                except Exception as exc:
                    print("Oh no! An exception occured! " + str(exc))
                    print(traceback.format_exc())
            self.res = [self.get_result_submit(aci) for aci in concurrent.futures.as_completed(futures)]
            self.res = list(filter(None, self.res))
        end = time.time()
        print("time elapsed: {}".format(end-start))

    def get_result_submit(self, item):
        self.progress += 1
        self.progression.emit(int(self.progress/self.max * 100))
        try:
            res = item.result()
        except Exception as e:
            print("Oh no! An exception occured! " + str(e))
            print(traceback.format_exc())
            return None
        return res

    def get_result_map(self, item):
        self.progress += 1
        self.progression.emit(int(self.progress/self.max * 100))
        return item

    def files_to_wav(self):
        for fn in self.files:
            if self.isInterruptionRequested():
                return (1)
            self.file_to_wav(fn)

    def log(self, text):
        self.converting.emit(text, True)
