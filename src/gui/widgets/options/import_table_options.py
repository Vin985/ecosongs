from PySide2.QtWidgets import QWidget

from gui.widgets.options.ui.import_table_options_ui import Ui_ImportTableOptions


class ImportTableOptions(QWidget, Ui_ImportTableOptions):
    def __init__(self, parent, table):
        super().__init__(parent)
        self.setupUi(self)
        self.table_name = table
        self.table_model = qApp.tables.get_table(self.table_name)
        self.init_ui()
        self.link_events()

    def link_events(self):
        self.file_chooser.text_changed.connect(self.load_file)

    def load_file(self, path):
        loaded_df = self.table_model.get_table(path=path)
        self.table_loaded.setModel(loaded_df)
        try:
            to_import_df = self.resolve_dependencies(loaded_df)
            df = self.table_model.check_columns(to_import_df)
            self.table_to_import.setModel(df)
        except ValueError:
            self.parent().log_error(
                "Error: Required columns for import cannot be found in loaded"
                + " table. Expected columns are: {0}.".format(self.table_model.columns)
            )

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
                    raise (
                        ValueError(
                            "Error: Cannot resolve dependencies because of missing"
                            + "columns. These columns are expected {0} to be able "
                            + "to merge with {1} table.".format(
                                self.table_model.columns, dep_table_name
                            )
                        )
                    )
                dep_table = qApp.tables.get_table(dep_table_name).df
                merge_columns = [right_on] + right_dep_columns
                dep_table = dep_table[merge_columns]
                print(dep_table)

                to_import = (
                    to_import.merge(
                        dep_table, left_on=left_dep_columns, right_on=right_dep_columns
                    )
                    .drop(columns=left_dep_columns + right_dep_columns)
                    .rename(columns={right_on: left_on})
                )
                print(to_import)
        return to_import
