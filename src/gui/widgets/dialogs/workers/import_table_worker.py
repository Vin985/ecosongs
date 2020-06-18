from gui.threads.thread_worker import ThreadWorker

# from PySide2.QtCore import qApp


class ImportTableWorker(ThreadWorker):
    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name
        self.table_model = qApp.tables.get_table(self.table_name)
        self.table = None

    def perform_task(self):
        print("Importing table: ", self.table_name)
        to_import = self.options["to_import"]
        if self.options["update"]:
            self.table_model.add(
                to_import, replace=self.options["overwrite"], save=True
            )
        else:
            self.table_model.update(to_import, save=True)
