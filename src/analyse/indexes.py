import numpy as np

from db.models import BaseModel, TableModel


def compute_index(index_type, *args, **kwargs):
    print(args)
    print(kwargs)
    index = globals()[index_type]
    if index:
        idx = index(*args, **kwargs)
        return idx.compute()
    return()


class AudioIndex(BaseModel):

    def __init__(self, attrs):
        print(attrs)
        BaseModel.__init__(self, attrs)

    def compute(self):
        pass


class ACITable(TableModel):
    TABLE_NAME = "ACI"

    def __init__(self, df=None, dbmanager=None):
        TableModel.__init__(self, ACI.COLUMNS, df=df, dbmanager=dbmanager)


class ACI(AudioIndex):

    # pylint: disable=too-many-instance-attributes

    COLUMNS = ["recording_id", "ACI", "year", "site",
               "plot", "date", "duration", "time_step", "denoised"]

    def __init__(self, values=None, recording=None, spectro=None, time_step=5,
                 unit="seconds", spec_opts=None):
        super().__init__(values)
        spec_opts = spec_opts or {}
        if not values:
            if recording:
                print("Computing ACI for:" + recording.path)
            if not spectro:
                spectro = recording.get_spectrogram(spec_opts)
            self.unit = unit
            self.time_step = time_step
            self.recording_id = recording.id
            self.date = recording.date
            self.site = recording.site
            self.plot = recording.plot
            self.year = recording.year
            self.spec = spectro.spec
            self.denoised = spectro.denoised
            self.duration = spectro.duration

    def compute(self):
        if self.time_step is None:
            j_bin = self.spec.shape[1]
        else:
            if self.unit == "seconds":
                j_bin = int(self.time_step
                            * self.spec.shape[1] / self.duration)
            elif self.unit == "frames":
                j_bin = self.time_step

        # alternative time indices to follow the R code
        times = range(0, self.spec.shape[1] - 10, j_bin)
        # sub-spectros of temporal size j
        jspecs = [np.array(self.spec[:, i:i + j_bin]) for i in times]
        # list of ACI values on each jspecs
        aci = [
            sum((np.sum(abs(np.diff(jspec)), axis=1) / np.sum(jspec, axis=1)))
            for jspec in jspecs
        ]
        self.temporal_values = aci
        self.ACI = sum(aci)
        return self.to_dict()

    def __str__(self):
        return "Global ACI: {0.ACI}".format(self)
