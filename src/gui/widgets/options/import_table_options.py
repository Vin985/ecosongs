from PySide2.QtWidgets import QWidget

from gui.widgets.options.ui.import_table_options_ui import Ui_ImportTableOptions


class ImportTableOptions(QWidget, Ui_ImportTableOptions):
    def __init__(self, parent, table):
        super().__init__(parent)
        self.setupUi(self)
        self.table_name = table
        self.table_model = qApp.tables.get_table(self.table_name)
        self.to_import = None
        self.init_ui()
        self.link_events()

    def link_events(self):
        self.file_chooser.text_changed.connect(self.load_file)
        self.radiogroup_update.buttonToggled.connect(self.enable_overwrite)

    def init_ui(self):
        # Init file chooser
        file_chooser_options = {
            "file_type": "file",
            "file_filter": qApp.dbmanager.FILE_EXTENSION
            + "(*"
            + qApp.dbmanager.FILE_EXTENSION
            + ")",
        }
        self.file_chooser.options = file_chooser_options

    def load_file(self, path):
        loaded_df = self.table_model.get_table(path=path)
        self.table_loaded.setModel(loaded_df)
        try:
            # First check if the table is raw and can be imported as is
            try:
                self.to_import = self.table_model.check_columns(loaded_df)
                if self.table_model.REFERS_TO:
                    self.parent().log_error(
                        "Warning!!! While the loaded table has the correct structure, it contains "
                        + "references to another table. Importing it as is could create problems "
                        + "and compromise the integrity of the database. Proceed at your own risk."
                    )
            except ValueError:
                to_import_df = self.resolve_dependencies(loaded_df)
                self.to_import = self.table_model.check_columns(to_import_df)
            self.table_to_import.setModel(self.to_import)
        except ValueError as ve:
            self.parent().log_error(str(ve))

    def enable_overwrite(self):
        self.checkbox_overwrite.setHidden(self.radio_replace.isChecked())
        self.parent().adjustSize()

    def resolve_dependencies(self, df):
        to_import = df
        if self.table_model.REFERS_TO:
            for dep_table_name, dependencies in self.table_model.REFERS_TO.items():
                left_on, right_on = dependencies["on"].split(":")
                right_dep_columns = dependencies["for_import"]
                left_dep_columns = [
                    dep_table_name + "_" + col for col in right_dep_columns
                ]

                if not all(col in df.columns for col in left_dep_columns):
                    msg = (
                        "Error: Cannot import table. To import a backup, the following"
                        + " columns are required {0}.\nIf the table was exported from another "
                        + "database, the following columns are required {1} "
                        + "to be able to merge with table {2}."
                    ).format(self.table_model.columns, left_dep_columns, dep_table_name)
                    raise (ValueError(msg))

                dep_table = qApp.tables.get_table(dep_table_name).df
                merge_columns = [right_on] + right_dep_columns
                dep_table = dep_table[merge_columns]

                to_import = (
                    to_import.merge(
                        dep_table, left_on=left_dep_columns, right_on=right_dep_columns
                    )
                    .drop(columns=left_dep_columns + right_dep_columns)
                    .rename(columns={right_on: left_on})
                )
        return to_import

    def get_options(self):
        opts = {
            "to_import": self.to_import,
            "update": self.radio_update.isChecked(),
            "overwrite": self.checkbox_overwrite.isChecked(),
        }
        print(opts)
        return opts
