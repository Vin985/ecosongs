import os
from time import time

import pandas as pd
import pyqtgraph as pg
from PySide2 import QtCore
from PySide2.QtWidgets import QFileDialog

from analysis.detection import detectors
from gui.widgets.analysis.ui.detection_evaluator_ui import Ui_DetectionEvaluator
from gui.widgets.common.tab_widget import TabWidget
from gui.widgets.dialogs.sensitivity_dialog import SensitivityDialog
from pyqtextra.pyqtgraph.RotateAxisItem import RotateAxisItem


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
        self.stats = {}

        self.all_tags = []

    # Define callbacks when events happen

    def link_events(self):
        # Checkboxes
        self.checkbox_show_tags.clicked.connect(self.show_explore_tabs)
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

        self.init_barplot()

        self.update_tag_selection_ui()

    def init_barplot(self):

        tags = self.tags_df.drop_duplicates().copy()
        counts = (
            tags["tag"]
            .value_counts()
            .reset_index()
            .rename(columns={"index": "tag_name", "tag": "count"})
            .sort_values("tag_name")
        )
        print(counts)

        bar_graph = pg.BarGraphItem(
            x=range(1, counts.shape[0] + 1),
            width=1,
            height=counts["count"],
            name=counts["tag_name"],
        )

        pg.setConfigOptions(foreground="#000000", background="w")
        plt = pg.PlotWidget()
        plt.setWindowTitle("pyqtgraph example: BarGraphItem")
        plt.addItem(bar_graph)
        axis = RotateAxisItem("bottom", angle=-90)
        axis.setTicks([list(enumerate(counts["tag_name"], 1))])
        plt.setAxisItems({"bottom": axis})

        self.plot_layout.replaceWidget(self.plot_widget, plt)

    def update_tag_selection_ui(self):
        msg = "Found {0} recordings with tags. {1} tags loaded".format(
            len(self.tags_df.recording_id.unique()), self.tags_df.shape[0],
        )

        if self.selected_recordings:
            msg = ("{0} recordings were selected. " + msg).format(
                self.recordings_df.shape[0]
            )
        self.lbl_selected_tags.setText(msg)
        self.show_explore_tabs()

    def show_explore_tabs(self):
        self.explore_tabs.setHidden(not self.checkbox_show_tags.isChecked())

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

        tic = time()
        res = detector.evaluate(predictions_df, self.tags_df, event_options)
        self.stats = res

        self.display_results(res)
        # matches = res.get("matched", None)
        # if matches is not None:
        #     print("saving")
        #     matches.to_csv("test/db/matches2.csv")
        # events = res.get("events", None)
        # if events is not None:
        #     print("saving")
        #     events.to_csv("test/db/events2.csv")
        # tags = res.get("tags", None)
        # if tags is not None:
        #     print("saving")
        #     tags.to_csv("test/db/tags2.csv")
        print("Took %0.6fs to evaluate predictions" % (time() - tic))
        tic = time()

    def display_results(self, results):
        self.group_results.setEnabled(True)
        stats = results["stats"]
        for key, value in stats.items():
            lbl = getattr(self, "lbl_" + key)
            lbl.setText(str(value))
            lbl.setEnabled(True)

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
