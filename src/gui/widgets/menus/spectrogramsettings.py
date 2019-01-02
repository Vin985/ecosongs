from functools import partial

import bidict
from gui.utils.settings import Settings
from gui.widgets.menus.ui.spectrogramsettings_ui import Ui_SpectrogramSettings
from PySide2.QtWidgets import QWidget


class SpectrogramSettings(QWidget, Ui_SpectrogramSettings):

    GROUP = "spectrogram"

    spec_window = bidict.bidict({"Hanning": "hann"})

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.init_settings()
        self.link_events()

    def init_settings(self):
        settings = Settings()
        spec_opts = settings.spectrogram_settings()
        self.combobox_scale.setCurrentIndex(self.combobox_scale.findText(spec_opts["scale"]))
        self.combobox_fft.setCurrentIndex(self.combobox_fft.findText(str(spec_opts["default_fft"])))
        spec_window = self.spec_window.inv[spec_opts["spec_window"]]
        self.combobox_spec_window.setCurrentIndex(self.combobox_spec_window.findText(spec_window))
        self.checkbox_to_db.setChecked(spec_opts["to_db"])
        self.checkbox_normalize.setChecked(spec_opts["normalize"])
        self.remove_noise.setChecked(spec_opts["remove_noise"])
        self.lineedit_noise_N.setText(str(spec_opts["nr_N"]))
        self.lineedit_noise_hist_rel_size.setText(str(spec_opts["nr_hist_rel_size"]))
        self.lineedit_noise_window.setText(str(spec_opts["nr_window_smoothing"]))

    def link_events(self):
        self.combobox_scale.currentTextChanged.connect(partial(self.update_setting, key="scale"))
        self.combobox_fft.currentTextChanged.connect(partial(self.update_setting, key="default_fft"))
        self.combobox_spec_window.currentTextChanged.connect(self.update_spec_window)
        self.checkbox_to_db.toggled.connect(partial(self.update_setting, key="to_db"))
        self.checkbox_normalize.toggled.connect(partial(self.update_setting, key="normalize"))
        self.remove_noise.toggled.connect(partial(self.update_setting, key="remove_noise"))
        self.lineedit_noise_N.textChanged.connect(partial(self.update_setting, key="nr_N"))
        self.lineedit_noise_hist_rel_size.textChanged.connect(partial(self.update_setting, key="nr_hist_rel_size"))
        self.lineedit_noise_window.textChanged.connect(partial(self.update_setting, key="nr_window_smoothing"))

    def update_spec_window(self, text):
        self.update_setting("window", self.spec_window[text])

    def update_setting(self, value, key):
        settings = Settings()
        settings.setValue(self.GROUP + "/" + key, value)
