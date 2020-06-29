from PySide2.QtCore import Signal

from gui.widgets.options.YYY_options import XXXOptions
from gui.widgets.dialogs.workers.YYY_worker import XXXWorker
from gui.widgets.dialogs.progress_dialog import ProgressDialog


class XXXDialog(ProgressDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.worker = XXXWorker()
        self.init_options_widget(XXXOptions(self))
        self.link_events()
