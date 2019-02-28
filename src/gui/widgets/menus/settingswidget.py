from PySide2.QtWidgets import QWidget

from gui.utils.settings import Settings


class SettingsWidget(QWidget):

    def __init__(self, parent=None, local=False):
        super().__init__(parent)
        self.local = local
        self.group = ""
        self.settings = {}

    def save_setting(self, key, value, context=""):
        if context:
            context = "/" + context
        settings = Settings()
        settings.setValue(self.group + context + "/" + key, str(value))

    def update_setting(self, value, key):
        self.settings[key] = value
        if not self.local:
            self.save_setting(key, value, self.CONTEXT)
