from gui.widgets.dialogs.progress_dialog import ProgressDialog
from gui.widgets.dialogs.workers.audio_analyzer_worker import AudioAnalyzerWorker
from gui.widgets.options.detector_options import DetectorOptions


class DetectorDialog(ProgressDialog):
    def __init__(self, recordings, export_pdf=False, parent=None):
        super().__init__(parent=parent)
        self.worker = AudioAnalyzerWorker(recordings)
        self.init_options_widget(DetectorOptions(self, len(recordings), export_pdf))
        self.link_events()

    def results_saved(self):
        print("saved")

    def duration_message(self):
        if self.worker.nitems:
            message = "Processed %d recordings in %0.3f seconds (%0.3fs/recording)" % (
                self.worker.nitems,
                self.duration,
                self.duration / self.worker.nitems,
            )
            if self.worker.options["save"]:
                message += ".\nSaving results, please wait..."
        else:
            message = (
                "Task completed in %0.3f seconds. No recordings were processed."
                % (self.duration,)
            )
        return message
