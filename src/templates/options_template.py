from PySide2.QtWidgets import QWidget

from gui.widgets.options.ui.YYY_options_ui import Ui_XXXOptions


class XXXOptions(QWidget, Ui_XXXOptions):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.link_events()

    def init_ui(self):
        pass

    def link_events(self):
        pass

    def get_options(self):
        opts = {}
        return opts
