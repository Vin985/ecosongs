
from PySide2.QtWidgets import QWidget

from gui.widgets.options.ui.tag_import_options_ui import \
    Ui_TagImportOptions


class TagImportOptions(QWidget, Ui_TagImportOptions):

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.link_events()

    def init_ui(self):
        pass

    def link_events(self):
        # Restricting slider movement
        pass

    def get_options(self):
        opts = {}
        return opts
