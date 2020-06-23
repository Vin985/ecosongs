import math
import multiprocessing as mp

import yaml
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget

from gui.widgets.options.ui.detector_options_ui import Ui_DetectorOptions


class DetectorOptions(QWidget, Ui_DetectorOptions):

    # TODO: externalize this!
    MAX_CHUNKSIZE = 100
    MIN_SIZE_PROCESS = 10

    detect_songs = Signal()
    cancelling = Signal()

    def __init__(self, parent, n_recordings, export_pdf=False):
        super().__init__(parent)
        self.setupUi(self)
        # Set settings to local to avoid saving them unless asked
        # TODO: allow saving settings
        self.export_pdf = export_pdf
        self.n_recordings = n_recordings
        self.init_ui()
        self.link_events()

    def link_events(self):
        self.checkbox_chunk_percent.clicked.connect(self.set_slider_chunksize_max)

    def init_ui(self):
        if self.export_pdf:
            self.checkbox_save.setChecked(False)
            self.checkbox_save.hide()
            self.checkbox_overwrite.setChecked(False)
            self.checkbox_overwrite.hide()

        n_cpu = mp.cpu_count()
        self.slider_nprocess.setMaximum(n_cpu)
        self.set_slider_chunksize_max()
        self.calculate_optimal_chunksize()

    def calculate_optimal_chunksize(self):
        n_cpu = mp.cpu_count()
        recommended_n_process = min(
            math.ceil(self.n_recordings / self.MIN_SIZE_PROCESS), n_cpu
        )
        recommended_chunksize = min(
            self.n_recordings / recommended_n_process, self.MAX_CHUNKSIZE
        )
        if self.checkbox_chunk_percent.isChecked():
            recommended_chunksize = math.ceil(
                recommended_chunksize / self.n_recordings * 100
            )

        self.slider_nprocess.setValue(recommended_n_process)
        self.slider_chunk_size.setValue(recommended_chunksize)

    def set_slider_chunksize_max(self):
        old_chunk = self.slider_chunk_size.value()
        if self.checkbox_chunk_percent.isChecked():
            self.slider_chunk_size.setMaximum(100)
            self.slider_chunk_size.setValue(
                math.ceil(old_chunk / self.n_recordings * 100)
            )
        else:
            self.slider_chunk_size.setMaximum(self.n_recordings)
            self.slider_chunk_size.setValue(int(self.n_recordings * old_chunk / 100))

    def get_options(self):
        model_opts = {
            "model_root_dir": "analysis/detection/models",
            "classifier": "biotic",
            "options_file": "analysis/detection/models/biotic/network_opts.yaml",
            "weights_file": "analysis/detection/models/biotic/weights_99.pkl-1",
        }
        with open(model_opts["options_file"]) as opt_file:
            options = yaml.load(opt_file)

        options["analysis"] = "detection"
        options["remove_noise"] = self.checkbox_remove_noise.isChecked()
        options["resample"] = self.checkbox_resample.isChecked()
        detection_options = {"export_pdf": self.export_pdf}
        # TODO: nprocess options
        opts = {
            "initargs": (options, model_opts["weights_file"], detection_options),
            "multiprocess": self.group_multiprocess.isChecked(),
            "nprocess": self.slider_nprocess.value(),
            "chunksize": self.slider_chunk_size.value(),
            "chunksize_percent": self.checkbox_chunk_percent.isChecked(),
            "use_gpu": self.checkbox_gpu.isChecked(),
            "analysis": "detection",
            "save": self.checkbox_save.isChecked(),
            "overwrite": self.checkbox_overwrite.isChecked(),
            "save_intermediate_results": True,
        }
        print(opts)
        return opts
