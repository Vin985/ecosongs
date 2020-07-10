import files.tag_manager as tag_manager
from gui.threads.thread_worker import ThreadWorker

# from PySide2.QtCore import qApp


class ImportTagsWorker(ThreadWorker):
    def __init__(self, recordings):
        super().__init__()
        self.recordings = recordings[["id", "name", "path", "has_tags"]].copy()

    def perform_task(self):
        print("Importing tags")
        self.options["save"] = True
        self.results = tag_manager.load_tags(
            self.recordings, self.options["task_options"],
        )

    def save_results(self):
        tags_table = qApp.tables.tags
        tags, recs = self.results
        tags_table.add(tags, save=True, replace=True)
        recs_df = qApp.tables.recordings.df
        recs_df.update(recs)
        qApp.tables.recordings.save()

