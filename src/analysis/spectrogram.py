import librosa
import numpy as np


class Spectrogram:

    def __init__(self, sample, n_fft=None, to_db=None, pcen=None,
                 remove_noise=None, normalize=None,
                 hop_length=-1, spec_window=-1, scale="Linear",
                 nr_hist_rel_size=2, nr_N=0.1, nr_window_smoothing=5):

        self.n_fft = n_fft

        self.duration = sample.duration
        self.sr = sample.sr
        self.to_db = to_db
        self.pcen = pcen
        self.denoised = remove_noise
        self.window = spec_window
        self.hop_length = hop_length
        self.scale = scale
        self.normalize = normalize
        self.nr_N = nr_N
        self.nr_hist_rel_size = nr_hist_rel_size
        self.nr_window_smoothing = nr_window_smoothing

        self.spec = self.create_spectrogram(sample)

    def create_spectrogram(self, sample):
        spectro = librosa.stft(
            sample.audio, self.n_fft, hop_length=self.hop_length, window=self.window)

        if self.scale == "Mel":
            spectro = librosa.feature.melspectrogram(S=spectro)

        spec = np.abs(spectro)

        if self.pcen:
            # TODO: test this!!!
            return librosa.pcen(spec * (2**31))

        if self.denoised:
            # TODO: check SNR to remove noise?
            spec = self.remove_noise(spec, self.nr_N,
                                     self.nr_hist_rel_size, self.nr_window_smoothing)
            spec = spec.astype("float32")

        if self.normalize:
            spec = librosa.util.normalize(spec)

        if self.to_db:
            spec = librosa.amplitude_to_db(spec, ref=np.max)

        return spec

    def get_subspec(self, start, duration):
        fps = self.spec.shape[1] / self.duration
        start_frame = int(start * fps)
        end_frame = int(start_frame + duration * fps)
        return self.spec[..., start_frame:end_frame]

    @staticmethod
    def remove_noise(spectro, N=0.1, hist_rel_size=2, window_smoothing=5):
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

        len_spectro_e = spectro.shape[0]
        histo_size = int(len_spectro_e / hist_rel_size)

        background_noise = []
        for row in spectro:
            hist, bin_edges = np.histogram(row, bins=histo_size, density=False)

            ws = int(window_smoothing / 2)
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

    def __str__(self):
        string = "Spectrogram with fft: {0.fft}, shape {1} and value \n {0.spec}".format(
            self, self.spec.shape)
        return (string)
