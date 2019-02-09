import concurrent.futures
import time
import traceback
import multiprocessing as mp
import logging

from PySide2.QtCore import QObject, Signal


class QParallelWorker(QObject):
    logging = Signal(str)
    progressed = Signal(int)

    def __init__(self):
        QObject.__init__(self)
        self.nitems = 0
        self.progress = 0
        self.with_progress = True

    def log(self, text):
        self.logging.emit(text)

    def update_progress(self, step=1):
        if self.with_progress:
            self.progress += step
            self.progressed.emit(self.progress/self.nitems * 100)

    def map(self, collection, func, *args, with_progress=True, multiprocess=False,
            mp_method="async", **kwargs):
        self.with_progress = with_progress
        if self.with_progress:
            self.nitems = len(collection)
            self.progress = 0

        if not multiprocess:
            res = self.map_single(collection, func, *args, **kwargs)
        elif mp_method == "async":
            res = self.mp_apply_async(collection, func, *args, **kwargs)
        elif mp_method == "futures":
            res = self.mp_apply_futures(collection, func, *args, **kwargs)
        elif mp_method == "imap":
            res = self.mp_imap(collection, func, *args, **kwargs)
        else:
            raise ValueError("Unsupported mp_value. Correct values are 'futures' or 'mp'")
        return res

    # TODO accept function args to async
    def mp_apply_async(self, collection, func, processes=None, initializer=None,
                       initargs=None, chunksize=1, chunksize_percent=None, callback=None):
        res = []
        # If no number of processes provided
        if not processes:
            # If there is less items than cpus, do not instantiate all processes
            if len(collection) < mp.cpu_count():
                processes = len(collection)
            else:
                # Use all available cpus
                processes = mp.cpu_count()

        # If chunksize is a percentage, compute chunksize
        if chunksize_percent:
            chunksize = int(len(collection) * chunksize_percent / 100)

        # Create chunks
        if chunksize > 1:
            chunks = [collection[x:x+chunksize] for x in range(0, len(collection), chunksize)]
        else:
            chunks = [collection]
        # perform logic
        async_results = []
        try:
            pool = mp.Pool(processes=processes, initializer=initializer, initargs=initargs)
            for chunk in chunks:
                async_results.append(pool.apply_async(func, args=(chunk, )))
            res = []
            for result in async_results:
                res += self.process_result(result.get(), callback, is_chunk=True)
            return res

        except Exception as exc:
            print(traceback.format_exc())

        finally:
            pool.close()
            pool.join()

    def mp_imap(self, collection, func, processes=None, initializer=None,
                initargs=None, chunksize=1, callback=None):
        # If no number of processes provided
        if not processes:
            # If there is less items than cpus, do not instantiate all processes
            if len(collection) < mp.cpu_count():
                processes = len(collection)
            else:
                # Use all available cpus
                processes = mp.cpu_count()
        print(processes)
        pool = mp.Pool(processes=processes, initializer=initializer, initargs=initargs)
        tmp = pool.imap_unordered(func, collection, chunksize=chunksize)
        res = [self.process_result(result, callback) for result in tmp]
        pool.close()
        pool.join()
        return res

    def mp_apply_futures(self, collection, func, *args, **kwargs):
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
                # TODO: better exception handling
                except Exception as exc:
                    print("Oh no! An exception occured! " + str(exc))
                    print(traceback.format_exc())
            res = [self.get_result(future) for future in concurrent.futures.as_completed(futures)]
            res = list(filter(None, res))
        end = time.time()
        print("time elapsed: {}".format(end-start))
        return res

    def map_single(self, collection, func, *args, **kwargs):
        return [self.apply_func(item, func, *args, **kwargs) for item in collection]

    def apply_func(self, item, func, *args, **kwargs):
        if self.thread().isInterruptionRequested():
            # TODO: make it cleaner
            return 1
        res = func(item, *args, **kwargs)
        self.update_progress()
        return res

    def process_result(self, result, callback, is_chunk=False):
        logging.debug("processing result %s", str(result))
        if callback:
            res = callback(result)
        else:
            res = result
        progress = 1 if not is_chunk else len(result)
        self.update_progress(progress)
        return res

    def get_result(self, item):
        self.progress += 1
        self.progressed.emit(int(self.progress/self.max * 100))
        try:
            res = item.result()
        except Exception as e:
            print("Oh no! An exception occured! " + str(e))
            print(traceback.format_exc())
            return None
        return res
