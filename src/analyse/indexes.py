import numpy as np


class ACI:
    def __init__(self, spectro, time_step=None, unit="seconds"):
        spec = spectro.spec
        if time_step is None:
            times = 1
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
        self.main = sum(aci)
        self.temporal_step = time_step

    def __str__(self):
        return ("Global ACI: {0.main}".format(self))
