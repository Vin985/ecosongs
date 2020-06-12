
from gui.widgets.options.export_table_options import ExportTableOptions
from gui.widgets.dialogs.workers.export_table_worker import ExportTableWorker
from gui.widgets.dialogs.progress_dialog import ProgressDialog


class ExportTableDialog(ProgressDialog):

    def __init__(self, table_name, table_data=None, parent=None):
        super().__init__(parent)
        self.worker = ExportTableWorker(table_name, table_data)
        self.init_options_widget(
            ExportTableOptions(self, table_name))
        self.link_events()
