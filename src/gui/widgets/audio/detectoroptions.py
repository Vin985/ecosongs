
import yaml
from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtWidgets import QWidget

from gui.widgets.audio.ui.detectoroptions_ui import Ui_DetectorOptions


class DetectorOptions(QWidget, Ui_DetectorOptions):
    detect_songs = Signal()
    cancelling = Signal()

    def __init__(self, parent, export_pdf=False):
        super().__init__(parent)
        self.setupUi(self)
        self.link_events()
        # Set settings to local to avoid saving them unless asked
        # TODO: allow saving settings
        self.export_pdf = export_pdf
        self.lbl_activity.setText(str(self.slider_activity.value()))
        self.lbl_end_threshold.setText(str(self.slider_end_threshold.value()))
        if export_pdf:
            self.checkbox_save.setChecked(False)
            self.checkbox_save.hide()
            self.checkbox_overwrite.setChecked(False)
            self.checkbox_overwrite.hide()

    def link_events(self):
        self.slider_activity.valueChanged.connect(self.update_activity)
        self.slider_end_threshold.valueChanged.connect(
            self.update_end_threshold)

    def update_end_threshold(self, activity):
        self.lbl_end_threshold.setText(str(activity))

    def update_activity(self, activity):
        self.lbl_activity.setText(str(activity))

    def get_options(self):
        model_opts = {"model_root_dir": "analysis/detection/models",
                      "classifier": "biotic",
                      "options_file": "analysis/detection/models/biotic/network_opts.yaml",
                      "weights_file": "analysis/detection/models/biotic/weights_99.pkl-1"}
        with open(model_opts["options_file"]) as opt_file:
            options = yaml.load(opt_file)
        # TODO: add checkbox
        options["remove_noise"] = self.checkbox_remove_noise.isChecked()
        options["resample"] = self.checkbox_resample.isChecked()
        detection_options = {"min_activity": self.slider_activity.value() / 100,
                             "min_duration": self.spin_min_duration.value(),
                             "export_pdf": self.export_pdf,
                             "end_threshold": self.slider_end_threshold.value() / 100}
        # TODO: nprocess options
        opts = {"initargs": (options,
                             model_opts["weights_file"],
                             detection_options),
                "multiprocess": True,
                "nprocess": 1,
                "chunksize_percent": 100}
        return opts
