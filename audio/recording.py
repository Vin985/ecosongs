import librosa

from audio.extract import ExtractInfo
from audio.sample import Sample


class Recording(Sample):
    def __init__(self, path, specgen, audio_type="songmeter"):
        self.path = path
        self.infos = ExtractInfo(path, audio_type)
        super().__init__(*self.__loadAudioFile(), specgen)

    def __loadAudioFile(self):
        # TODO: externalize supported types
        if self.infos.ext in ["wav", "flac"]:
            return (librosa.load(self.path, sr=None))
        else:
            raise ValueError("Unsupported audio file type")

    def getSample(self, start, duration):
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

        return Sample(
            self.audio[start_frame:end_frame],
            self.sr,
            self.specgen,
            start=start_frame,
            infos=self.infos)
