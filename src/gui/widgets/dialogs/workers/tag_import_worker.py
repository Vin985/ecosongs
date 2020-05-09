
import files.tag_manager as tag_manager
from gui.threads.thread_worker import ThreadWorker


class TagImportWorker(ThreadWorker):

    def __init__(self, recordings):
        super().__init__()
        self.recordings = recordings

    def perform_task(self):
        print("Importing tags")
        self.options["save"] = True
        tag_manager.load_tags(self.recordings, self.options)

    def save_results(self):
        print(self.results, self.recordings)
