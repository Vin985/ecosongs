import configparser
import os
from pathlib import Path

import pandas as pd

DEFAULT_TAGS_COLUMNS = {"Label": "tag",
                        "Related": "related",
                        "LabelStartTime_Seconds": "tag_start",
                        "LabelEndTime_Seconds": "tag_end",
                        "overlap": "overlap",
                        "background": "background"}
DEFAULT_TAGS_COLUMNS_TYPE = {"overlap": "str"}

DEFAULT_EXTENSIONS = [".csv"]

DEFAULT_TAG_SUFFIX = "-sceneRect"

DEFAULT_LABEL_FOLDER = "labels"


def filter_tags(df, *args, **kwargs):
    return df.loc[df.tags.apply(keep_tag, *args, **kwargs)]


def keep_tag(raw_tags, has_tags=None, exclude_tags=None, keep_by_default=False):
    has_tags = has_tags or []
    exclude_tags = exclude_tags or []
    tags = raw_tags.split(",")
    exclude = any([tag in exclude_tags for tag in tags])
    if exclude:
        return False
    include = any([tag in has_tags for tag in tags])
    if include:
        return True
    return keep_by_default
    # for tag in tags:
    #     if tag in exclude_tags:
    #         return False
    #     if tag in has_tags:
    #         return True
    # return keep_by_default


def get_species(raw_tags, species):
    tags = raw_tags.split(",")
    for tag in tags:
        if tag in species:
            return tag
    return None


def get_done_files(path, full_path=False):
    local_conf = os.path.join(path, "config.conf")
    done_files = []
    if os.path.isfile(local_conf):
        config = configparser.ConfigParser()
        config.read(local_conf)
        done_files = config['files'].get("files_done", [])
        if isinstance(done_files, str):
            done_files = done_files.split(",")
        if full_path:
            done_files = [os.path.join(path, file_name)
                          for file_name in done_files if file_name]
    return done_files


def rename_columns(df, columns):
    if columns:
        if isinstance(columns, dict):
            # df["tags"] = df["Label"] + \
            #     "," + df["Related"]
            df = df[columns.keys()]
            df = df.rename(columns=columns)
        else:
            raise ValueError(
                "columns must be a dict with old labels as keys and new labels as values")
    return df


def has_excluded_tags(df, filter_options):
    keep_by_default = filter_options.get("keep_by_default", False)
    has_tags = filter_options.get("has_tags", [])
    exclude_tags = filter_options.get("exclude_tags", [])
    res = not all(df.tags.apply(keep_tag, has_tags=has_tags,
                                exclude_tags=exclude_tags, keep_by_default=keep_by_default))
    return res


def load_tag_file(path, columns, columns_type):
    df = pd.read_csv(path, dtype=columns_type)
    df = rename_columns(df, columns)


def load_tags(recordings, options=None):
    done_files = []
    dfs = []
    res = []
    options = options or {}
    label_folder = options.get("label_folder", DEFAULT_LABEL_FOLDER)
    suffix = options.get("suffix", DEFAULT_TAG_SUFFIX)
    extensions = options.get("extensions", DEFAULT_EXTENSIONS)
    columns = options.get("columns", DEFAULT_TAGS_COLUMNS)
    columns_type = options.get("columns_type", DEFAULT_TAGS_COLUMNS_TYPE)

    # Get only the directory portion of pth
    recordings.loc[:, "dirname"] = recordings.path.apply(os.path.dirname)
    # Get unique folders
    folders = recordings.dirname.unique()

    for folder_path in folders:
        # Get only recordings in the current folder
        recs = recordings.loc[recordings.dirname == folder_path]
        folder_path = Path(folder_path)
        # Create labels subfolder
        label_path = folder_path / label_folder
        # Folder has labels
        if label_path.exists():
            # Get list of completed files
            done_files = get_done_files(folder_path, full_path=True)
            # Get list of all files
            files = [x for x in label_path.iterdir() if x.is_file()
                     and x.suffix in extensions]
            # List of files to load
            selected = recs.name.values
            for f in files:
                # File name without extension
                file_id = f.stem
                # do not check hidden files or locked files
                if not file_id[0] == ".":
                    # Remove suffix
                    file_id = file_id[: -len(suffix)]
                    # Check if file needs to be loaded
                    if file_id in selected:
                        # Get information about recording
                        rec = recs[recs.name == file_id]
                        rec_id = rec.iloc[0]["id"]
                        # Load file
                        df = pd.read_csv(f, dtype=columns_type)
                        if not df.empty:
                            try:
                                # Format columns
                                df = rename_columns(df, columns)
                                df.loc[:, "recording_id"] = int(rec_id)
                            except KeyError as ke:
                                print("Key Error {0} found for file {1}. Skipping."
                                      "Please make sure the file is correct "
                                      "and has all columns".format(
                                          ke, file_id))
                                continue
                            dfs.append(df)
                        # Get recording path
                        rec_path = rec.iloc[0]["path"]
                        # Update original recording data frame to set tag status
                        recordings.loc[recordings.path == rec_path,
                                       "has_tags"] = 2 if rec_path in done_files else 1
    if dfs:
        # Create result dataframe from individual dataframes
        res = pd.concat(dfs, ignore_index=True)
        res["tag_duration"] = res["tag_end"] - res["tag_start"]
        res.reset_index(inplace=True)
        res.rename(columns={"index": "tag_index"}, inplace=True)
    recordings.drop("dirname", axis=1, inplace=True)
    return res  # (res, recordings)


def load_annotations(root_path,
                     tags_path,
                     files=None,
                     only_done=True,
                     columns=None,
                     columns_type=None,
                     extensions=None):
    columns = columns or DEFAULT_TAGS_COLUMNS
    columns_type = columns or DEFAULT_TAGS_COLUMNS_TYPE
    extensions = extensions or DEFAULT_EXTENSIONS
    res_files = []
    dfs = []
    done_files = []
    res = pd.DataFrame()
    # Only get done files. Load list of done files
    if only_done:
        done_files = get_done_files(root_path)
    for _, _, files in os.walk(tags_path):
        for f in sorted(files):
            # do not check hidden files or locked files
            if not f[0] == ".":
                # Get extension
                ext = f[-4:]
                if ext in extensions:
                    # TODO: change this, only works if it is always ending by "-sceneRect.csv"
                    file_id = f[:-14]
                    if (not only_done) or (only_done and (file_id in done_files)):
                        df = pd.read_csv(os.path.join(
                            tags_path, f), dtype=columns_type)
                        try:
                            df = rename_columns(df, columns)
                            # if filter_options:
                            #     if has_excluded_tags(df, filter_options):
                            #         continue
                        except KeyError as ke:
                            print("Key Error {0} found for file {1}. Skipping."
                                  "Please make sure the file is correct and has all columns".format(
                                      ke, file_id))
                            continue
                        dfs.append(df)
                        file_name = df.iloc[0].file_name
                        res_files.append(file_name)
        # only walk through the first level of the directory
        break
    if dfs:
        res = pd.concat(dfs, ignore_index=True)
        res["tag_duration"] = res["tag_end"] - res["tag_start"]
        res["file_id"] = res.file_name.apply(lambda x: x[:-4])
        res.reset_index(inplace=True)
        res.rename(columns={"index": "tag_index"}, inplace=True)
    return (res_files, res)