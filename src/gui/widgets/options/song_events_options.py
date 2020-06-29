from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal

from gui.widgets.options.ui.song_events_options_ui import Ui_SongEventsOptions


class SongEventsOptions(QWidget, Ui_SongEventsOptions):

    EVENT_DETECTION_METHODS = ["standard", "subsampling"]

    option_changed = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.link_events()

    def init_ui(self):
        pass

    def link_events(self):
        self.spin_activity.valueChanged.connect(self.emit_signal)
        self.spin_end_threshold.valueChanged.connect(self.emit_signal)
        self.spin_min_duration.valueChanged.connect(self.emit_signal)
        self.combo_method.currentIndexChanged.connect(self.emit_signal)

    def emit_signal(self, *args, **kwargs):
        self.option_changed.emit()

    def get_options(self):
        opts = {
            "method": self.EVENT_DETECTION_METHODS[self.combo_method.currentIndex()],
            "min_activity": self.spin_activity.value(),
            "end_threshold": self.spin_end_threshold.value(),
            "min_duration": self.spin_min_duration.value() / 1000,
            "isolate_events": True,
        }
        return opts
