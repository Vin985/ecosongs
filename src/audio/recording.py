import librosa
import pandas as pd
from utils.basemodel import BaseModel

from audio import sample


class Recordings():
    TABLE_NAME = "recordings"

    def __init__(self, df=pd.DataFrame(), dbmanager=None):
        self._df = df
        # TODO: Change to externalize dbmanager
        self.dbmanager = dbmanager
        self.recordings = {}

    def load_data(self):
        try:
            self._df = self.dbmanager.get_table(self.TABLE_NAME)
            print(self._df.dtypes)
            print(self._df)
            return(self._df.loc[:, self._df.columns.intersection(Recording.COLUMNS)])
            # self._df["date"] = pd.to_datetime(self._df["date"])
        except KeyError:
            self._df

    @property
    def df(self):
        if self._df.empty:
            self.load_data()
        return self._df

    @property
    def empty(self):
        return self._df.empty

    def query(self, query):
        return self._df.query(query)

    def append(self, new, save=False):
        # TODO: check duplicates
        # TODO: add idx column?
        self._df = self._df.append(new, ignore_index=True, sort=True)
        if save:
            self.dbmanager.save_data(self.TABLE_NAME, self._df, format="table")

    def load_recordings(self, indexes, specgen):
        """Create Recording objects from indexes if they had not been loaded
        in memory before.

        Parameters
        ----------
        indexes : type
            Description of parameter `indexes`.
        specgen : spectogram generator
            Description of parameter `specgen`.

        Returns
        -------
        type
            Description of returned object.

        """
        to_load = [idx for idx in indexes if idx not in self.recordings]
        if to_load:
            to_load = self._df.iloc[indexes]
            self.recordings.update({row.Index: Recording(row._asdict(), specgen=specgen) for row in to_load.itertuples(index=True)})
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
    def __init__(self, attrs, specgen=None):
        # TODO: load from path
        # super(self.__class__, self).__init__(*args, **kwargs)
        BaseModel.__init__(self, attrs)
        sample.Sample.__init__(self, specgen=specgen)

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
            specgen=self.specgen,
            duration=duration)

    def __str__(self):
        string = "Audio file of type {0.ext}, with id {0.id} recorded on {0.date}".format(
            self)
        return (string)