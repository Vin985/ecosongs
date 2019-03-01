import time

import librosa

from audio import sample
from db.models import BaseModel, TableModel


class RecordingTable(TableModel):
    TABLE_NAME = "recordings"
    DUPLICATE_COLUMNS = ["name", "plot", "site", "year"]

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, Recording.COLUMNS, df=df, dbmanager=dbmanager)
        self.recordings = {}

    def load_recordings(self, indexes, spec_opts=None):
        """Create Recording objects from indexes if they had not been loaded
        in memory before.

        Parameters
        ----------
        indexes : type
            Description of parameter `indexes`.

        Returns
        -------
        type
            Description of returned object.

        """
        to_load = [idx for idx in indexes if idx not in self.recordings]
        if to_load:
            to_load = self._df.iloc[indexes]
            to_update = {row.Index: Recording(row._asdict(), spec_opts=spec_opts) for row in to_load.itertuples(index=True)}
            self.recordings.update(to_update)
        return [self.recordings[idx] for idx in indexes]


class Recording(BaseModel, sample.Sample):

    COLUMNS = ["name", "year", "site",
               "plot", "date", "path",
               "ext", "recorder", "duration", "sample_rate"]  # , "old_name"]
    #
    # def __init__(self, filepath, recorder=None, model=None):
    #     self.filepath = filepath
    #     if not model:
    #         infos = metadata.extract_from_file(filepath, recorder)
    #     self.model = models.RecordingModel(filepath=filepath, **infos)
    #     self.audio = None

    # TODO: load from file_path only
    def __init__(self, attributes, spec_opts=None):
        # TODO: load from path
        # super(self.__class__, self).__init__(*args, **kwargs)
        BaseModel.__init__(self, attributes)
        sample.Sample.__init__(self, spec_opts=spec_opts)

    # @property
    # def name(self):
    #     """
    #     Docstring for name property
    #     """
    #     return self.model.name
    #
    # @name.setter
    # def name(self, name):
    #     """
    #     Docstring for name property
    #     """
    #     self.model.name = name

    def create_spectrogram(self, spec_opts=None):
        if not self.audio.size:
            self.load_audio()
        return super().create_spectrogram(spec_opts)

    def load_audio(self, sr=None):
        # TODO: externalize supported types
        if self.ext.lower() in ["wav", "flac"]:
            (self.audio, self.sr) = (librosa.load(self.path, sr=sr))
        else:
            raise ValueError("Unsupported audio file type")

    def get_sample(self, start, duration, sr=None):
        if not self.audio.size:
            self.load_audio(sr)

        # Convert starting time to frames
        start_frame = start * self.sr

        # if starting frame is greater than file length, raise an Exception
        if start_frame > self.length:
            raise ValueError('Starting value is greater than file length')

        # get end frame from duration of sample
        end_frame = start_frame + duration * self.sr
        # make sure we don't get over file length
        if end_frame > self.length:
            end_frame = self.length

        return sample.Sample(
            self.audio[start_frame:end_frame],
            self.sr,
            start=start_frame,
            duration=duration)

    def __str__(self):
        string = "Audio file of type {0.ext}, with id {0.id} recorded on {0.date}".format(
            self)
        return string
