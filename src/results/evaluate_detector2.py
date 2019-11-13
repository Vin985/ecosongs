import configparser
import inspect
import os

import feather
import numpy as np
import pandas as pd
from plotnine import element_text, ggtitle, theme

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
try:
    from plot.events_plot import EventsPlot
except Exception:
    print("Woops, module EventsPlot not found")


def get_done_files(path):
    local_conf = os.path.join(path, "config.conf")
    done_files = []
    if os.path.isfile(local_conf):
        config = configparser.ConfigParser()
        config.read(local_conf)
        done_files = config['files'].get("files_done", [])
        if type(done_files) is str:
            done_files = done_files.split(",")
        # remove extension
        res = [f[:-4] for f in done_files]
    return res


def load_annotations(folder_path, labels_path, only_done=True, extensions=[".csv"], columns=None):
    res_files = []
    dfs = []
    done_files = []
    # Only get done files. Load list of done files
    if only_done:
        done_files = get_done_files(folder_path)
    for root, dirs, files in os.walk(labels_path):
        for f in sorted(files):
            # do not check hidden files or locked files
            if not f[0] == ".":
                # Get extension
                ext = f[-4:]
                if ext in extensions:
                    file_id = f[:-14]
                    if (not only_done) or (only_done and (file_id in done_files)):
                        df = pd.read_csv(os.path.join(labels_path, f))
                        if columns:
                            if type(columns) is dict:
                                df = df[columns.keys()]
                                df.rename(columns=columns, inplace=True)
                                df.file_name = df.file_name.apply(
                                    lambda x: x[:-4])
                            else:
                                raise ValueError(
                                    "columns must be a dict with old labels as keys and new labels as values")
                        dfs.append(df)
                        res_files.append(file_id)
        # only walk through the first level of the directory
        break
    if dfs:
        res = pd.concat(dfs, ignore_index=True)
    return (res_files, res)


ROOT_PATH = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/Priority"
LABELS_PATH = os.path.join(ROOT_PATH, "labels")
INCLUDE_TAG = ["Biophony", "Bird"]
EXCLUDE_TAG = ["Human"]

TAG_COLUMNS = {"Filename": "file_name", "Label": "tag", "Related": "related_tags",
               "LabelStartTime_Seconds": "tag_start", "LabelEndTime_Seconds": "tag_end"}
EVENTS_COLUMNS = {'end': "event_end", 'event_id': "event_id",
                  'recording_id': "recording_id", 'start': "event_start", 'name': "file_name", "index": "event_index"}
# Load raw data
events_data = feather.read_dataframe("../db/feather/song_events.feather")
recordings_data = feather.read_dataframe("../db/feather/recordings.feather")
# Load annotations
files_with_annots, annots_df = load_annotations(
    ROOT_PATH, LABELS_PATH, only_done=True, columns=TAG_COLUMNS)
print(files_with_annots)
print(annots_df)

# Get only recordings
recs_df = recordings_data.loc[recordings_data["name"].isin(files_with_annots)]
events_df = events_data.loc[events_data.recording_id.isin(recs_df.id)]
events_df = events_df.merge(
    recs_df[["id", "name"]], left_on="recording_id", right_on="id")
events_df.reset_index(inplace=True)
events_df = events_df[EVENTS_COLUMNS.keys()]
events_df.rename(columns=EVENTS_COLUMNS, inplace=True)
print(events_df)


def merge_annotations(annots):
    res = []
    previous = {}
    annots.sort_values(by=['start'])
    for idx, annot in annots.iterrows():
        if not previous:
            previous = {"start": annot.start, "end": annot.end,
                        "duration": annot.duration, "n_annot": 1}
            res.append(previous)
        else:
            # Next annotation overlaps with the previous one
            if previous["start"] <= annot.start < previous["end"]:
                # annotation ends later than the previous one: use the end of this one instead
                if annot.end > previous["end"]:
                    # print("annotation overlap, extending the last one")
                    previous["end"] = annot.end
                    previous["n_annot"] += 1
                    previous["duration"] = previous["end"] - previous["start"]
            else:
                # Annotation starts after the next one, create new tag
                previous = {"start": annot.start,
                            "end": annot.end, "duration": annot.duration, "n_annot": 1}
                res.append(previous)
    res = pd.DataFrame(res)
    return res


def match_events(tag, events_df=None):
    # get tags that overlap with the detected event
    events_df = events_df.drop(["file_name", "recording_id"], axis=1)
    events = events_df.loc[(events_df.event_start < tag.tag_end) &
                           (events_df.event_end > tag.tag_start)]
    events.reset_index(inplace=True, drop=True)

    tmp = [tag]
    if events.shape[0] == 0:
        empty_event = pd.Series(
            {"event_end": 0, "event_id": -1, "event_start": 0, "event_index": -1})
        events = pd.DataFrame([empty_event])
    else:
        for i in range(1, events.shape[0]):
            tmp.append(tag)
    tmp_df = pd.DataFrame(tmp)
    tmp_df.reset_index(inplace=True)
    tmp_df.rename(columns={"index": "tag_index"}, inplace=True)
    res = pd.concat([tmp_df, events], join="outer", axis=1)

    return res


def get_detected_tags_list(detected):
    res = []
    for tag in detected:
        if tag == "":
            continue
        elif ',' in tag:
            tmp = tag.split(",")
            tmp = [item for item in tmp if item not in res]
            res += tmp
        elif tag not in res:
            res.append(tag)
    return res


def match_tags(file, annots_df, events_df):
    res = {}
    annots = annots_df.loc[annots_df.file_name == file]
    # Get events detected for the file
    events = events_df.loc[events_df.file_name == file]
    # Match events with annotations
    res = [match_events(row, events) for _, row in annots.iterrows()]
    match = pd.concat(res)

    return match


# Iterate over files to match events
res = [match_tags(f, annots_df, events_df) for f in files_with_annots]

match_df = pd.concat(res)

print(match_df)
print(match_df.loc[match_df.event_index != -1].index)

# True pos: number of unique events that matched with a tag
true_pos = len(match_df[match_df.event_index != -1].event_index.unique())
# False neg: number of tags that did not have a match
false_neg = match_df[match_df.event_index == -1].shape[0]

n_annots_matched = len(
    match_df.loc[match_df.event_index != -1].tag_index.unique())
print(true_pos)
print(false_neg)
print(n_annots_matched)

precision = true_pos / events_df.shape[0]
recall = true_pos / (true_pos + false_neg)
f1 = 2 * (precision * recall) / (precision + recall)
# recall = n_annots_matched / annots_df.shape[0]
print(precision)
print(recall)
print(f1)
