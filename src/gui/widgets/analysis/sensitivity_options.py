
from PySide2.QtWidgets import QWidget

from gui.widgets.analysis.ui.sensitivity_options_ui import Ui_SensitivityOptions
from functools import partial


class SensitivityOptions(QWidget, Ui_SensitivityOptions):

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.link_events()

    def init_ui(self):
        self.slider_activity_start.multiplier = .01
        self.slider_activity_end.multiplier = .01
        self.slider_end_threshold_start.multiplier = .01
        self.slider_end_threshold_end.multiplier = .01
        self.slider_min_duration_start.multiplier = 10
        self.slider_min_duration_end.multiplier = 10
        self.slider_min_duration_start.unit = " ms"
        self.slider_min_duration_end.unit = " ms"

    def link_events(self):
        # Restricting slider movement
        self.slider_activity_start.value_changed.connect(
            partial(self.check_limits, slider=self.slider_activity_start,
                    maximum=self.slider_activity_end))
        self.slider_activity_end.value_changed.connect(
            partial(self.check_limits, slider=self.slider_activity_end,
                    minimum=self.slider_activity_start))

        self.slider_end_threshold_start.value_changed.connect(
            partial(self.check_limits, slider=self.slider_end_threshold_start,
                    maximum=self.slider_end_threshold_end))
        self.slider_end_threshold_end.value_changed.connect(
            partial(self.check_limits, slider=self.slider_end_threshold_end,
                    minimum=self.slider_end_threshold_start))

        self.slider_min_duration_start.value_changed.connect(
            partial(self.check_limits, slider=self.slider_min_duration_start,
                    maximum=self.slider_min_duration_end))
        self.slider_min_duration_end.value_changed.connect(
            partial(self.check_limits, slider=self.slider_min_duration_end,
                    minimum=self.slider_min_duration_start))

    def check_limits(self, value, slider, minimum=None, maximum=None):
        if maximum and value >= maximum.value():
            slider.setSliderPosition(maximum.value() - slider.singleStep())
        if minimum and value <= minimum.value():
            slider.setSliderPosition(minimum.value() + slider.singleStep())

    def get_options(self):
        analysis_options = {"min_activity_start": self.slider_activity_start.display_value,
                            "min_activity_end": self.slider_activity_end.display_value,
                            "end_threshold_start": self.slider_end_threshold_start.display_value,
                            "end_threshold_end": self.slider_end_threshold_end.display_value,
                            "min_duration_start": self.slider_min_duration_start.display_value,
                            "min_duration_end": self.slider_min_duration_end.display_value,
                            "activity_step": self.spin_activity_step.value(),
                            "end_threshold_step": self.spin_end_threshold_step.value(),
                            "min_duration_step": self.spin_duration_step.value()}

        opts = {"analysis_options": analysis_options,
                "multiprocess": True,
                "nprocess": 1,
                "chunksize_percent": 5}
        return opts