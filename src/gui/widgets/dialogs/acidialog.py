import time
import pandas as pd

from PySide2.QtCore import Qt, Signal, Slot

from gui.widgets.dialogs.analyzerdialog import AnalyzerDialog
from gui.widgets.dialogs.ui.aci_dialog_ui import Ui_AciDialog


class AciDialog(AnalyzerDialog, Ui_AciDialog):

    compute_index = Signal(str)

    def __init__(self, recordings, parent=None):
        super().__init__(recordings)
        self.setupUi(self)
        self.link_events()
        # Set settings to local to avoid saving them unless asked
        # TODO: allow saving settings
        self.spectro_settings.local = True
        self.btn_close.hide()

    def link_events(self):
        super().link_events()
        self.compute_index.connect(
            self.audio_analyzer.compute_index, type=Qt.QueuedConnection)

    @Slot()
    def start(self):
        spec_opts = self.spectro_settings.settings
        spec_opts.update({'to_db': False, 'remove_noise': False})
        options = {"initargs": spec_opts, "chunksize_percent": 2}
        self.audio_analyzer.options = options
        self.compute_index.emit("ACI")
        self.started = time.time()

    @Slot()
    def process_results(self):
        super().process_results()
        acis = pd.DataFrame(self.audio_analyzer.results)
        print(acis)
