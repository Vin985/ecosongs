
import traceback
from itertools import product

import pandas as pd
from PySide2.QtCore import Slot, qApp, Signal

from analysis.detection.detector_evaluation import (mp_get_stats,
                                                    mp_initialize_evaluator)
from gui.threads.thread_worker import ThreadWorker
from utils.commons import range_list


class SensitivityWorker(ThreadWorker):

    saved = Signal()

    def __init__(self, predictions, recordings, tags):
        super().__init__()
        self.recordings = recordings
        self.tags = tags
        self.predictions = predictions
        self.parameters = []

    @Slot()
    def perform_analysis(self):
        self.results = []
        self.computing.emit()
        print("launching sensitivity analysis")
        opts = self.options["analysis_options"]
        # opts["min_activity_start"] = 0.8
        # opts["min_activity_end"] = 0.9
        # opts["end_threshold_start"] = 0.5
        # opts["end_threshold_end"] = 0.6
        # opts["min_duration_start"] = 0.1
        # opts["min_duration_end"] = 0.12

        try:
            min_activities = range_list(
                opts["min_activity_start"], opts["min_activity_end"], opts["min_activity_step"])
            end_thresholds = range_list(
                opts["end_threshold_start"], opts["end_threshold_end"], opts["end_threshold_step"])
            min_durations = range_list(
                opts["min_duration_start"], opts["min_duration_end"], opts["min_duration_step"])
        except Exception:
            self.error.emit(traceback.format_exc())

        self.parameters = list(
            product(*[min_activities, end_thresholds, min_durations]))

        print(self.parameters)
        self.options["chunksize_percent"] = 5
        print(self.options)
        self.map(self.parameters, mp_get_stats,
                 initializer=mp_initialize_evaluator,
                 initargs=(self.predictions, self.recordings, self.tags))
        self.done.emit()

    def save_results(self, audio_path, labels_path):
        try:
            analysis_options_table = qApp.tables.analysis_options
            events_table = qApp.tables.song_events
            stats_table = qApp.tables.detector_statistics
            for params, stats, events in self.results:
                params["audio_path"] = audio_path
                params["labels_path"] = labels_path
                options_id = analysis_options_table.add(
                    params, analysis_type="activity_prediction", save=False, replace=False)

                events["analysis_options"] = options_id
                events_table.add(events, save=False, replace=True)

                stats_df = pd.DataFrame([stats])
                stats_df["analysis_options"] = options_id
                stats_table.add(stats_df, save=False)
            analysis_options_table.save()
            events_table.save()
            stats_table.save()
        except Exception:
            self.error.emit(traceback.format_exc())
        self.saved.emit()

        # self.results = []
        # self.computing.emit()
        # if self.recordings:
        #     # TODO: put chunksize as option
        #     self.map(self.recordings, function, *args, **kwargs)
        # # self.results = pd.DataFrame(self.results)
        # self.done.emit()

    # def test(self, result):
    #     print("in test callback")
    #     print(result)
    #     return result
