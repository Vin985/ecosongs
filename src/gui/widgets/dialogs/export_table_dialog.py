
from gui.widgets.options.export_table_options import ExportTableOptions
from gui.widgets.dialogs.workers.export_table_worker import ExportTableWorker
from gui.widgets.dialogs.progress_dialog import ProgressDialog


class ExportTableDialog(ProgressDialog):

    def __init__(self, table, parent=None):
        super().__init__(parent)
        self.worker = ExportTableWorker(table)
        self.init_options_widget(ExportTableOptions(self, table))
        self.link_events()
