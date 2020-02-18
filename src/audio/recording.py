from db.models import BaseModel

from pysoundplayer import audio


class Recording(BaseModel):

    # TODO: load from file_path only
    def __init__(self, attributes):
        # TODO: load from path
        # super(self.__class__, self).__init__(*args, **kwargs)
        BaseModel.__init__(self, attributes)
        #sample.Sample.__init__(self, spec_opts=spec_opts)
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

    def create_spectrogram(self, spec_opts=None):
        if not self.audio:
            self.load_audio()
        return self.audio.get_spectrogram(spec_opts)

    def load_audio(self, sr=None, **kwargs):

        # TODO: externalize supported types
        if self.ext.lower() in ["wav", "flac"]:
            self.audio = audio.Audio(self.path, sr, **kwargs)
            #(self.audio, self.sr) = (librosa.load(self.path, sr=sr))
        else:
            raise ValueError("Unsupported audio file type")

    # def get_sample(self, start, duration, sr=None):
    #     if not self.audio:
    #         self.load_audio(sr)

    #     # Convert starting time to frames
    #     start_frame = start * self.sr

    #     # if starting frame is greater than file length, raise an Exception
    #     if start_frame > self.length:
    #         raise ValueError('Starting value is greater than file length')

    #     # get end frame from duration of sample
    #     end_frame = start_frame + duration * self.sr
    #     # make sure we don't get over file length
    #     if end_frame > self.length:
    #         end_frame = self.length

    #     return sample.Sample(
    #         self.audio[start_frame:end_frame],
    #         self.sr,
    #         start=start_frame,
    #         duration=duration)

    def __str__(self):
        string = "Audio file of type {0.ext}, with id {0.id} recorded on {0.date}".format(
            self)
        return string
