import os.path
from datetime import datetime

import numpy as np


class AudioExtract:
    def __init__(self, audio, sr):
        self.audio = audio
        self.sr = sr
        self.length = len(self.audio)
        self.duration = round(self.length / sr, 2)

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


class ExtractInfo:
    def __init__(self, path, audio_type):
        filename = os.path.basename(path)
        infos = filename.split(".")
        self.name = infos[0]
        self.ext = infos[1].lower()
        if audio_type is "songmeter":
            self.__extract_SM_info(infos[0])
        else:
            self.id = infos[0]
            self.date = "Unknown"

    # SongMeter format:
    # SITEID_DATE_TIME
    # SITEID : str
    # DATE: YYYYMMDD
    # TIME: HHMMSS
    def __extract_SM_info(self, path):
        res = path.split("_", 1)
        self.id = res[0]
        self.date = datetime.strptime(res[1], "%Y%m%d_%H%S%M")

    def __str__(self):
        string = "Audio file of type {0.ext}, with id {0.id} recorded on {0.date}".format(
            self)
        return (string)
