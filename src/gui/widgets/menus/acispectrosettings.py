from gui.widgets.menus.spectrogramsettings import SpectrogramSettings


class AciSpectroSettings(SpectrogramSettings):
    CONTEXT = "aci"

    def __init__(self, parent=None, local=False):
        super().__init__(parent, local)
