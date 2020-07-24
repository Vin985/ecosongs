# %%

import inspect
import os

import random
import numpy as np
import pandas as pd

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
try:
    from db import dbutils
    from db.tablemanager import TableManager
    from analysis.detection.detectors.standard_detector import StandardDetector
    from analysis.detection.detectors.subsampling_detector import SubsamplingDetector
except Exception:
    print("Woops, module EventsPlot not found")


audio_folder = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split"
label_folder = (
    "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split/labels"
)


db_opts = {
    "database": "ecosongs",
    "db_type": "feather",
    "path": "/mnt/win/UMoncton/Doctorat/dev/ecosongs/src/db",
}

dbmanager = dbutils.get_db_manager(**db_opts)
tables = TableManager(dbmanager)

# %%

recordings_df = tables.recordings.df
predictions_df = tables.activity_predictions.df
tags_df = tables.tags.df

#%%

recs_id = predictions_df.recording_id.cat.categories.tolist()
in_tags = tags_df.recording_id[tags_df.recording_id.isin(recs_id)].tolist()
rec_sample = random.sample(in_tags, 50)

preds = predictions_df.loc[predictions_df.recording_id.isin(rec_sample)]
tags = tags_df.loc[tags_df.recording_id.isin(rec_sample)]

std_detector = StandardDetector()

options = {
    "min_activity": 0.9,
    "min_duration": 0.35,
    "end_threshold": 0.15,
    "method": "standard",
}


tag = tags_df.loc[tags_df.recording_id == 93108]
pred = predictions_df.loc[predictions_df.recording_id == 93108]

#%%


def linearize_tags(nsteps, step, tag_df):
    res = np.zeros(nsteps)
    for tag in tag_df.itertuples():
        idx_start = int(round(tag.tag_start / step, 0))
        idx_end = int(round(tag.tag_end / step, 0))
        res[idx_start:idx_end] += 1
    res = pd.DataFrame(res)
    res.columns = ["has_tag"]
    return res


tmp = pred.time.to_numpy()
res3 = linearize_tags(len(tmp), tmp[1] - tmp[0], tag)
res3.has_tag.plot()


#%%


def calculate_tag_active_duration(tags):
    duration = 0
    previous_start, previous_end = 0, 0
    for tag in tags.itertuples():
        start = tag.tag_start
        end = tag.tag_end
        if previous_start < start < previous_end:
            if end > previous_end:
                duration += end - previous_end
                previous_end = end
        else:
            previous_start = start
            previous_end = end
            duration += end - start
    return duration


dur = calculate_tag_active_duration(tag)

#%%

res = std_detector.evaluate(preds, tags, options)


def event_overlap_duration(tags):
    tags.sort_values("tag_start")
    previous_end = tags.iloc[0].event_start
    overlap = 0
    for tag in tags.itertuples():
        if tag.tag_end > previous_end:
            end = min(tag.tag_end, tag.event_end)
            start = max(tag.tag_start, previous_end)
            overlap += end - start
            if end == tag.event_end:
                return overlap
            previous_end = end
    return overlap


event_overlap = (
    res["matches"][["event_id", "tag_start", "tag_end", "event_start", "event_end"]]
    .groupby("event_id")
    .apply(event_overlap_duration)
)

print(event_overlap)
