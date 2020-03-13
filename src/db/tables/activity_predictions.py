import pandas as pd

from analysis.detection import predictions_utils
from db.models import TableModel


class ActivityPredictionsTable(TableModel):
    TABLE_NAME = "activity_predictions"
    COLUMNS = ["recording_id", "time", "activity"]
    DUPLICATE_COLUMNS = ["recording_id", "analysis_options"]

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)

    def get_events(self, recording_id, event_options):
        preds = self.df[self.df["recording_id"] == recording_id]
        events = pd.DataFrame()
        if not preds.empty:
            events = predictions_utils.detect_songs_events(
                preds[["time", "activity"]], recording_id, event_options)
        return events
