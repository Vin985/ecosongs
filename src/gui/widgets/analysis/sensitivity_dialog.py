import time

from PySide2.QtCore import Qt, QThread, Signal, Slot
from PySide2.QtWidgets import QDialog

from gui.widgets.menus.progressdialog import ProgressDialog

import time

import pandas as pd
from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtGui import qApp

from gui.widgets.menus.progressdialog import ProgressDialog
from gui.widgets.analysis.sensitivity_options import SensitivityOptions
from gui.widgets.analysis.sensitivity_worker import SensitivityWorker


class SensitivityDialog(ProgressDialog):

    launch_analysis = Signal()

    def __init__(self, recordings, tags, predictions, parent=None):
        super().__init__(parent)
        self.worker = SensitivityWorker(recordings, tags, predictions)
        self.options = SensitivityOptions(self)
        self.content_layout.addWidget(self.options)
        self.link_events()
        # self.adjustSize()

    def link_events(self):
        super().link_events()
        self.launch_analysis.connect(
            self.worker.perform_analysis, type=Qt.QueuedConnection)

    @Slot()
    def start(self):
        print("clicking start")
        self.worker.options = self.options.get_options()
        self.launch_analysis.emit()
        self.started = time.time()

    @Slot()
    def process_results(self):
        pass
