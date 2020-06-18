
import pathlib

from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt

from gui.widgets.options.ui.export_table_options_ui import \
    Ui_ExportTableOptions


class ExportTableOptions(QWidget, Ui_ExportTableOptions):

    def __init__(self, parent, table):
        super().__init__(parent)
        self.setupUi(self)
        self.table_name = table
        self.table_model = qApp.tables.get_table(self.table_name)
        self.expand_columns = {}
        self.columns = []
        self.init_ui()
        self.link_events()

    def link_events(self):
        self.combo_expand_table.currentIndexChanged.connect(
            self.init_expand_columns_list)
        self.list_expand_columns.selection_changed.connect(
            self.update_expand_columns)
        self.list_columns.selection_changed.connect(
            self.update_columns)
        self.btn_select_all.clicked.connect(self.list_columns.select_all)
        self.btn_deselect_all.clicked.connect(self.list_columns.deselect_all)
        self.btn_expand_select_all.clicked.connect(
            self.list_expand_columns.select_all)
        self.btn_expand_deselect_all.clicked.connect(
            self.list_expand_columns.deselect_all)
        self.btn_expand_select_required.clicked.connect(
            self.select_expand_required)

    def select_expand_required(self):
        expand_table_name = self.combo_expand_table.currentText()
        required = self.table_model.REFERS_TO[expand_table_name]["for_import"]
        for req in required:
            items = self.list_expand_columns.findItems(req, Qt.MatchExactly)
            if items:
                item = items[0]
                item.setCheckState(Qt.Checked)

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
        self.update_columns()

    def update_columns(self):
        self.columns = self.list_columns.selected

    def init_expand_widget(self):
        self.update_expand_label()
        self.init_expand_combobox()
        self.init_expand_columns_list(0)
        # self.parent().resize()

    def update_expand_label(self):
        lbl_text = self.lbl_expand.text()
        lbl_text = lbl_text.replace("{1}", ",".join(
            self.table_model.REFERS_TO.keys()))
        self.lbl_expand.setText(lbl_text)

    def init_expand_combobox(self):
        self.combo_expand_table.addItems(self.table_model.REFERS_TO.keys())

    def init_expand_columns_list(self, index):
        expand_table_name = self.combo_expand_table.currentText()
        expand_table = qApp.tables.get_table(expand_table_name)
        self.list_expand_columns.addItems(expand_table.columns)
        self.select_expand_required()
        self.update_expand_columns()

    def update_expand_columns(self):
        self.expand_columns[self.combo_expand_table.currentText(
        )] = self.list_expand_columns.selected

    def get_options(self):
        opts = {"columns": self.columns,
                "expand": self.expand_columns,
                "dest": self.file_chooser.input_path.text()}
        print(opts)
        return opts
