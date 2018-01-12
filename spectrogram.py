import librosa
import numpy as np

from compute_indice import remove_noiseInSpectro


class SpectrogramGenerator:
    def __init__(self, params):
        # spectrogram parameters
        self.params = params
        print(params)

    # TODO : add other params to spectrogram
    def create_spectrogram(self, sample, n_fft):
        spectro = librosa.stft(
            sample.audio, n_fft, window=self.params['window'])
        mag, phase = librosa.magphase(spectro)

        specdb = librosa.amplitude_to_db(spectro, ref=np.max)
        if (self.params['remove_noise']):
            specdb = remove_noiseInSpectro(
                specdb,
                histo_relative_size=self.params['hist_rel_size'],
                window_smoothing=self.params['window_smoothing'])
            specdb = specdb.astype("float32")

        return Spectrogram(specdb, n_fft, sample.duration, self.params)

    def create_spectrograms(self, sample):
        return ([
            self.create_spectrogram(sample, fft) for fft in self.params['ffts']
        ])


class Spectrogram:
    # TODO : store spectrogram results with params
    def __init__(self, spec, n_fft, duration, params):
        self.spec = spec
        self.fft = n_fft
        self.duration = duration
        self.params = params
