import time

import pandas as pd
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
        self.detect_songs.connect(
            self.worker.detect_songs, type=Qt.QueuedConnection)

    @Slot()
    def start(self):
        print("clicking start")
        # TODO: add detection options in UI
        self.worker.options = self.options.get_options()
        self.detect_songs.emit()
        self.started = time.time()

    @Slot()
    def process_results(self):
        super().process_results()
        res = self.worker.results
        if res:
            events = pd.concat(res)
            if self.options.checkbox_save.isChecked():
                activity_table = qApp.tables.activity_predictions
                activity_table.add(events, save=True,
                                   replace=self.options.checkbox_overwrite.isChecked())

        # if self.options.checkbox_save.isChecked():
        #     events_table = qApp.tables.song_events
        #     analysis_options = qApp.tables.analysis_options
        #     options_id = analysis_options.add(
        #         self.audio_analyzer.options, type="event_detection", save=True)
        #     events["analysis_options"] = options_id
        #     print(events)
        #     events_table.add(events, save=True,
        #                      replace=self.options.checkbox_overwrite.isChecked())
