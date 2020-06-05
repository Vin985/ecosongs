
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QRegExp

from gui.widgets.options.ui.export_table_options_ui import \
    Ui_ExportTableOptions


class ExportTableOptions(QWidget, Ui_ExportTableOptions):

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.link_events()

    def init_ui(self):
        # TODO: load from config file
        pass

    def link_events(self):
        pass

    def get_options(self):
        opts = {}
        # import_options = {"label_folder": self.input_tag_folder.text(),
        #                   "suffix": self.input_suffix.text(),
        #                   "extensions": self.input_extensions.text().split(";")}

        # opts = {"task_options": import_options,
        #         "save": self.checkbox_save.isChecked(),
        #         "overwrite": self.checkbox_overwrite.isChecked()}
        return opts
