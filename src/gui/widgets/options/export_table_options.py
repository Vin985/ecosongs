
import pathlib

from PySide2.QtWidgets import QWidget

from gui.widgets.options.ui.export_table_options_ui import \
    Ui_ExportTableOptions


class ExportTableOptions(QWidget, Ui_ExportTableOptions):

    def __init__(self, parent, table):
        super().__init__(parent)
        self.setupUi(self)
        self.table_name = table
        self.table_model = qApp.tables.get_table(self.table_name)
        self.init_ui()
        self.link_events()
        self.expand_columns = {}

    def link_events(self):
        self.combo_expand_table.currentIndexChanged.connect(
            self.init_expand_columns_list)
        self.list_expand_columns.itemChanged.connect(
            self.update_expand_columns)

    def init_ui(self):
        # Init file chooser
        file_chooser_options = {"file_type": "save_file",
                                "default": str(pathlib.Path.home() /
                                               (self.table_name + qApp.dbmanager.FILE_EXTENSION))}
        self.file_chooser.options = file_chooser_options
        self.file_chooser.init_display()

        # Init columns
        self.init_columns_list()

        # Init expand options
        if not self.table_model.REFERS_TO:
            self.expand_widget.setHidden(True)
            self.expand = False
        else:
            self.expand = True
            self.init_expand_widget()

    def init_columns_list(self):
        self.list_columns.addItems(self.table_model.columns, True)

    def init_expand_widget(self):
        self.update_expand_label()

    def update_expand_label(self):
        lbl_text = self.lbl_expand.text()
        lbl_text = lbl_text.replace("{1}", ",".join(
            self.table_model.REFERS_TO.keys()))
        self.lbl_expand.setText(lbl_text)
        self.init_expand_combobox()

    def init_expand_combobox(self):
        self.combo_expand_table.addItems(self.table_model.REFERS_TO.keys())
        self.init_expand_columns_list(0)

    def init_expand_columns_list(self, index):
        expand_table_name = self.combo_expand_table.currentText()
        expand_table = qApp.tables.get_table(expand_table_name)
        self.list_expand_columns.addItems(expand_table.COLUMNS, True)

    def update_expand_columns(self, item):
        self.expand_columns[self.combo_expand_table.currentText(
        )] = self.list_expand_columns.selected
        print(self.expand_columns)

    def get_options(self):
        opts = {}
        export_options = {"expand": self.radio_expand.isChecked(),
                          "dest": self.file_chooser.input_path.text()}
        opts = {"task_options": export_options}
        return opts
