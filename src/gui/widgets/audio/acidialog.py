import time

from PySide2.QtCore import Qt, Signal, Slot

from gui.widgets.audio.analyzerdialog import AnalyzerDialog
from gui.widgets.audio.ui.aci_dialog_ui import Ui_AciDialog


class AciDialog(AnalyzerDialog, Ui_AciDialog):

    compute_index = Signal(str)

    def __init__(self, recordings):
        super().__init__(recordings)
        self.setupUi(self)
        self.link_events()
        # Set settings to local to avoid saving them unless asked
        # TODO: allow saving settings
        self.spectro_settings.local = True
        self.btn_close.hide()

    def link_events(self):
        super().link_events()
        self.btn_start.clicked.connect(self.start)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_close.clicked.connect(self.accept)

        self.compute_index.connect(self.audio_analyzer.compute_index, type=Qt.QueuedConnection)

    @Slot()
    def cancel(self):
        self.reject()

    def reset_progress(self):
        self.progress_bar.setEnabled(True)
        self.progress_bar.setValue(0)

    @Slot()
    def start(self):
        print("clicking start")
        spec_opts = self.spectro_settings.settings
        spec_opts.update({'to_db': False, 'remove_noise': False})
        options = {"initargs": spec_opts, "chunksize_percent": 20}
        self.audio_analyzer.options = options
        self.compute_index.emit("ACI")
        self.started = time.time()

    @Slot()
    def computing(self):
        self.reset_progress()
        self.btn_start.setEnabled(False)

    @Slot()
    def process_results(self):
        super().process_results()
        acis = self.audio_analyzer.results
        print(acis)

    @Slot()
    def log(self, text):
        self.lbl_progress.setText(text)
