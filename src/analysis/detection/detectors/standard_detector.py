import pandas as pd

from .detector import Detector


class StandardDetector(Detector):
    def __init__(self):
        super().__init__()
        # self._events = pd.DataFrame()
        # self.matches = pd.DataFrame()

    # @property
    # def events(self):
    #     if not self._events:
    #         self._events = self.get_events()
    #     return self._events

    # @events.setter
    # def events(self, df):
    #     self._events = df

    def get_events(self, predictions, options):
        predictions = predictions[["activity", "recording_id", "time"]]
        events = predictions.groupby("recording_id", as_index=False, observed=True)
        if options.get("parallel", True):
            events = events.parallel_apply(self.get_recording_events, options)
        else:
            events = events.apply(self.get_recording_events, options)
        events.reset_index(inplace=True)
        events.drop(["level_0", "level_1"], axis=1, inplace=True)
        events["event_duration"] = events["end"] - events["start"]
        events.reset_index(inplace=True)
        events = events[self.EVENTS_COLUMNS.keys()]
        events.rename(columns=self.EVENTS_COLUMNS, inplace=True)
        return events

    def get_recording_events(self, predictions, options=None):
        options = options or {}
        min_activity = options.get("min_activity", self.DEFAULT_MIN_ACTIVITY)
        end_threshold = options.get("end_threshold", self.DEFAULT_END_THRESHOLD)
        min_duration = options.get("min_duration", self.DEFAULT_MIN_DURATION)
        event_index = 0
        ongoing = False
        events = []
        start = 0
        end = 0
        # def detect_songs_events(predictions):
        for activity, recording_id, pred_time in predictions.itertuples(index=False):
            # Check if prediction is above a defined threshold
            if activity > min_activity:
                # If not in a song, create a new event
                if not ongoing:
                    ongoing = True
                    event_index += 1
                    start = pred_time
            elif ongoing:
                # if above an end threshold, consider it as a single event
                if activity > end_threshold:
                    continue
                # If below the threshold and in an active event, end it
                ongoing = False
                end = pred_time
                # log event if its duration is greater than minimum threshold
                if (end - start) > min_duration:
                    events.append(
                        {
                            "event_index": event_index,
                            "recording_id": recording_id,
                            "start": start,
                            "end": end,
                        }
                    )
        events = pd.DataFrame(events)
        return events

    def associate_recordings(self, events, recordings):
        events = events.merge(
            recordings[["id", "name"]], left_on="recording_id", right_on="id"
        )
        events.reset_index(inplace=True)
        events = events[self.EVENTS_COLUMNS.keys()]
        events.rename(columns=self.EVENTS_COLUMNS, inplace=True)
        return events

    def get_matches(self, events, tags):
        tags = tags.rename(columns=self.TAGS_COLUMNS_RENAME)
        tmp = tags.merge(events, on="recording_id", how="outer")
        # Select tags associated with an event
        matched = tmp.loc[
            (tmp.event_start < tmp.tag_end) & (tmp.event_end > tmp.tag_start)
        ]
        # Get list of tags not associated with an event
        unmatched = tags.loc[~tags.tag_id.isin(matched.tag_id.unique())]
        # add them to the final dataframe
        match_df = matched.merge(unmatched, how="outer")
        match_df.loc[match_df.event_id.isna(), "event_id"] = -1
        match_df.event_id = match_df.event_id.astype("int64")
        match_df.reset_index(inplace=True)
        return match_df

    def match_predictions(self, predictions, events, tags):
        for _, x in tags.iterrows():
            predictions.loc[
                predictions.time.between(x["tag_start"], x["tag_end"]),
                ["tag", "tag_index"],
            ] = [1, x["tag_index"]]

        for _, x in events.iterrows():
            predictions.loc[
                predictions.time.between(x["event_start"], x["event_end"]), "event"
            ] = 2

    def get_stats(self, events, matches):
        # True pos: number of unique events that matched with a tag
        true_pos_events = len(matches[matches.event_id != -1].event_id.unique())
        true_pos_tags = len(matches[matches.event_id != -1].tag_id.unique())
        # False neg: number of tags that did not have a match
        false_neg = matches[matches.event_id == -1].shape[0]
        # Number of tags that are matched
        n_tags_matched = len(matches.loc[matches.event_id != -1].tag_id.unique())

        # Precision: TP / TP + FP
        precision = true_pos_events / events.shape[0]
        # Recall: TP / TP + FN
        recall = true_pos_tags / (true_pos_tags + false_neg)
        f1_score = 2 * (precision * recall) / (precision + recall)

        return {
            "n_events": events.shape[0],
            "n_tags": len(matches.tag_id.unique()),
            "true_positive_events": true_pos_events,
            "true_positive_tags": true_pos_tags,
            "false_negative": false_neg,
            "n_tags_matched": n_tags_matched,
            "precision": precision,
            "recall": recall,
            "F1_score": f1_score,
        }

    def evaluate(self, predictions, tags, options):
        events = self.get_events(predictions, options)
        matches = self.get_matches(events, tags)
        stats = self.get_stats(events, matches)
        print("Stats for options {0}: {1}".format(options, stats))
        return [options, stats, events]
