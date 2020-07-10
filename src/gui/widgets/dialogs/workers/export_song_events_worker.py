from gui.threads.thread_worker import ThreadWorker

from analysis.detection import detectors

# from PySide2.QtCore import qApp


class ExportSongEventsWorker(ThreadWorker):
    def __init__(self, recordings):
        super().__init__()
        self.recordings = recordings

    def perform_task(self):
        print("Exporting song events")
        predictions_df = qApp.tables.activity_predictions.get_predictions_by_recordings(
            self.recordings.id
        )

        detector = detectors.DETECTORS[self.options["method"]]
        events = detector.get_events(predictions_df, self.options)
        events = events.merge(self.recordings, left_on="recording_id", right_on="id")
        events = events.drop(columns=["recording_id", "id"])
        events.reset_index(inplace=True, drop=True)

        if self.options["format"] == "csv":
            events = events.drop(columns=["event_id"])
            events.to_csv(self.options["dest"])
        else:
            events.to_feather(self.options["dest"])

