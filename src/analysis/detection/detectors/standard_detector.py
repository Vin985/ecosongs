
import pandas as pd

from .detector import Detector


class StandardDetector(Detector):

    DEFAULT_MIN_ACTIVITY = 0.85
    DEFAULT_MIN_DURATION = 0.1
    DEFAULT_END_THRESHOLD = 0.6

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self._events = pd.DataFrame()
        self.matches = pd.DataFrame()

    @property
    def events(self):
        if not self._events:
            self._events = self.get_events()
        return self._events

    @events.setter
    def events(self, df):
        self._events = df

    def get_events(self):
        events = self.predictions.groupby("recording_id", as_index=False).apply(
            self.get_recording_events)
        events.reset_index(inplace=True)
        events.drop(["level_0", "level_1"], axis=1, inplace=True)
        events["event_duration"] = events["end"] - \
            events["start"]
        return events

    def get_recording_events(self, recording_id):
        min_activity = self.options.get(
            "min_activity", self.DEFAULT_MIN_ACTIVITY)
        min_duration = self.options.get(
            "min_duration", self.DEFAULT_END_THRESHOLD)
        end_threshold = self.options.get(
            "end_threshold", self.DEFAULT_MIN_DURATION)
        event_id = 0
        ongoing = False
        events = []
        start = 0
        end = 0
        # def detect_songs_events(predictions):
        for pred_time, activity in self.predictions.itertuples(index=False):
            # Check if prediction is above a defined threshold
            if activity > min_activity:
                # If not in a song, create a new event
                if not ongoing:
                    ongoing = True
                    event_id += 1
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
                    events.append({"event_id": event_id, "recording_id": recording_id,
                                   "start": start, "end": end})
        events = pd.DataFrame(events)
        return events

    def associate_recordings(self, recordings):
        self.events = self.events.merge(
            recordings[["id", "name"]], left_on="recording_id", right_on="id")
        self.events.reset_index(inplace=True)
        self.events = self.events[self.EVENTS_COLUMNS.keys()]
        self.events.rename(columns=self.EVENTS_COLUMNS, inplace=True)

    def get_matches(self, tags):
        tmp = tags.merge(
            self.events, left_on="file_id", right_on="file_name", how="outer")
        # Select tags associated with an event
        matched = tmp.loc[(tmp.event_start < tmp.tag_end) &
                          (tmp.event_end > tmp.tag_start)]
        # Get list of tags not associated with an event
        unmatched = tags.loc[~tags.tag_index.isin(
            matched.tag_index.unique())]
        # add them to the final dataframe
        match_df = matched.merge(unmatched, how="outer")
        match_df.loc[match_df.event_index.isna(), "event_index"] = -1
        match_df.event_index = match_df.event_index.astype('int64')
        match_df.reset_index(inplace=True)
        self.matches = match_df

    def match_predictions(self, tags, filter=None):
        for _, x in tags.iterrows():
            self.predictions.loc[self.predictions.time.between(x["tag_start"], x["tag_end"]), [
                "tag", "tag_index"]] = [1, x["tag_index"]]

        for _, x in self.events.iterrows():
            self.predictions.loc[self.predictions.time.between(
                x["event_start"], x["event_end"]), "event"] = 2

    def get_stats(self):
        # True pos: number of unique events that matched with a tag
        true_pos_events = len(
            self.matches[self.matches.event_index != -1].event_index.unique())
        true_pos_tags = len(
            self.matches[self.matches.event_index != -1].tag_index.unique())
        # False neg: number of tags that did not have a match
        false_neg = self.matches[self.matches.event_index == -1].shape[0]
        # Number of tags that are matched
        n_tags_matched = len(
            self.matches.loc[self.matches.event_index != -1].tag_index.unique())

        # Precision: TP / TP + FP
        precision = true_pos_events / self.events.shape[0]
        # Recall: TP / TP + FN
        recall = true_pos_tags / (true_pos_tags + false_neg)
        f1_score = 2 * (precision * recall) / (precision + recall)

        return {"n_events": self.events.shape[0],
                "n_tags": len(self.matches.tag_index.unique()),
                "true_positive_events": true_pos_events,
                "true_positive_tags": true_pos_tags,
                "false_negative": false_neg,
                "n_tags_matched": n_tags_matched,
                "precision": precision,
                "recall": recall,
                "F1_score": f1_score}

    def evaluate(self, recordings, tags):
        self.get_events()
        self.associate_recordings(recordings)
        self.get_matches(tags)
        # print("Took %0.6fs to match events" % (time.time() - tic))
        # tic = time.time()
        stats = self.get_stats()
        # print("Took %0.6fs to get_stats" % (time.time() - tic))
        print("Stats for options {0}: {1}".format(self.options, stats))
        return [self.options, stats, self.events]
