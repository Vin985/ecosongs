
import yaml
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget

from gui.widgets.options.ui.detectoroptions_ui import Ui_DetectorOptions


class DetectorOptions(QWidget, Ui_DetectorOptions):
    detect_songs = Signal()
    cancelling = Signal()

    def __init__(self, parent, export_pdf=False):
        super().__init__(parent)
        self.setupUi(self)
        # Set settings to local to avoid saving them unless asked
        # TODO: allow saving settings
        self.export_pdf = export_pdf
        if export_pdf:
            self.checkbox_save.setChecked(False)
            self.checkbox_save.hide()
            self.checkbox_overwrite.setChecked(False)
            self.checkbox_overwrite.hide()

    def get_options(self):
        model_opts = {"model_root_dir": "analysis/detection/models",
                      "classifier": "biotic",
                      "options_file": "analysis/detection/models/biotic/network_opts.yaml",
                      "weights_file": "analysis/detection/models/biotic/weights_99.pkl-1"}
        with open(model_opts["options_file"]) as opt_file:
            options = yaml.load(opt_file)

        options["analysis"] = "detection"
        options["remove_noise"] = self.checkbox_remove_noise.isChecked()
        options["resample"] = self.checkbox_resample.isChecked()
        detection_options = {"export_pdf": self.export_pdf}
        # TODO: nprocess options
        opts = {"initargs": (options,
                             model_opts["weights_file"],
                             detection_options),
                "multiprocess": True,
                "nprocess": 1,
                "chunksize_percent": 5,
                "analysis": "detection",
                "save": self.checkbox_save.isChecked(),
                "overwrite": self.checkbox_overwrite.isChecked()}
        return opts
