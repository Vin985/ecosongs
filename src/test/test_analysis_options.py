import os
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
try:
    from db import dbutils
    from db.tablemanager import TableManager
    from analysis.detection import detector_evaluation
    from analysis.detection import predictions_utils
except Exception:
    print("Woops, module EventsPlot not found")


AUDIO_FOLDER = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split"
LABEL_FOLDER = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split/labels"


db_opts = {"database": "ecosongs", "db_type": "feather",
           "path": "/mnt/win/UMoncton/Doctorat/dev/ecosongs/src/test/db"}

dbmanager = dbutils.get_db_manager(**db_opts)
tables = TableManager(dbmanager)


def merge_with_statistics(table_manager, audio_folder):
    options_table = table_manager.analysis_options
    options_df = options_table.get_rows_by_column(
        "analysis_type", ["detector_sensitivity"])

    options_df = options_table.expand_options(options_df)
    print(options_df.columns)
    detector_data_table = table_manager.detector_statistics

    options_df = options_df.loc[options_df["audio_path"] == audio_folder]

    print(detector_data_table.df)

    data = options_df.merge(detector_data_table.df,
                            left_on="id", right_on="analysis_options")
    data.drop_duplicates(inplace=True)

    print(data["min_activity"])


def add_options(table_manager):
    options_table = table_manager.analysis_options
    options = {"test1": 1, "test2": 2}
    test_id = options_table.add(options, "test_options", save=False)
    print(test_id)
    options_df = options_table.df
    print(options_df.loc[options_df.analysis_type == "test_options"])


def add_options_list(table_manager):
    options_table = table_manager.analysis_options
    options = [{"test1": 1, "test2": 2}, {"test1": 3, "test2": 4}]
    res = options_table.add(options, "test_options", save=False)
    options_df = options_table.df
    print(options_df.loc[options_df.analysis_type == "test_options"])


def add_options_list_duplicate(table_manager):
    options_table = table_manager.analysis_options
    options = [{"test1": 1, "test2": 2}, {"test1": 3, "test2": 4}]
    options_table.add(options, "test_options", save=False)
    options = [{"test1": 1, "test2": 2}, {"test1": 5, "test2": 4}]
    res = options_table.add(options, "test_options", save=False, replace=False)

    options_df = options_table.df.loc[options_table.df.analysis_type ==
                                      "test_options", :]
    print(options_df)
    ids = options_df.id.astype(str)
    final = list("id:" + ids + ";" + options_df.options)
    print(final)


# add_options(tables)
# add_options_list(tables)
add_options_list_duplicate(tables)
