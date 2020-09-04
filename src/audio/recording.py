from db.dbmodels import BaseDBModel
from pysoundplayer import audio
from utils.commons import is_df_empty

from analysis.detection.detectors import DETECTORS


class Recording(BaseDBModel):

    NO_TAG = 0
    TAGS_INCOMPLETE = 1
    TAGS_COMPLETE = 2

    # TODO: load from file_path only
    def __init__(self, attributes):
        # TODO: load from path
        BaseModel.__init__(self, attributes)
        self.audio = None
        self.predictions = None
        self.tags = None
        self.events = None
        self.event_options = None
        self.matched = None
        self.stats = {}

    def create_spectrogram(self, spec_opts=None):
        if not self.audio:
            self.load_audio()
        return self.audio.get_spectrogram(spec_opts)

    def load_audio(self, sr=None, **kwargs):
        if not self.audio:
            # TODO: externalize supported types
            if self.ext.lower() in ["wav", "flac"]:
                self.audio = audio.Audio(self.path, sr, **kwargs)
            else:
                raise ValueError("Unsupported audio file type")

    def __str__(self):
        string = "Audio file of type {0.ext}, with id {0.id} recorded on {0.date}".format(
            self
        )
        return string

    def tag_status(self, complete=True):
        if is_df_empty(self.tags):
            return 0
        if complete:
            return int(self.has_tags == self.TAGS_COMPLETE)
        return self.has_tags

    def get_events(self, event_options):
        if (
            self.events is None or self.event_options != event_options
        ) and not self.predictions.empty:
            print("recalculating events")
            detector = DETECTORS[event_options.get("method", "standard")]
            if self.tag_status(complete=True):
                self.evaluate_annotations(event_options)
            else:
                self.events = detector.get_events(self.predictions, event_options)
            self.event_options = event_options
        return self.events

    def get_tags(self, event_options):
        if self.tag_status(complete=True) and not self.events.empty:
            if self.matched is None or self.event_options != event_options:
                print("recalculating tags")
                self.evaluate_annotations(event_options)
                self.event_options = event_options
        return self.tags

    def evaluate_annotations(self, options):
        detector = DETECTORS[options.get("method", "standard")]
        stats = detector.evaluate(self.predictions, self.tags, options)
        self.events = stats["events"]
        self.tags = stats["tags"]
        self.matched = stats["matched"]
        self.stats = stats["stats"]

    def get_stats(self, event_options, match_options):
        events = self.get_events(event_options)
        if not is_df_empty(events) and not is_df_empty(self.tags):
            detector = DETECTORS[event_options.get("method", "standard")]
            matches = detector.get_matches(self.events, self.tags)
            stats = detector.get_stats(events, self.tags, matches, match_options)
            return stats
        return None

    def get_event_overlap(self, event_id):
        if self.matched is not None and not self.matched.empty:
            res = self.matched.loc[self.matched.event_id == event_id, "event_overlap"]
            if not res.empty:
                return res.values[0]
        return 0

    def get_tag_overlap(self, tag_id):
        if self.matched is not None and not self.matched.empty:
            res = self.matched.loc[self.matched.tag_id == tag_id, "tag_overlap"]
            if not res.empty:
                return res.values[0]
        return 0
