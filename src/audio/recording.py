from db.models import BaseModel

from pysoundplayer import audio


class Recording(BaseModel):

    # TODO: load from file_path only
    def __init__(self, attributes):
        # TODO: load from path
        BaseModel.__init__(self, attributes)
        self.audio = None

    def create_spectrogram(self, spec_opts=None):
        if not self.audio:
            self.load_audio()
        return self.audio.get_spectrogram(spec_opts)

    def load_audio(self, sr=None, **kwargs):

        # TODO: externalize supported types
        if self.ext.lower() in ["wav", "flac"]:
            self.audio = audio.Audio(self.path, sr, **kwargs)
        else:
            raise ValueError("Unsupported audio file type")

    def __str__(self):
        string = "Audio file of type {0.ext}, with id {0.id} recorded on {0.date}".format(
            self)
        return string
