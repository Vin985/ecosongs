from PySide2.QtCore import Signal

from gui.widgets.options.export_song_events_options import ExportSongEventsOptions
from gui.widgets.dialogs.workers.export_song_events_worker import ExportSongEventsWorker
from gui.widgets.dialogs.progress_dialog import ProgressDialog


class ExportSongEventsDialog(ProgressDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.worker = ExportSongEventsWorker()
        self.init_options_widget(ExportSongEventsOptions(self))
        self.link_events()

