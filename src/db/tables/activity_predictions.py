import pandas as pd
import numpy as np

from analysis.detection.detectors.standard_detector import StandardDetector
from analysis.detection.detectors.subsampling_detector import SubsamplingDetector
from db.models import TableModel


class ActivityPredictionsTable(TableModel):
    TABLE_NAME = "activity_predictions"
    COLUMNS = ["recording_id", "time", "activity"]
    DUPLICATE_COLUMNS = ["recording_id"]
    COLUMNS_TYPE = {"activity": np.float32,
                    "time": np.float32,
                    "recording_id": "category"}

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)
        self.detectors = {
            "standard": StandardDetector(),
            "subsampling": SubsamplingDetector()
        }

    def check_ids(self, table):
        # Do not check ids as we do not use them for this table (index is time)
        return table

    def save(self, update=False):
        if "id" in self._df.columns:
            self._df.drop(columns=["id"], inplace=True)
        self._df.activity = self._df.activity.round(3)
        self._df.time = self._df.time.round(3)
        super().save(update)

    def get_events_by_id(self, recording_id, options):
        detector = self.detectors[options["method"]]
        preds = self.df[self.df["recording_id"] == recording_id]
        events = detector.get_recording_events(preds, recording_id, options)
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
