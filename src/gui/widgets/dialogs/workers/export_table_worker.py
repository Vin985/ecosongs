from gui.threads.thread_worker import ThreadWorker

# from PySide2.QtCore import qApp


class ExportTableWorker(ThreadWorker):
    def __init__(self, table_name, table_data):
        super().__init__()
        self.table_name = table_name
        self.table_data = table_data

    def perform_task(self):
        print("Exporting table: ", self.table_name)
        table_model = qApp.tables.get_table(self.table_name)
        to_export = self.table_data.copy()

        # if self.table_name == "activity_predictions":
        #     to_export = to_export.iloc[1:50000]
        if self.options["expand"]:
            for expand_table, expand_columns in self.options["expand_columns"].items():
                expand_data = qApp.tables.get_table(expand_table).df
                merge_on = table_model.REFERS_TO[expand_table]["on"].split(":")

                # rename columns to prefix name of table
                new_cols = {col: expand_table + "_" + col for col in expand_columns}

                # Add the column to merge on
                expand_columns.add(merge_on[1])

                # Only keep relevant columns
                expand_data = expand_data[expand_columns].copy()

                # Rename columns
                expand_data.rename(columns=new_cols, inplace=True)

                to_export = to_export.merge(
                    expand_data, left_on=merge_on[0], right_on=merge_on[1]
                )
                to_export.drop(columns=merge_on, inplace=True)

        # Remove columns not selected. Probably less efficient than selecting
        # Columns directly but ensure that useful columns are not removed before merge
        # and that merged columns are not excluded.
        selected_columns = self.options["columns"]
        to_remove = [col for col in table_model.columns if col not in selected_columns]
        to_export.drop(columns=to_remove, inplace=True)

        table_model.export_table(table=to_export, options=self.options)
        # self.options["save"] = True
        # self.results = tag_manager.load_tags(
        #     self.recordings, self.options["task_options"])
