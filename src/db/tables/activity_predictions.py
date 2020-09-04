import pandas as pd
import numpy as np

from analysis.detection.detectors.standard_detector import StandardDetector
from analysis.detection.detectors.subsampling_detector import SubsamplingDetector
from db.dbmodels import TableDBModel


class ActivityPredictionsTable(TableDBModel):
    TABLE_NAME = "activity_predictions"
    COMMON_COLUMNS = []
    COLUMNS = ["recording_id", "time", "activity"]
    DUPLICATE_COLUMNS = ["recording_id"]
    COLUMNS_TYPE = {
        "activity": np.float32,
        "time": np.float32,
        "recording_id": "category",
    }
    REFERS_TO = {
        "recordings": {
            "on": "recording_id:id",
            "for_import": ["name", "year", "plot", "site"],
        }
    }

    def __init__(self, df=None, dbmanager=None):
        TableDBModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)
        self.detectors = {
            "standard": StandardDetector(),
            "subsampling": SubsamplingDetector(),
        }

    def check_ids(self, table):
        return table

    def save(self, update=False):
        if "id" in self._df.columns:
            self._df.drop(columns=["id"], inplace=True)
        self._df.activity = self._df.activity.round(3)
        self._df.time = self._df.time.round(3)
        self._df = self._df.drop_duplicates()
        super().save(update)

    def get_events_by_id(self, recording_id, options):
        detector = self.detectors[options["method"]]
        preds = self.df.loc[self.df["recording_id"] == recording_id]
        events = detector.get_recording_events(preds, options)
        return events

    def get_predictions_by_id(self, recording_id):
        if not self.df.empty:
            return self.df.loc[self.df["recording_id"] == recording_id]
        return pd.DataFrame()

    def get_events(self, recording_ids, event_options):
        if not isinstance(recording_ids, list):
            print("Recording_ids should be a list")
            return

        tmp = [
            self.get_events_by_id(recording_id, event_options)
            for recording_id in recording_ids
        ]
        res = pd.concat(tmp)
        return res

    def get_predictions_by_recordings(self, recording_ids):
        return self.get_rows_by_column("recording_id", recording_ids)
