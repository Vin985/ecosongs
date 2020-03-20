from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QWidget

from gui.widgets.analysis.ui.analysis_ui import Ui_Analysis


class Analysis(QWidget, Ui_Analysis):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.link_events()

    # Define callbacks when events happen
    def link_events(self):
        # Link menu actions
        pass
