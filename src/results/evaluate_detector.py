import inspect
import os

import feather
import numpy as np
import pandas as pd
from plotnine import element_text, ggtitle, theme

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
print(currentdir)
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
try:
    from plot.events_plot import EventsPlot
except Exception:
    print("Woops, module EventsPlot not found")


def load_annotations(folder_path, extensions=[".csv"]):
    res_files = []
    dfs = []
    for root, dirs, files in os.walk(folder_path):
        for f in sorted(files):
            if not f[0] == ".":
                ext = f[-4:]
                if ext in extensions:
                    df = pd.read_csv(os.path.join(folder_path, f))
                    dfs.append(df)
                    res_files.append(f[:-14])
        break
    res = pd.concat(dfs)
    res.reset_index(inplace=True)
    return (res_files, res)


# Load raw data
events_data = feather.read_dataframe("../db/feather/song_events.feather")
recordings_data = feather.read_dataframe("../db/feather/recordings.feather")
files_with_annots, annots_df = load_annotations(
    "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/Priority/labels")

# clean annotations
annots_df = annots_df[["Filename", "Label",
                       "LabelStartTime_Seconds", "LabelEndTime_Seconds"]]
annots_df.rename(columns={"Filename": "name", "Label": "label",
                          "LabelStartTime_Seconds": "start", "LabelEndTime_Seconds": "end"}, inplace=True)
annots_df.name = annots_df.name.apply(lambda x: x[:-4])
annots_df["duration"] = annots_df.end - annots_df.start

# Get only recordings
# recordings = recordings_data.loc[(recordings_data["year"]
#                                   == "Data") & (recordings_data["plot"] == "Priority")]
#

recs_df = recordings_data.loc[recordings_data["name"].isin(files_with_annots)]
events_df = events_data.loc[events_data.recording_id.isin(recs_df.id)]
events_df = events_df.merge(
    recs_df[["id", "name"]], left_on="recording_id", right_on="id")
events_df["duration"] = events_df.end - events_df.start

print(annots_df)
print(events_df)


def merge_annotations(annots):
    res = []
    previous = None
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
                    print("annotation overlap, extending the last one")
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


for file in files_with_annots:
    print(file)
    res = {}
    annots = annots_df[annots_df.name == file]
    # merge overlapping annotations into one
    print(annots.shape[0])
    annots = merge_annotations(annots)
    print(annots)
    events = events_df[events_df.name == file]
    print(recs_df.loc[recs_df.name == file])
    res["dur_total"] = recs_df.loc[recs_df.name == file, "duration"].values[0]
    res["n_tot_annots"] = annots.shape[0]
    res["n_tot_events"] = events.shape[0]
    res["dur_tot_annots"] = np.sum(annots.duration)
    res["dur_tot_events"] = np.sum(events.duration)

    tmp = []
    for index, event in events.iterrows():

        dur_overlap = 0
        prop_overlap = 0
        dur_overestimate = event.duration
        prop_overestimate = 100
        # get tags that overlap with the detected event
        tags = annots.loc[(event.start < annots.end) &
                          (event.end > annots.start)]

        ntags = tags.shape[0]
        if ntags > 0:
            for idx, tag in tags.iterrows():
                dur_overlap = min(tag.end, event.end) - \
                    max(tag.start, event.start)
                prop_overlap = dur_overlap / tag.duration * 100
                dur_overestimate = event.duration - dur_overlap
                prop_overestimate = dur_overestimate / event.duration * 100
                print("found overlapping annotation for: " +
                      str(dur_overlap))
        tmp_res = {"ntags": ntags,
                   "dur_overlap": dur_overlap,
                   "prop_overlap": prop_overlap,
                   "dur_overestimate": dur_overestimate,
                   "prop_overestimate": prop_overestimate}
        tmp.append(tmp_res)
    over_res = pd.DataFrame(tmp)
    print(over_res.agg("mean"))
    print(res)
    break
