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


def load_annotations(folder_path, labels_path, only_done=True, extensions=[".csv"]):
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
                        dfs.append(df)
                        res_files.append(file_id)
        # only walk through the first level of the directory
        break
    if dfs:
        res = pd.concat(dfs)
        res.reset_index(inplace=True)
    return (res_files, res)


ROOT_PATH = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/Priority"
LABELS_PATH = os.path.join(ROOT_PATH, "labels")
INCLUDE_TAG = ["Biophony", "Bird"]
EXCLUDE_TAG = ["Human"]

# Load raw data
events_data = feather.read_dataframe("../db/feather/song_events.feather")
recordings_data = feather.read_dataframe("../db/feather/recordings.feather")
files_with_annots, annots_df = load_annotations(
    ROOT_PATH, LABELS_PATH, only_done=True)

print(files_with_annots)


# clean annotations
annots_df = annots_df[["Filename", "Label",
                       "LabelStartTime_Seconds", "LabelEndTime_Seconds"]]
annots_df.rename(columns={"Filename": "name", "Label": "label",
                          "LabelStartTime_Seconds": "start", "LabelEndTime_Seconds": "end"}, inplace=True)
annots_df.name = annots_df.name.apply(lambda x: x[:-4])
annots_df["duration"] = annots_df.end - annots_df.start
annots_df["matched"] = False


# Get only recordings
recs_df = recordings_data.loc[recordings_data["name"].isin(files_with_annots)]
events_df = events_data.loc[events_data.recording_id.isin(recs_df.id)]
events_df = events_df.merge(
    recs_df[["id", "name"]], left_on="recording_id", right_on="id")
events_df["duration"] = events_df.end - events_df.start
events_df["matched"] = False
events_df["ntags"] = 0
events_df["dur_overlap"] = 0
events_df["prop_overlap"] = 0
events_df["dur_overestimate"] = 0
events_df["prop_overestimate"] = 100
events_df["tags_idx"] = ""
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


def test_func(x):
    print(x)
    return 1


def match_with_annotation(event, annots=None):
    dur_overlap = 0
    prop_overlap = 0
    dur_overestimate = event.duration
    prop_overestimate = 100

    # get tags that overlap with the detected event
    tags = annots.loc[(event.start < annots.end) &
                      (event.end > annots.start)]
    tags_idx = tags.index.tolist()

    # Get how many tags the event overlaps
    ntags = tags.shape[0]
    if ntags > 0:
        event.matched = True
        tags_duration = 0
        # Iterate over all tags to check the proportion of annotation time is covered
        for idx, tag in tags.iterrows():
            # Get the overlap time
            dur_overlap += min(tag.end, event.end) - \
                max(tag.start, event.start)
            # Compute all tags duration
            tags_duration += tag.duration
            tag.matched = True
        # proportion of overlap related to tags duration
        prop_overlap = dur_overlap / tags_duration * 100
        # Duration of event not overlapping any annotation
        dur_overestimate = event.duration - dur_overlap
        # Proportion of the event that does not overlap
        prop_overestimate = dur_overestimate / event.duration * 100
    event.ntags = ntags
    event.dur_overlap = dur_overlap
    event.prop_overlap = prop_overlap
    event.dur_overestimate = dur_overestimate
    event.prop_overestimate = prop_overestimate
    # Index of tags overlapped
    event.tags_idx = ",".join(str(i) for i in tags_idx)
    return event


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


def match_events(file, annots_df, events_df):
    res = {}
    # Get annotations for the file
    annots = annots_df.loc[annots_df.name == file]
    # merge overlapping annotations into one
    annots = merge_annotations(annots)

    # Get events detected for the file
    events = events_df.loc[events_df.name == file].copy()
    # Match events with annotations
    match = events.apply(match_with_annotation, axis=1, annots=annots)
    detected = match.tags_idx.unique()
    detected = get_detected_tags_list(detected)
    n_detected = len(detected)
    recall = n_detected / annots.shape[0]

    res["dur_total"] = recs_df.loc[recs_df.name == file, "duration"].values[0]
    res["n_tot_annots"] = annots.shape[0]
    res["n_tot_events"] = events.shape[0]
    res["dur_tot_annots"] = np.sum(annots.duration)
    res["dur_tot_events"] = np.sum(events.duration)
    res["n_detected"] = n_detected
    res["recall"] = recall

    return {"file": file, "global_stats": res, "events": match}


def match_with_annotation2(event, annots=None):
    dur_overlap = 0
    prop_overlap = 0
    dur_overestimate = event.duration
    prop_overestimate = 100

    # get tags that overlap with the detected event
    tags = annots.loc[(event.start < annots.end) &
                      (event.end > annots.start)]
    tags.reset_index(inplace=True, drop=True)
    tags.rename(columns={"start": "tag_start",
                         "end": "tag_end", "duration": "tag_duration"})

    ev = []
    for i in range(0, tags.shape[0]):
        ev.append(event)
    tmp = pd.DataFrame(ev)
    tmp.reset_index(inplace=True, drop=True)
    print(tags)
    print(tmp)
    res = pd.concat([tags, tmp], join="outer", axis=1)
    print(res)

    return event


def match_events2(file, annots_df, events_df):
    res = {}
    # Get annotations for the file
    annots = annots_df.loc[annots_df.name == file]

    # Get events detected for the file
    events = events_df.loc[events_df.name == file].copy()
    # Match events with annotations
    match = events.apply(match_with_annotation2, axis=1, annots=annots)
    # detected = match.tags_idx.unique()
    # detected = get_detected_tags_list(detected)
    # n_detected = len(detected)
    # recall = n_detected / annots.shape[0]
    #
    # res["dur_total"] = recs_df.loc[recs_df.name == file, "duration"].values[0]
    # res["n_tot_annots"] = annots.shape[0]
    # res["n_tot_events"] = events.shape[0]
    # res["dur_tot_annots"] = np.sum(annots.duration)
    # res["dur_tot_events"] = np.sum(events.duration)
    # res["n_detected"] = n_detected
    # res["recall"] = recall
    #
    # return {"file": file, "global_stats": res, "events": match}


res = [match_events2(f, annots_df, events_df) for f in files_with_annots]

# Iterate over files to match events
res = [match_events(f, annots_df, events_df) for f in files_with_annots]
# Create final data_frame
final_df = pd.concat([x["events"] for x in res])

print(final_df)
true_pos = final_df[final_df["matched"] == True]

# Calculate precision
precision = true_pos.shape[0] / final_df.shape[0]
print(precision)

recall = [item["global_stats"]["recall"] for item in res]
mean_recall = sum(recall) / float(len(recall))
print(recall)
print(mean_recall)

stats_df = true_pos[["ntags", "dur_overlap",
                     "prop_overlap", "dur_overestimate", "prop_overestimate"]]
stats = stats_df.agg("mean")

print(stats)
