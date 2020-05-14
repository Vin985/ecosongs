import datetime
import functools

import pandas as pd

from .detector import Detector


class SubsamplingDetector(Detector):

    def get_stats(self, predictions, recordings, tags):
        pass

    def resample_max(self, x, threshold=0.98, mean_thresh=0):
        if any(x >= threshold) and x.mean() > mean_thresh:
            return 2
        return 0

    def isolate_events_subsampling(self, predictions, step):
        tmp = predictions.loc[predictions.event > 0]
        tmp.reset_index(inplace=True)

        step = datetime.timedelta(milliseconds=step)
        start = None
        events = []
        event_id = 1
        if len(tmp):
            for _, x in tmp.iterrows():
                if not start:
                    prev_time = x.datetime
                    start = prev_time
                    continue
                diff = x.datetime - prev_time
                if diff > step:
                    end = prev_time + step
                    events.append({"event_id": event_id, "recording_id": x.recording_id,
                                   "start": start.timestamp(), "end": end.timestamp()})
                    event_id += 1
                    start = x.datetime
                prev_time = x.datetime

            end = prev_time + step
            events.append({"event_id": event_id, "recording_id": x.recording_id,
                           "start": start.timestamp(), "end": end.timestamp()})

        events = pd.DataFrame(events)
        return events

    # def detect_events_subsampling(predictions, recording_id=-1, detection_options=None):
    #     preds = predictions.copy()
    #     if not "tag" in preds.columns:
    #         preds.loc[:, "tag"] = -1
    #     preds.loc[:, "event"] = -1
    #     preds.loc[:, "datetime"] = pd.to_datetime(preds.time * 10**9)
    #     preds.set_index("datetime", inplace=True)

    #     min_activity = detection_options.get("min_activity", 0.85)
    #     step = detection_options.get("min_duration", 0.1) * 1000
    #     isolate_events = detection_options.get("isolate_events", False)

    #     resampled = preds.resample(str(step)+"ms")
    #     resample_func = functools.partial(resample_max, threshold=min_activity)
    #     res = resampled.agg({"activity": resample_func,
    #                          "tag": has_tag})
    #     res.rename(columns={"activity": "event"}, inplace=True)
    #     res["recording_id"] = recording_id

    #     if isolate_events:
    #         return isolate_events_subsampling(res, step)

    #     return res

    def get_recording_events(self, predictions, recording_id, options=None):
        preds = predictions[["time", "activity"]].copy()
        min_activity = options.get(
            "min_activity", self.DEFAULT_MIN_ACTIVITY)
        step = options.get("min_duration", self.DEFAULT_MIN_DURATION) * 1000

        preds.loc[:, "datetime"] = pd.to_datetime(preds.time * 10**9)
        preds.set_index("datetime", inplace=True)

        resampled = preds.resample(str(step)+"ms")
        # TODO: add resampling method in options
        resample_func = functools.partial(
            self.resample_max, threshold=min_activity)
        res = resampled.agg({"activity": resample_func})
        res.rename(columns={"activity": "event"}, inplace=True)
        res["recording_id"] = recording_id

        return self.isolate_events_subsampling(res, step)
