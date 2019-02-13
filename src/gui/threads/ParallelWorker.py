import concurrent.futures
import logging
import multiprocessing as mp
import time
import traceback


class ParallelWorker():

    def __init__(self):
        self.__options = {"with_progress": True, "multiprocess": True, "nprocess": None,
                          "mp_method": "async", "chunksize": 1, "chunksize_percent": None}
        self.nitems = 0
        self.progress = 0
        self.pool = None
        self.results = []

    @property
    def with_progress(self):
        return self.__options["with_progress"]

    @property
    def options(self):
        """
        Docstring for options property
        """
        return self.__options

    @options.setter
    def options(self, options):
        """
        Docstring for options property
        """
        self.__options.update(options)

    def terminate_tasks(self):
        print("in cancel tasks")
        self.pool.terminate()
        self.pool.join()

    def log(self, text):
        print(text)

    def update_progress(self, step=1):
        if self.with_progress:
            self.progress += step
            print("progress: " + str(int(self.progress/self.nitems * 100)))

    def map(self, collection, func, *args, **kwargs):
        print(self.options)
        if self.with_progress:
            self.nitems = len(collection)
            self.progress = 0

        mp_method = self.options["mp_method"]
        if not self.options["multiprocess"]:
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
    def mp_apply_async(self, collection, func, initializer=None, initargs=None, callback=None):
        print("async")
        res = []
        # If no number of processes provided
        if not self.options["nprocess"]:
            # If there is less items than cpus, do not instantiate all processes
            if len(collection) < mp.cpu_count():
                processes = len(collection)
            else:
                # Use all available cpus
                processes = mp.cpu_count()
        else:
            processes = self.options["nprocess"]

        # If chunksize is a percentage, compute chunksize
        if self.options["chunksize_percent"]:
            chunksize = int(len(collection) * self.options["chunksize_percent"] / 100)
        else:
            chunksize = self.options["chunksize"]

        print("chunks")
        print(chunksize)
        # Create chunks
        if len(collection) > 1:
            chunks = [collection[x:x+chunksize] for x in range(0, len(collection), chunksize)]
        else:
            chunks = [collection]

        # perform logic
        async_results = []
        print(processes)
        try:
            self.pool = mp.Pool(processes=processes, initializer=initializer, initargs=initargs)
            for chunk in chunks:
                print("chunk: " + str(chunk))
                async_results.append(self.pool.apply_async(func, args=(chunk, )))
            self.results = []
            for result in async_results:
                self.results += self.process_chunk_result(result.get(), callback)
            return self.results
        except Exception as exc:
            print(traceback.format_exc())
            return self.results
        finally:
            self.pool.close()
            self.pool.join()

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
        pool = mp.Pool(processes=processes, initializer=initializer, initargs=initargs)
        tmp = pool.imap_unordered(func, collection, chunksize=chunksize)
        res = [self.process_chunk_result(result, callback) for result in tmp]
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
        res = func(item, *args, **kwargs)
        self.update_progress()
        return res

    def process_result(self, result, callback, progress=1):
        logging.debug("processing result %s", str(result))
        if callback:
            res = callback(result)
        else:
            res = result
        self.update_progress(progress)
        return res

    def process_chunk_result(self, chunk_result, callback):
        result, size = chunk_result
        return self.process_result(result, callback, size)

    def get_result(self, item):
        self.update_progress(1)
        try:
            res = item.result()
        except Exception as e:
            print("Oh no! An exception occured! " + str(e))
            print(traceback.format_exc())
            return None
        return res
