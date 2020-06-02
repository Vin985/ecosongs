
# from pandarallel import pandarallel


class Detector():

    EVENTS_COLUMNS = {'index': 'event_id',
                      'event_index': "event_index",
                      'recording_id': "recording_id",
                      'start': "event_start",
                      'end': "event_end",
                      "event_duration": "event_duration"}
    TAGS_COLUMNS_RENAME = {'id': "tag_id"}

    DEFAULT_MIN_ACTIVITY = 0.85
    DEFAULT_MIN_DURATION = 0.1
    DEFAULT_END_THRESHOLD = 0.6

    def __init__(self):
        pass
        # pandarallel.initialize()
        # self.predictions = predictions
        # self.options = options or {}

        # self.predictions.loc[:, "tag"] = 0
        # self.predictions.loc[:, "tag_index"] = -1
        # self.predictions.loc[:, "event"] = 0
        # self.predictions.loc[:, "datetime"] = pd.to_datetime(
        #     predictions.time * 10**9)

    def _get_recording_events(self, predictions, options):
        return self.get_recording_events(predictions, predictions.name, options)

    def get_recording_events(self, predictions, recording_id, options=None):
        pass

    def get_events(self, predictions, options):
        pass
