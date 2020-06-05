
from gui.threads.thread_worker import ThreadWorker

# from PySide2.QtCore import qApp


class ExportTableWorker(ThreadWorker):

    def __init__(self, table):
        super().__init__()
        self.table = table

    def perform_task(self):
        print("Exporting table: ", self.table)
        # self.options["save"] = True
        # self.results = tag_manager.load_tags(
        #     self.recordings, self.options["task_options"])
