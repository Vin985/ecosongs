import time

import pandas as pd
from PySide2.QtCore import Qt, QThread, Signal, Slot
# from PySide2.QtGui import qApp
from PySide2.QtWidgets import QDialog

from gui.widgets.options.sensitivity_options import SensitivityOptions
from gui.widgets.dialogs.workers.sensitivity_worker import SensitivityWorker
from gui.widgets.dialogs.progress_dialog import ProgressDialog


class SensitivityDialog(ProgressDialog):

    launch_analysis = Signal()
    save_results = Signal(str, str)

    def __init__(self, predictions, recordings, tags, audio_path, labels_path, parent=None):
        super().__init__(parent)
        self.worker = SensitivityWorker(
            predictions=predictions, recordings=recordings, tags=tags)
        self.options = SensitivityOptions(self)
        self.content_layout.addWidget(self.options)
        self.save = False
        self.overwrite = False
        self.audio_path = audio_path
        self.labels_path = labels_path
        self.link_events()
        # self.adjustSize()

    def link_events(self):
        super().link_events()
        self.launch_analysis.connect(
            self.worker.perform_analysis, type=Qt.QueuedConnection)
        self.save_results.connect(
            self.worker.save_results, type=Qt.QueuedConnection)
        self.worker.saved.connect(self.results_saved)

    @Slot()
    def start(self):
        print("clicking start")
        opts = self.options.get_options()
        self.worker.options = opts
        self.save = opts["save"]
        self.overwrite = opts["overwrite"]
        self.launch_analysis.emit()
        self.started = time.time()

    @Slot()
    def duration_message(self):
        params = len(self.worker.parameters)
        log_text = ("Calculated stats for %d combinations in %0.3f seconds (%0.3fs/combination)" %
                    (params, self.duration, self.duration / params))
        if self.save:
            log_text += ". Saving results, please wait..."
            self.save_results.emit(self.audio_path, self.labels_path)
        return log_text

    def results_saved(self):
        super().process_results()

    def save_results2(self):
        results = self.worker.results
        analysis_options_table = qApp.tables.analysis_options
        events_table = qApp.tables.song_events
        stats_table = qApp.tables.detector_statistics
        for params, stats, events in results:
            print(" saving params " + str(params))
            params["audio_path"] = self.audio_path
            params["labels_path"] = self.labels_path
            options_id = analysis_options_table.add(
                params, analysis_type="activity_prediction", save=False, replace=False)

            # events["analysis_options"] = options_id
            # events_table.add(events, save=False, replace=True)

            stats_df = pd.DataFrame([stats])
            stats_df["analysis_options"] = options_id
            stats_table.add(stats_df, save=False)
        analysis_options_table.save()
        events_table.save()
        stats_table.save()
