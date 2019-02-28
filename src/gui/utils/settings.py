import logging

from PySide2.QtCore import QSettings

import utils.commons as utils


class Settings(QSettings):
    # def __init__(self):
    #     super(self.__class__, self).__init__()

    GROUP_SPECTROGRAM = "spectrogram"

    @property
    def spec_fft(self):
        return int(self.value("/spectrogram/default_fft", 512))

    @property
    def sites_path(self):
        return str(self.value("sites_path", "../conf/sites.csv"))

    @property
    def db_name(self):
        return str(self.value("database/name", "ecosongs"))

    @property
    def db_type(self):
        return str(self.value("database/type", "hdf5"))

    @property
    def db_path(self):
        return str(self.value("database/path", "db"))

    def spectrogram_settings(self, context=""):
        group = self.GROUP_SPECTROGRAM
        res = {}
        # Spectrogram settings
        if context:
            context = "/" + context
        self.beginGroup(group + context)
        if context and not self.childKeys():
            logging.info("No entries found for selected context, using default group")
            self.endGroup()
            self.beginGroup(group)
        res["spec_window"] = self.value("window", "Hanning")
        res["n_fft"] = int(self.value("n_fft", 512))
        res["to_db"] = utils.str2bool(self.value("to_db", "True"))
        res["normalize"] = utils.str2bool(self.value("normalize", "True"))
        hop_length = self.value("hop_length")
        res["spec_hop_length"] = int(hop_length) if hop_length else None
        res["scale"] = self.value("scale", "Linear")
        res["remove_noise"] = utils.str2bool(self.value("remove_noise", "True"))
        res["nr_hist_rel_size"] = int(self.value("nr_hist_rel_size", 2))
        res["nr_N"] = float(self.value("nr_N", 0.1))
        res["nr_window_smoothing"] = int(self.value("nr_window_smoothing", 5))
        self.endGroup()
        return res

    def image_settings(self):
        res = {}
        self.beginGroup("image")
        res["color_masks_str"] = list(self.value("color_masks", ["red", "lime", "blue"]))
        res["contrast"] = int(self.value("contrast", 0))
        res["invert_colors"] = utils.str2bool(self.value("invert_colors", "False"))
        composite_ffts = list(self.value("composite_ffts", [128, 512, 2048]))
        res["composite_ffts"] = [int(i) for i in composite_ffts]
        self.endGroup()
        return res
