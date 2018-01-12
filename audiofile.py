import librosa


class AudioFile:
    def __init__(self, audio, sr):
        self.audio = audio
        self.sr = sr
        self.length = len(self.audio)
        self.duration = round(self.length / sr, 2)


class RecordingId:
    def __init__(self, path, audio_type):
        self.id = "id"


class Recording(AudioFile):
    def __init__(self, path, audio_type="songmeter"):
        super().__init__(*librosa.load(path, sr=None))
        self.id = RecordingId(path, audio_type)

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
            self.id,
            start=start_frame)


class Sample(AudioFile):
    def __init__(self, audio, sr, sample_id, start):
        super().__init__(audio, sr)
        self.start = start
        self.id = sample_id
        self.spectrograms = []

    def generate_spectrograms(self, specgen):
        self.spectrograms = specgen.create_spectrograms(self)
