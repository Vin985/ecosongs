import os
from time import time
import pandas as pd

from PySide2 import QtCore
from PySide2.QtWidgets import QFileDialog

from analysis.detection import detectors
from gui.widgets.analysis.ui.detection_evaluator_ui import Ui_DetectionEvaluator
from gui.widgets.common.tab_widget import TabWidget
from gui.widgets.dialogs.sensitivity_dialog import SensitivityDialog


class DetectionEvaluator(TabWidget, Ui_DetectionEvaluator):

    DEFAULT_LABEL_FOLDER = "labels"
    MSG_LABEL_COLOR = {"info": "blue", "warning": "orange", "error": "red"}

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.link_events()
        self.files = []
        self.tags_df = pd.DataFrame()
        self.predictions_df = pd.DataFrame()
        self.recordings_df = pd.DataFrame()
        self.selected_recordings = []

        self.all_tags = []

    # Define callbacks when events happen

    def link_events(self):
        # Checkboxes
        self.checkbox_show_tags.clicked.connect(self.show_tags_table)
        # Buttons
        # self.btn_audio_folder.clicked.connect(self.select_audio_folder)
        # self.btn_label_folder.clicked.connect(self.select_label_folder)
        # self.btn_load_data.clicked.connect(self.load_data)
        self.btn_calculate.clicked.connect(self.calculate)
        # self.btn_sensitivity.clicked.connect(self.launch_sensitivity_analysis)

        # # sliders
        # self.list_include_tag.itemSelectionChanged.connect(self.include_tag)
        # self.list_exclude_tag.itemSelectionChanged.connect(self.exclude_tag)

    def init_ui(self):
        self.load_tags()

    def enter_tab(self, opts):
        if opts:
            self.recordings_df = opts.get("selected_recordings", pd.DataFrame())
        self.init_ui()

    def load_tags(self):
        tags_df = qApp.tables.tags.df
        if not self.recordings_df.empty:
            if self.checkbox_only_done.isChecked():
                self.selected_recordings = list(
                    self.recordings_df.loc[
                        self.recordings_df.has_tags == 2, "id"
                    ].unique()
                )
            else:
                self.selected_recordings = self.recordings_df.id.unique()
            tags_df = tags_df.loc[tags_df.recording_id.isin(self.selected_recordings)]
        self.tags_df = tags_df
        self.table_tags.setModel(self.tags_df)
        self.update_tag_selection_ui()

    def update_tag_selection_ui(self):
        msg = "Found {0} recordings with tags. {1} tags loaded".format(
            len(self.tags_df.recording_id.unique()), self.tags_df.shape[0],
        )

        if self.selected_recordings:
            msg = ("{0} recordings were selected. " + msg).format(
                self.recordings_df.shape[0]
            )
        self.lbl_selected_tags.setText(msg)
        self.show_tags_table()

    def show_tags_table(self):
        self.table_tags.setHidden(not self.checkbox_show_tags.isChecked())

    #############
    ### Slots ###
    #############

    # Calculate the statistics to evaluate the detection performance
    @QtCore.Slot()
    def calculate(self):

        event_options = self.song_events_options.get_options()
        detector = detectors.DETECTORS[event_options["method"]]
        predictions_df = qApp.tables.activity_predictions.df
        predictions_df = predictions_df.loc[
            predictions_df.recording_id.isin(self.selected_recordings)
        ]
        print(self.selected_recordings)
        print(self.predictions_df)
        print(self.tags_df.columns)

        tic = time()
        res = detector.evaluate(predictions_df, self.tags_df, event_options)
        # res = detector.evaluate(predictions_df, self.tags_df.loc[], event_options)
        print(res)
        matches = res.get("matches", None)
        if matches is not None:
            print("saving")
            matches.to_csv("test/db/matches.csv")
        events = res.get("events", None)
        if events is not None:
            print("saving")
            events.to_csv("test/db/events.csv")
        tags = res.get("tags", None)
        if tags is not None:
            print("saving")
            tags.to_csv("test/db/tags.csv")
        print("Took %0.6fs to evaluate predictions" % (time() - tic))
        tic = time()
        # self.display_stats(stats)

    def display_stats(self, stats):
        print(stats)
        self.results_widget.setEnabled(True)
        self.lbl_n_events.setText(str(stats["n_events"]))
        self.lbl_n_annots.setText(str(stats["n_tags"]))
        self.lbl_events_matched.setText(str(stats["true_positive_events"]))
        self.lbl_annots_matched.setText(str(stats["n_tags_matched"]))
        self.lbl_precision.setText(str(round(stats["precision"], 3)))
        self.lbl_recall.setText(str(round(stats["recall"], 3)))

    # Filter the annotations by keeping the files with the selected tags.
    # Prevents the selected tags to be excluded.
    @QtCore.Slot()
    def include_tag(self):
        items = [item.text() for item in self.list_include_tag.selectedItems()]
        self.change_items_status(self.list_exclude_tag, items)

    # Filter the annotations by excluding the files with the selected tags
    # Prevents the selected tags to be included.
    @QtCore.Slot()
    def exclude_tag(self):
        items = [item.text() for item in self.list_exclude_tag.selectedItems()]
        self.change_items_status(self.list_include_tag, items)

    @QtCore.Slot()
    def launch_sensitivity_analysis(self):
        print("launching")
        self.sensitivity_dialog = SensitivityDialog(
            parent=self,
            predictions=self.predictions_df,
            recordings=self.recordings_df,
            tags=self.tags_df,
            audio_path=self.input_audio_folder.text(),
            labels_path=self.input_label_folder.text(),
        )
        self.sensitivity_dialog.setModal(True)
        self.sensitivity_dialog.show()

    ####################
    ### GUI Updating ###
    ####################

    def enable_options(self):
        self.options_widget.setEnabled(True)
        self.all_tags = list(set((",".join(self.tags_df.tags)).split(",")))
        self.all_tags.sort()
        self.list_include_tag.addItems(self.all_tags)
        self.list_exclude_tag.addItems(self.all_tags)

        self.update_min_activity(self.slider_min_activity.value())
        self.update_end_threshold(self.slider_end_threshold.value())
        self.update_min_duration(self.slider_min_duration.value())

    def update_min_activity(self, value):
        self.lbl_min_activity.setText(str(value / 100))

    def update_end_threshold(self, value):
        self.lbl_end_threshold.setText(str(value / 100))

    def update_min_duration(self, value):
        self.lbl_min_duration.setText(str(value * 10) + " ms")

    def display_message(self, text, msg_type="info"):
        self.lbl_message.setText(text)
        style = "color:" + self.MSG_LABEL_COLOR[msg_type] + ";"
        self.lbl_message.setStyleSheet(style)

    #####################
    ### File browsing ###
    #####################

    # Generic method to browse for files
    def browse(self, text_input):
        default = os.getcwd()
        if text_input.text():
            default = text_input.text()
        text = QFileDialog.getExistingDirectory(self, "Choose directory", default)
        # Update gui input
        text_input.setText(text)

    #####################
    ### Tag selection ###
    #####################

    def enable_item(self, item):
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

    def disable_item(self, item):
        item.setFlags(QtCore.Qt.NoItemFlags)

    def change_items_status(self, dest, disable_list):
        for i in range(dest.count()):
            item = dest.item(i)
            if item.text() in disable_list:
                self.disable_item(item)
            else:
                self.enable_item(item)
