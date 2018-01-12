import librosa


class AudioFile:
    def __init__(self, audio, sr, start=0):
        self.audio = audio
        self.sr = sr
        self.length = len(self.audio)


class Recording(AudioFile):
    def __init__(self, path):
        AudioFile.__init__(self, *librosa.load(path, sr=None))
        self.path = path

    def getSample(self, start, duration):
        # Convert starting time to frames
        start_frame = start * self.sr

        # if starting frame is greater than file length, raise an Exception
        if start_frame > self.length:
            raise ValueError('Starting value greater than file length')

        # get end frame from duration of sample
        end_frame = start_frame + duration * self.sr
        # make sure we don't get over file length
        if end_frame > self.length:
            end_frame = self.length

        return AudioFile(
            self.audio[start_frame:end_frame], self.sr, start=start)
