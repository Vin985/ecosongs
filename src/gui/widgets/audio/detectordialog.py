import time

import yaml
from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtGui import qApp

from analysis.detection.song_detector import SongEventsTable
from gui.widgets.audio.analyzerdialog import AnalyzerDialog
from gui.widgets.audio.ui.detector_dialog_ui import Ui_DetectorDialog


class DetectorDialog(AnalyzerDialog, Ui_DetectorDialog):

    detect_songs = Signal()
    cancelling = Signal()

    def __init__(self, recordings):
        super().__init__(recordings)
        self.setupUi(self)
        self.link_events()
        # Set settings to local to avoid saving them unless asked
        # TODO: allow saving settings
        self.btn_close.hide()
        self.lbl_activity.setText(str(self.slider_activity.value()))

    def link_events(self):
        super().link_events()
        self.slider_activity.valueChanged.connect(self.update_activity)
        self.detect_songs.connect(self.audio_analyzer.detect_songs, type=Qt.QueuedConnection)

    def reset_progress(self):
        self.progress_bar.setEnabled(True)
        self.progress_bar.setValue(0)

    def update_activity(self, activity):
        self.lbl_activity.setText(str(activity))

    @Slot()
    def start(self):
        print("clicking start")
        # TODO: add detection options in UI
        model_opts = {"model_root_dir": "analysis/detection/models",
                      "classifier": "biotic",
                      "options_file": "analysis/detection/models/biotic/network_opts.yaml",
                      "weights_file": "analysis/detection/models/biotic/weights_99.pkl-1"}
        with open(model_opts["options_file"]) as opt_file:
            options = yaml.load(opt_file)
        detection_options = {'min_activity': self.slider_activity.value()/100,
                             'min_duration': self.spin_min_duration.value()}
        options = {"initargs": (options,
                                model_opts["weights_file"],
                                detection_options),
                   "chunksize_percent": 2}
        self.audio_analyzer.options = options
        self.detect_songs.emit()
        self.started = time.time()

    @Slot()
    def process_results(self):
        super().process_results()
        events = self.audio_analyzer.results
        print(events)
        if self.checkbox_save.isChecked():
            events_table = SongEventsTable(dbmanager=qApp.feather_manager)
            events_table.add(events, save=True, replace=self.checkbox_overwrite.isChecked())
