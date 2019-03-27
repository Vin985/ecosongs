import time

from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtGui import qApp

from gui.widgets.audio.analyzerdialog import AnalyzerDialog
from gui.widgets.audio.detectoroptions import DetectorOptions


class DetectorDialog(AnalyzerDialog):

    detect_songs = Signal()
    cancelling = Signal()

    def __init__(self, recordings, export_pdf=False, parent=None):
        super().__init__(recordings, parent)
        self.options = DetectorOptions(self, export_pdf)
        self.content_layout.addWidget(self.options)
        self.btn_close.hide()
        self.link_events()
        # self.adjustSize()

    def link_events(self):
        super().link_events()
        self.detect_songs.connect(self.audio_analyzer.detect_songs, type=Qt.QueuedConnection)

    @Slot()
    def start(self):
        print("clicking start")
        # TODO: add detection options in UI
        self.audio_analyzer.options = self.content_widget.get_options()
        self.detect_songs.emit()
        self.started = time.time()

    @Slot()
    def process_results(self):
        super().process_results()
        events = self.audio_analyzer.results
        print(events)
        if self.content_widget.checkbox_save.isChecked():
            events_table = qApp.tables.song_events
            events_table.add(events, save=True,
                             replace=self.content_widget.checkbox_overwrite.isChecked())
