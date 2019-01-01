from gui.utils.settings import Settings
from gui.widgets.menus.ui.spectrogramsettings_ui import Ui_SpectrogramSettings
from PySide2.QtWidgets import QWidget


class SpectrogramSettings(QWidget, Ui_SpectrogramSettings):

    GROUP = "spectrogram"

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
        spec_window = Settings.spec_window.inv[spec_opts["spec_window"]]
        print("loading:" + spec_window)
        self.combobox_window.setCurrentIndex(self.combobox_window.findText(spec_window))

    def link_events(self):
        self.combobox_scale.currentIndexChanged.connect(self.update_scale)
        self.combobox_fft.currentIndexChanged.connect(self.update_fft)
        self.combobox_window.currentIndexChanged.connect(self.update_window)

    def update_window(self):
        spec_window = Settings.spec_window[self.combobox_window.currentText()]
        print("saving:" + spec_window)
        self.update_setting("window", spec_window)

    def update_scale(self):
        self.update_setting("scale", self.combobox_scale.currentText())

    def update_fft(self):
        self.update_setting("default_fft", self.combobox_fft.currentText())

    def update_setting(self, key, value):
        settings = Settings()
        settings.setValue(self.GROUP + "/" + key, value)
