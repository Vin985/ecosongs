import numpy as np


class ACI:

    COLUMNS = ["ACI", "recording_id", "year", "site",
               "plot", "date", "duration", "time_step"]

    def __init__(self, recording=None, spectro=None, time_step=5, unit="seconds", spec_opts={}):
        if recording:
            print("Computing ACI for:" + recording.path)
        if not spectro:
            spectro = recording.get_spectrogram(spec_opts)
        spec = spectro.spec
        if time_step is None:
            j_bin = spec.shape[1]
        else:
            if unit == "seconds":
                j_bin = int(time_step * spec.shape[1] / spectro.duration)
            elif unit == "frames":
                j_bin = time_step

        # alternative time indices to follow the R code
        times = range(0, spec.shape[1] - 10, j_bin)
        # sub-spectros of temporal size j
        jspecs = [np.array(spec[:, i:i + j_bin]) for i in times]
        # list of ACI values on each jspecs
        aci = [
            sum((np.sum(abs(np.diff(jspec)), axis=1) / np.sum(jspec, axis=1)))
            for jspec in jspecs
        ]
        self.temporal_values = aci
        self.ACI = sum(aci)
        self.time_step = time_step
        self.path = recording.path
        self.duration = spectro.duration
        self.date = recording.date
        self.site = recording.site
        self.plot = recording.plot
        self.recording_id = 1
        self.year = recording.year

    def __str__(self):
        return ("Global ACI: {0.main}".format(self))

    def to_dict(self):
        return {key: getattr(self, key) for key in self.COLUMNS}
