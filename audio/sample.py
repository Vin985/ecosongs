from analyse.indexes import ACI
from audio.extract import AudioExtract


class Sample(AudioExtract):
    def __init__(self, audio, sr, specgen, start=0, infos=None):
        super().__init__(audio, sr)
        self.start = start
        if infos:
            self.infos = infos
        self.specgen = specgen
        self.spectrogram = None

    def get_spectrogram(self, n_fft=None):
        if not self.spectrogram:
            self.spectrogram = self.specgen.create_spectrogram(self, n_fft)
        return (self.spectrogram)

    def get_ACI(self, time_step=None, unit="seconds"):
        self.ACI = ACI(self.get_spectrogram(), time_step, unit)
        return (self.ACI)
