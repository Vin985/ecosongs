import cv2
import numpy as np
import scipy.ndimage as ndimage

# Remove single spots from an image


def filter_isolated_cells(array, struct):

    filtered_array = np.copy(array)
    id_regions, num_ids = ndimage.label(filtered_array, structure=struct)
    id_sizes = np.array(ndimage.sum(array, id_regions, range(num_ids + 1)))
    area_mask = (id_sizes == 1)
    filtered_array[area_mask[id_regions]] = 0

    return filtered_array


class Sample:
    def __init__(self, audio, sr, start=0):
        self.audio = audio
        self.sr = sr
        self.start = start
        self.spectrogram = None

    @property
    def length(self):
        """
        Length in frames of the audio extract
        """
        return len(self.audio)

    @property
    def duration(self):
        """
        Duration is length divided by sample rate
        """
        return round(self.length / self.sr, 2)

    def get_spectrogram(self, specgen, n_fft=None):
        if not self.spectrogram:
            self.spectrogram = specgen.create_spectrogram(self, n_fft)
        return (self.spectrogram)

    # def get_ACI(self, time_step=None, unit="seconds"):
    #     self.ACI = ACI(self.get_spectrogram(), time_step, unit)
    #     return (self.ACI)

    def get_SNR(self,
                frame_length_e=512,
                min_DB=-60,
                window_smoothing_e=5,
                activity_threshold_dB=3,
                hist_number_bins=100,
                dB_range=10,
                N=0):
        """

        Computes indices from the Signal to Noise Ratio of a waveform.

        window_smoothing_e: odd number for sliding mean smoothing of the
            histogram (can be 3, 5 or 7)
        hist_number_bins - Number of columns in the histogram
        dB_range - dB range to consider in the histogram
        N: The decibel threshold for the waveform is given by the modal
            intensity plus N times the standard deviation. Higher values of N
            will remove more energy from the waveform.

        Output:
            Signal-to-noise ratio (SNR): the decibel difference between the
                maximum envelope amplitude in any minute segment and the
                background noise.
            Acoustic activity: the fraction of frames within a one minute
                segment where the signal envelope is more than 3 dB above
                the level of background noise
            Count of acoustic events: the number of times that the signal
                envelope crosses the 3 dB threshold
            Average duration of acoustic events: an acoustic event is a portion
                of recordingwhich startswhen the signal envelope crosses above
                the 3 dB threshold and ends when it crosses belowthe 3 dB
                threshold.

        Ref: Towsey, Michael W. (2013) Noise removal from wave-forms and
        spectrograms derived from natural recordings of the environment.
        """

        times = range(0, len(self.audio) - frame_length_e + 1, frame_length_e)
        wave_env = 20 * np.log10(
            [np.max(abs(self.audio[i:i + frame_length_e])) for i in times])

        minimum = np.max(
            (np.min(wave_env), min_DB)
        )  # If the minimum value is less than -60dB, the minimum is set to -60dB

        hist, bin_edges = np.histogram(
            wave_env,
            range=(minimum, minimum + dB_range),
            bins=hist_number_bins,
            density=False)
        half_ws = int(window_smoothing_e / 2)
        hist_smooth = ([
            np.mean(hist[i - half_ws:i + half_ws])
            for i in range(half_ws, len(hist) - half_ws)
        ])
        hist_smooth = np.concatenate((np.zeros(half_ws), hist_smooth,
                                      np.zeros(half_ws)))

        modal_intensity = np.argmax(hist_smooth)

        if N > 0:
            count_thresh = 68 * sum(hist_smooth) / 100
            count = hist_smooth[modal_intensity]
            index_bin = 1
            while count < count_thresh:
                if modal_intensity + index_bin <= len(hist_smooth):
                    count = count + hist_smooth[modal_intensity + index_bin]
                if modal_intensity - index_bin >= 0:
                    count = count + hist_smooth[modal_intensity - index_bin]
                index_bin += 1
            thresh = np.min((hist_number_bins,
                             modal_intensity + N * index_bin))
            background_noise = bin_edges[thresh]
        elif N == 0:
            background_noise = bin_edges[modal_intensity]

        SNR = np.max(wave_env) - background_noise
        SN = np.array([
            frame - background_noise - activity_threshold_dB
            for frame in wave_env
        ])
        acoustic_activity = np.sum([i > 0 for i in SN]) / float(len(SN))

        # Compute acoustic events
        start_event = [n[0] for n in np.argwhere((SN[:-1] < 0) & (SN[1:] > 0))]
        end_event = [n[0] for n in np.argwhere((SN[:-1] > 0) & (SN[1:] < 0))]
        if len(start_event) != 0 and len(end_event) != 0:
            if start_event[0] < end_event[0]:
                events = list(zip(start_event, end_event))
            else:
                events = list(zip(end_event, start_event))
            count_acoustic_events = len(events)
            average_duration_e = np.mean(
                [end - begin for begin, end in events])
            average_duration_s = average_duration_e * self.duration / float(
                len(SN))
        else:
            count_acoustic_events = 0
            average_duration_s = 0

        dict = {
            'SNR': SNR,
            'Acoustic_activity': acoustic_activity,
            'Count_acoustic_events': count_acoustic_events,
            'Average_duration': average_duration_s
        }
        return dict

    # Decide if given spectrum shows bird sounds or noise only

    def has_bird(self, imgen, threshold=16):

        # working copy
        #img = self.get_spectrogram().spec.copy()
        # img = imgen.create_composite_part(self.get_spectrogram(),
        #                                   (255, 0, 0)).copy()
        img = imgen.spec2img(self.get_spectrogram().spec, (255, 0, 0))
        img = img.convert('L')
        img = np.asarray(img).copy()
        # STEP 1: Median blur
        #img = cv2.medianBlur(img, 5)
        # cv2.imshow('SPEC', img)
        # cv2.waitKey(-1)

        # STEP 2: Median threshold
        col_median = np.median(img, axis=0, keepdims=True)
        row_median = np.median(img, axis=1, keepdims=True)

        img[img < row_median * 3] = 0
        img[img < col_median * 4] = 0
        img[img > 0] = 1

        # STEP 3: Remove singles
        img = filter_isolated_cells(img, struct=np.ones((3, 3)))

        # STEP 4: Morph Closing
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE,
                               np.ones((5, 5), np.float32))
        cv2.imshow('SPEC', img)
        cv2.waitKey(-1)
        # STEP 5: Frequency crop
        img = img[128:-16, :]
        cv2.imshow('SPEC', img)
        cv2.waitKey(-1)
        # STEP 6: Count columns and rows with signal
        # (Note: We only use rows with signal as threshold, but columns might come
        # in handy in other scenarios)

        # column has signal?
        col_max = np.max(img, axis=0)
        col_max = ndimage.morphology.binary_dilation(
            col_max, iterations=2).astype(col_max.dtype)
        # cthresh = col_max.sum()

        # row has signal?
        row_max = np.max(img, axis=1)
        row_max = ndimage.morphology.binary_dilation(
            row_max, iterations=2).astype(row_max.dtype)
        rthresh = row_max.sum()

        # final threshold
        thresh = rthresh

        # DBUGB: show?
        # print thresh
        # cv2.imshow('BIRD?', img)
        # cv2.waitKey(-1)

        # STEP 7: Apply threshold (Default = 16)
        bird = True
        if thresh < threshold:
            bird = False

        return bird, thresh
