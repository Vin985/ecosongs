
from gui.widgets.options.import_table_options import ImportTableOptions
from gui.widgets.dialogs.workers.import_table_worker import ImportTableWorker
from gui.widgets.dialogs.progress_dialog import ProgressDialog


class ImportTableDialog(ProgressDialog):

    def __init__(self, table_name, parent=None):
        super().__init__(parent)
        self.worker = ImportTableWorker(table_name)
        self.init_options_widget(
            ImportTableOptions(self, table_name))
        self.link_events()
