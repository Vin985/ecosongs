from PySide2.QtCore import Signal

from gui.widgets.options.tag_import_options import TagImportOptions
from gui.widgets.dialogs.workers.tag_import_worker import TagImportWorker
from gui.widgets.dialogs.progress_dialog import ProgressDialog


class TagImportDialog(ProgressDialog):

    launch_analysis = Signal()
    save_results = Signal(str, str)

    def __init__(self, recordings, parent=None):
        super().__init__(parent)
        self.worker = TagImportWorker(recordings)
        self.init_options_widget(TagImportOptions(self))
        self.link_events()
