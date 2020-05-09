import pandas as pd

from analysis.detection import predictions_utils
from db.models import TableModel


class ActivityPredictionsTable(TableModel):
    TABLE_NAME = "activity_predictions"
    COLUMNS = ["recording_id", "time", "activity"]
    DUPLICATE_COLUMNS = ["recording_id"]

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)

    def get_events_by_id(self, recording_id, event_options):
        preds = self.df[self.df["recording_id"] == recording_id]
        events = pd.DataFrame()
        if not preds.empty:
            events = predictions_utils.detect_songs_events(
                preds, recording_id, event_options)
        return events

    def get_events(self, recording_ids, event_options):
        if not isinstance(recording_ids, list):
            print("Recording_ids should be a list")
            return

        tmp = [self.get_events_by_id(recording_id, event_options)
               for recording_id in recording_ids]
        res = pd.concat(tmp)
        return res

    def get_predictions_by_recordings(self, recording_ids):
        return self.get_rows_by_column("recording_id", recording_ids)
