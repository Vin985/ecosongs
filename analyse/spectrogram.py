import librosa
import numpy as np

from analyse.compute_indice import remove_noiseInSpectro


class Spectrogram:
    def __init__(self, spec, n_fft, duration, sr, config):
        self.spec = spec
        self.fft = n_fft
        self.duration = duration
        self.sr = sr
        self.config = config

    def __str__(self):
        string = "Spectrogram with fft: {0.fft}, shape {1} and value \n {0.spec}".format(
            self, self.spec.shape)
        return (string)


class SpectrogramGenerator:
    def __init__(self, config):
        # spectrogram parameters
        self.config = config

    # TODO : add other params to spectrogram
    def create_spectrogram(self, sample, n_fft):
        if not n_fft:
            n_fft = self.config['default_fft']
        spectro = librosa.stft(
            sample.audio, n_fft, window=self.config['window'])
        mag, phase = librosa.magphase(spectro)

        specdb = librosa.amplitude_to_db(spectro, ref=np.max)
        if self.config['remove_noise']:
            specdb = self.remove_noise(specdb)
            specdb = specdb.astype("float32")

        return Spectrogram(specdb, n_fft, sample.duration, sample.sr,
                           self.config)

    def remove_noise(self, spectro):
        """
        Compute a new spectrogram which is "Noise Removed".

        spectro: spectrogram of the audio signal
        Options to be configured in conf file:
        histo_relative_size: ratio between the size of the spectrogram and
           the size of the histogram
        window_smoothing: number of points to apply a mean filtering on the
           histogram and on the background noise curve
        N: Parameter to set the threshold around the modal intensity

        Output:
            Noise removed spectrogram

        Ref: Towsey, Michael W. (2013) Noise removal from wave-forms and
           spectrograms derived from natural recordings of the environment.
           Queensland University of Technology, Brisbane.
        """

        # Min value for the new spectrogram (preferably slightly higher than 0)
        low_value = 1.e-07
        N = self.config['N']

        len_spectro_e = spectro.shape[0]
        histo_size = int(len_spectro_e / self.config['hist_rel_size'])

        background_noise = []
        for row in spectro:
            hist, bin_edges = np.histogram(row, bins=histo_size, density=False)

            ws = int(self.config['window_smoothing'] / 2)
            hist_smooth = ([
                np.mean(hist[i - ws:i + ws])
                for i in range(ws, len(hist) - ws)
            ])
            hist_smooth = np.concatenate((np.zeros(ws), hist_smooth,
                                          np.zeros(ws)))

            modal_intensity = int(
                np.min([np.argmax(hist_smooth), 95 * histo_size / 100
                        ]))  # test if modal intensity value is in the top 5%
            if N > 0:
                count_thresh = 68 * sum(hist_smooth) / 100
                count = hist_smooth[modal_intensity]
                index_bin = 1
                while count < count_thresh:
                    if modal_intensity + index_bin < len(hist_smooth):
                        count = count + hist_smooth[modal_intensity
                                                    + index_bin]
                    if modal_intensity - index_bin >= 0:
                        count = count + hist_smooth[modal_intensity
                                                    - index_bin]
                    index_bin += 1
                thresh = int(
                    np.min((histo_size, modal_intensity + N * index_bin)))
                background_noise.append(bin_edges[thresh])
            elif N == 0:
                background_noise.append(bin_edges[modal_intensity])

        background_noise_smooth = ([
            np.mean(background_noise[i - ws:i + ws])
            for i in range(ws, len(background_noise) - ws)
        ])
        # keep background noise at the end to avoid last row problem
        # (last bin with old microphones)
        background_noise_smooth = np.concatenate(
            (background_noise[0:(ws)], background_noise_smooth,
             background_noise[-(ws):]))

        new_spec = np.array(
            [col - background_noise_smooth for col in spectro.T]).T
        # replace negative values by value close to zero
        new_spec = new_spec.clip(min=low_value)

        return new_spec
