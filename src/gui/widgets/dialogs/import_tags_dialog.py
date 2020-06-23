from PySide2.QtCore import Signal

from gui.widgets.options.import_tags_options import ImportTagsOptions
from gui.widgets.dialogs.workers.import_tags_worker import ImportTagsWorker
from gui.widgets.dialogs.progress_dialog import ProgressDialog


class ImportTagsDialog(ProgressDialog):

    launch_analysis = Signal()
    save_results = Signal(str, str)

    def __init__(self, recordings, parent=None):
        super().__init__(parent)
        self.worker = ImportTagsWorker(recordings)
        self.init_options_widget(ImportTagsOptions(self))
        self.link_events()
