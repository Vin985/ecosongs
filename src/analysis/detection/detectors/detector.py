
import pandas as pd


class Detector():

    PREDICTIONS_COLUMNS = {'end': "event_end", 'event_id': "event_id",
                           'recording_id': "recording_id", 'start': "event_start",
                           'name': "file_name", "index": "event_index"}
    EVENTS_COLUMNS = {'end': "event_end", 'event_id': "event_id",
                      'recording_id': "recording_id", 'start': "event_start",
                      'name': "file_name", "index": "event_index", "event_duration": "event_duration"}

    def __init__(self, predictions, options=None):
        self.predictions = predictions
        self.options = options or {}

        self.predictions.loc[:, "tag"] = 0
        self.predictions.loc[:, "tag_index"] = -1
        self.predictions.loc[:, "event"] = 0
        self.predictions.loc[:, "datetime"] = pd.to_datetime(
            predictions.time * 10**9)

    def get_events(self):
        pass

    def get_stats(self, recordings, tags):
        pass
