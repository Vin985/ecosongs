import pathlib

from PySide2.QtWidgets import QWidget

from gui.widgets.options.ui.export_song_events_options_ui import (
    Ui_ExportSongEventsOptions,
)


class ExportSongEventsOptions(QWidget, Ui_ExportSongEventsOptions):
    def __init__(self, recordings, parent):
        super().__init__(parent)
        self.recordings = recordings
        self.setupUi(self)
        self.init_ui()
        self.link_events()

    def init_ui(self):

        self.radio_db.setText(
            self.radio_db.text() + " (" + qApp.dbmanager.FILE_EXTENSION + ")"
        )
        # Init file chooser
        file_chooser_options = {
            "file_type": "save_file",
        }
        self.file_chooser.options = file_chooser_options
        self.select_csv_format()

        activity_table = qApp.tables.activity_predictions.df
        recs = activity_table.recording_id.unique()

        no_preds = [rec for rec in self.recordings if rec not in recs]

        if not no_preds:
            self.frame_calculate_predictions.setHidden(True)
        else:
            txt = "{0} selected recordings have no predictions associated.".format(
                len(no_preds)
            )
            self.lbl_no_preds.setText(txt)

    def link_events(self):
        self.checkbox_calculate_predictions.clicked.connect(
            self.enable_save_predictions
        )
        self.radiogroup_format.buttonClicked.connect(self.change_format)

    def change_format(self, button):
        if button is self.radio_csv:
            self.select_csv_format()
        else:
            self.select_db_format()

    def select_csv_format(self):
        self.file_chooser.options["default"] = str(
            pathlib.Path.home() / ("song_events.csv")
        )
        self.file_chooser.init_display()

    def select_db_format(self):
        self.file_chooser.options["default"] = str(
            pathlib.Path.home() / ("song_events" + qApp.dbmanager.FILE_EXTENSION)
        )
        self.file_chooser.init_display()

    def enable_save_predictions(self):
        self.checkbox_save.setEnabled(self.checkbox_calculate_predictions.isChecked())

    def get_options(self):
        events_options = self.song_events_options.get_options()
        opts = {
            "calculate_predictions": self.checkbox_calculate_predictions.isChecked(),
            "save_predictions": self.checkbox_save.isChecked(),
            "dest": self.file_chooser.input_path.text(),
            "format": "csv" if self.radio_csv.isChecked() else qApp.dbmanager.NAME,
        }
        opts.update(events_options)
        print(opts)
        return opts
