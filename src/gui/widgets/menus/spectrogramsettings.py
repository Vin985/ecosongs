from functools import partial

import bidict

from gui.utils.settings import Settings
from gui.widgets.menus.settingswidget import SettingsWidget
from gui.widgets.menus.ui.spectrogramsettings_ui import Ui_SpectrogramSettings


class SpectrogramSettings(SettingsWidget, Ui_SpectrogramSettings):

    CONTEXT = ""

    spec_window = bidict.bidict({"Hanning": "hann"})

    def __init__(self, parent=None, local=False):
        super().__init__(parent)
        # TODO: create different settings for different indexes and all
        # TODO: load spectrogram settings here using context?
        self.setupUi(self)
        self.init_settings()
        self.link_events()

    def load_settings(self):
        settings = Settings()
        self.group = Settings.GROUP_SPECTROGRAM
        self.settings = settings.spectrogram_settings(self.CONTEXT)

    def init_settings(self):
        if not self.settings:
            self.load_settings()
        self.combobox_scale.setCurrentIndex(
            self.combobox_scale.findText(self.settings["scale"]))
        self.combobox_fft.setCurrentIndex(
            self.combobox_fft.findText(str(self.settings["n_fft"])))
        spec_window = self.spec_window.inv[self.settings["spec_window"]]
        self.combobox_spec_window.setCurrentIndex(
            self.combobox_spec_window.findText(spec_window))
        self.checkbox_pcen.setChecked(self.settings["pcen"])
        # TODO if pcen is checked, disable to_db and remove_noise
        self.checkbox_to_db.setChecked(self.settings["to_db"])
        self.checkbox_normalize.setChecked(self.settings["normalize"])
        self.remove_noise.setChecked(self.settings["remove_noise"])
        self.lineedit_noise_N.setText(str(self.settings["nr_N"]))
        self.lineedit_noise_hist_rel_size.setText(
            str(self.settings["nr_hist_rel_size"]))
        self.lineedit_noise_window.setText(
            str(self.settings["nr_window_smoothing"]))

    def link_events(self):
        self.combobox_scale.currentTextChanged.connect(
            partial(self.update_setting, key="scale"))
        self.combobox_fft.currentTextChanged.connect(
            partial(self.update_setting, key="n_fft"))
        self.combobox_spec_window.currentTextChanged.connect(
            self.update_spec_window)
        self.checkbox_pcen.toggled.connect(
            partial(self.update_setting, key="pcen"))
        self.checkbox_to_db.toggled.connect(
            partial(self.update_setting, key="to_db"))
        self.checkbox_normalize.toggled.connect(
            partial(self.update_setting, key="normalize"))
        self.remove_noise.toggled.connect(
            partial(self.update_setting, key="remove_noise"))
        self.lineedit_noise_N.textChanged.connect(
            partial(self.update_setting, key="nr_N"))
        self.lineedit_noise_hist_rel_size.textChanged.connect(
            partial(self.update_setting, key="nr_hist_rel_size"))
        self.lineedit_noise_window.textChanged.connect(
            partial(self.update_setting, key="nr_window_smoothing"))

    def update_spec_window(self, text):
        self.update_setting("window", self.spec_window[text])
