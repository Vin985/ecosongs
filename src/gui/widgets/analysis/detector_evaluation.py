import os

from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QFileDialog, qApp

from gui.widgets.analysis.ui.detector_evaluation_ui import \
    Ui_DetectorEvaluation

from analysis.detection import detector_evaluation


class DetectorEvaluation(QWidget, Ui_DetectorEvaluation):

    DEFAULT_LABEL_FOLDER = "labels"
    MSG_LABEL_COLOR = {"info": "blue", "warning": "orange", "error": "red"}

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.link_events()
        self.folders = {"audio": "", "labels": ""}
        self.init_form()
        self.files = []
        self.tags_df = None
        self.predictions_df = None
        self.recordings_df = None

        self.all_tags = []
        self.included_tags = []
        self.excluded_tags = []

    # Define callbacks when events happen

    def link_events(self):
        # Buttons
        self.btn_audio_folder.clicked.connect(self.select_audio_folder)
        self.btn_label_folder.clicked.connect(self.select_label_folder)
        self.btn_load_data.clicked.connect(self.load_data)

        # sliders
        self.slider_min_activity.sliderMoved.connect(self.update_min_activity)
        self.slider_end_threshold.sliderMoved.connect(
            self.update_end_threshold)
        self.slider_min_duration.sliderMoved.connect(self.update_min_duration)

        self.list_include_tag.itemSelectionChanged.connect(self.include_tag)
        self.list_exclude_tag.itemSelectionChanged.connect(self.exclude_tag)

    def include_tag(self):
        items = [item.text() for item in self.list_include_tag.selectedItems()]
        self.change_items_status(self.list_exclude_tag, items)
        print("including")

    def exclude_tag(self):
        items = [item.text() for item in self.list_exclude_tag.selectedItems()]
        self.change_items_status(self.list_include_tag, items)
        print("excluding")

    def change_items_status(self, dest, disable_list):
        for i in range(dest.count()):
            item = dest.item(i)
            if item.text() in disable_list:
                self.disable_item(item)
            else:
                self.enable_item(item)

    def enable_item(self, item):
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

    def disable_item(self, item):
        item.setFlags(QtCore.Qt.NoItemFlags)

    def init_form(self):
        pass

    def select_audio_folder(self):
        self.browse(self.input_audio_folder)
        if self.cb_check_label.isChecked():
            audio_path = self.input_audio_folder.text()
            tmp_label_path = os.path.join(
                audio_path, self.DEFAULT_LABEL_FOLDER)
            if os.path.exists(tmp_label_path):
                self.input_label_folder.setText(tmp_label_path)
                self.display_message(
                    "Found 'labels' folder below the selected audio folder. Using this folder by default for labels.")

    # Browse destination directory
    def select_label_folder(self):
        self.browse(self.input_label_folder)

    # Generic method to browse for files
    def browse(self, text_input):
        default = os.getcwd()
        if text_input.text():
            default = text_input.text()
        text = QFileDialog.getExistingDirectory(self, "Choose directory",
                                                default)
        # Update gui input
        text_input.setText(text)

    def display_message(self, text, msg_type="info"):
        self.lbl_message.setText(text)
        style = "color:" + self.MSG_LABEL_COLOR[msg_type] + ";"
        self.lbl_message.setStyleSheet(style)

    def load_data(self):
        print("loading data")
        if not self.input_audio_folder.text() or not self.input_label_folder.text():
            self.display_message(
                "Audio or label folder are missing. Please select them properly before trying to load data.", "error")
            return

        self.files, self.tags_df = detector_evaluation.load_annotations(root_path=self.input_audio_folder.text(),
                                                                        tags_path=self.input_label_folder.text(),
                                                                        only_done=self.cb_only_done.isChecked())

        paths = [os.path.join(self.input_audio_folder.text(), file_name)
                 for file_name in self.files]
        self.recordings_df = qApp.tables.recordings.get_recordings_by_path(
            paths)

        self.display_message("{0} annotations found in {1} files".format(
            self.tags_df.shape[0], len(self.files)))
        self.enable_options()

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
        self.lbl_min_activity.setText(str(value))

    def update_end_threshold(self, value):
        self.lbl_end_threshold.setText(str(value))

    def update_min_duration(self, value):
        self.lbl_min_duration.setText(str(value))
