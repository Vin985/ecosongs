
import files.tag_manager as tag_manager
from gui.threads.thread_worker import ThreadWorker

# from PySide2.QtCore import qApp


class TagImportWorker(ThreadWorker):

    def __init__(self, recordings):
        super().__init__()
        self.recordings = recordings

    def perform_task(self):
        print("Importing tags")
        self.options["save"] = True
        self.results = tag_manager.load_tags(
            self.recordings, self.options["task_options"])

    def save_results(self):
        tags_table = qApp.tables.tags
        tags_table.add(self.results, save=True, replace=True)
        qApp.tables.recordings.save()
