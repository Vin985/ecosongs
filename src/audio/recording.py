import librosa
from utils.basemodel import BaseModel

from audio import sample


class Recording(BaseModel, sample.Sample):

    COLUMNS = ["name", "year", "site",
               "plot", "date", "path",
               "ext", "recorder", "error"]
    #
    # def __init__(self, filepath, recorder=None, model=None):
    #     self.filepath = filepath
    #     if not model:
    #         infos = metadata.extract_from_file(filepath, recorder)
    #     self.model = models.RecordingModel(filepath=filepath, **infos)
    #     self.audio = None

    def __init__(self, *args, **kwargs):
        # TODO: load from path
        BaseModel.__init__(self, *args, **kwargs)
        self.audio = None

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

    def load_audio(self, sr):
        # TODO: externalize supported types
        if self.ext.lower() in ["wav", "flac"]:
            (self.audio, self.sr) = (librosa.load(self.path, sr=sr))
        else:
            raise ValueError("Unsupported audio file type")

    def get_sample(self, start, duration, sr=None):
        if not self.audio:
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
            start=start_frame)

    def __str__(self):
        string = "Audio file of type {0.ext}, with id {0.id} recorded on {0.date}".format(
            self)
        return (string)
