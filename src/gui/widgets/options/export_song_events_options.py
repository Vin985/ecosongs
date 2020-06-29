from PySide2.QtWidgets import QWidget

from gui.widgets.options.ui.export_song_events_options_ui import (
    Ui_ExportSongEventsOptions,
)


class ExportSongEventsOptions(QWidget, Ui_ExportSongEventsOptions):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.link_events()

    def init_ui(self):
        pass

    def link_events(self):
        pass

    def get_options(self):
        opts = {}
        return opts
