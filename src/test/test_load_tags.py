# %%

import os
import inspect
from pathlib import Path
import pandas as pd

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
try:
    from db import dbutils
    from db.tablemanager import TableManager
    from utils import tag_manager
except Exception:
    print("Woops, module EventsPlot not found")


audio_folder = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split"
label_folder = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split/labels"


db_opts = {"database": "ecosongs", "db_type": "feather",
           "path": "/mnt/win/UMoncton/Doctorat/dev/ecosongs/src/db"}

dbmanager = dbutils.get_db_manager(**db_opts)
tables = TableManager(dbmanager)


recordings_df = tables.recordings.df

# %%


def load_tags(files):
    folder_path = files.name
    label_path = os.path.join(folder_path, "labels")
    if os.path.exists(label_path):
        done_files = tag_manager.get_done_files(folder_path)


# %%

recordings_df.loc[:, "has_tag"] = 0
recs_df = recordings_df.loc[recordings_df.id.isin(range(80571, 80576))]

recs_df.loc[:, "dirname"] = recs_df.path.apply(os.path.dirname)

folders = recs_df.dirname.unique()

# recs_df.groupby("dirname", as_index=False).apply(load_tags)

# %%
tags = []
done_files = []
dfs = []
res = []
extensions = [".csv"]
suffix = "-sceneRect"

for folder_path in folders:
    folder_path = Path(folder_path)
    recs = recs_df.loc[recs_df.dirname == str(folder_path)]
    label_path = folder_path / "labels"
    if label_path.exists():
        done_files = tag_manager.get_done_files(folder_path, full_path=True)
        files = [x for x in label_path.iterdir() if x.is_file()
                 and x.suffix in extensions]
        selected = recs.name.values
        for f in files:
            file_id = f.stem
            # do not check hidden files or locked files
            if not file_id[0] == ".":
                # TODO: change this, only works if it is always ending by "-sceneRect.csv"
                file_id = file_id[:-len(suffix)]
                if file_id in selected:
                    rec = recs[recs.name == file_id]
                    rec_id = rec.iloc[0]["id"]
                    df = pd.read_csv(f, dtype=tag_manager.TAGS_COLUMNS_TYPE)
                    try:
                        df = tag_manager.rename_columns(
                            df, tag_manager.TAGS_COLUMNS)
                        df.loc[:, "recording_id"] = int(rec_id)
                        # print(df)
                        # if filter_options:
                        #     if has_excluded_tags(df, filter_options):
                        #         continue
                    except KeyError as ke:
                        print("Key Error {0} found for file {1}. Skipping."
                              "Please make sure the file is correct and has all columns".format(
                                  ke, file_id))
                        continue
                    dfs.append(df)
                    rec_path = rec.iloc[0]["path"]
                    # if str(f) in done_files:
                    #     has_tag = 2
                    # else:
                    #     has_tag = 1
                    recs.loc[recs.path == rec_path,
                             "has_tag"] = 2 if rec_path in done_files else 1
if dfs:
    res = pd.concat(dfs, ignore_index=True)
    res["tag_duration"] = res["tag_end"] - res["tag_start"]
    res.reset_index(inplace=True)
    res.rename(columns={"index": "tag_index"}, inplace=True)

res
# recs.loc[recs.path.isin(done_files), "has_tag"] = 2
recordings_df.update(recs)

# %%


# %%
