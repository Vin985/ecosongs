from gui.utils.settings import Settings
from PySide2.QtWidgets import QWidget


class SettingsPage(QWidget):
    GROUP = ""

    def update_setting(self, value, key):
        settings = Settings()
        settings.setValue(self.GROUP + "/" + key, value)
