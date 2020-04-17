# %%

import os
import inspect
import pandas as pd
import numpy as py

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


audio_folder = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split"
label_folder = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split/labels"


db_opts = {"database": "ecosongs", "db_type": "feather",
           "path": "/mnt/win/UMoncton/Doctorat/dev/ecosongs/src/db"}

dbmanager = dbutils.get_db_manager(**db_opts)
tables = TableManager(dbmanager)


def profile_function(audio_folder, label_folder):

    files, tags_df = detector_evaluation.load_annotations(root_path=audio_folder,
                                                          tags_path=label_folder,
                                                          only_done=True)

    paths = [os.path.join(audio_folder, file_name)
             for file_name in files]
    recordings_df = tables.recordings.get_recordings_by_path(paths)
    recording_ids = recordings_df.id.tolist()
    predictions_df = tables.activity_predictions.get_predictions_by_recordings(
        recording_ids)

    event_options = {"min_activity": 0.9,
                     "min_duration": 0.1,
                     "end_threshold": 0.6}
    events_df = detector_evaluation.get_events(
        predictions_df, event_options)

    events_df = detector_evaluation.prepare_events(
        events_df, recordings_df)

    matches_df = detector_evaluation.get_matches(events_df, tags_df)
    stats = detector_evaluation.get_stats(matches_df, events_df)
    print(stats)
    return(predictions_df, tags_df, recordings_df, events_df, matches_df, stats)


predictions, tags, recordings, events, matches, stats = profile_function(
    audio_folder, label_folder)

# %%

RECORDING = 80233
# RECORDING = 80534

predictions.loc[:, "tag"] = 0
predictions.loc[:, "event"] = 0
predictions.loc[:, "datetime"] = pd.to_datetime(predictions.time * 10**9)
rec = recordings[recordings.id == RECORDING]
m = matches[matches.recording_id == RECORDING]
ev = events[events.recording_id == RECORDING]


tags_id = m.tag_index.unique()
t = tags.loc[tags.tag_index.isin(tags_id)]
print(t)
# %%
preds = predictions.loc[predictions.recording_id == RECORDING].copy()
preds.set_index("datetime", inplace=True)

for _, x in t.iterrows():
    if "Human" in x.tags:
        print("Human!!")
    preds.loc[preds.time.between(x["tag_start"], x["tag_end"]), "tag"] = 1

for _, x in ev.iterrows():
    preds.loc[preds.time.between(
        x["event_start"], x["event_end"]), "event"] = 2

preds.activity.plot()
preds.tag.plot()
preds.event.plot()

# preds.loc[preds.time.between(t.iloc[0].tag_start, t.iloc[0].tag_end)]
# preds.loc[preds.time.between(
#     t.iloc[0].tag_start, t.iloc[0].tag_end), "tag"] = t.iloc[0].tag_index


# def rolling_test(x):
#     print(x)
#     return x


# preds.rolling(window=10).mean().plot()
# preds.rolling(window=10).apply(rolling_test, raw=True)


# dft = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]},
#                    index=pd.date_range('20130101 09:00:00',
#                                        periods=5,
#                                        freq='s'))
# dft.rolling(2).sum()

# %%

def rolling_max(x, threshold=0.95, mean_thresh=0.1):
    if any(x >= threshold) and x.mean() > mean_thresh:
        return 2
    return 0

# %%


# r = preds.rolling("1s").mean()
# r.activity.plot()
# r = preds.rolling("2s").mean()
# r.activity.plot()
# r = preds.rolling("3s").mean()
# r.activity.plot()<
# r = preds.rolling("300ms").mean()
# r.activity.plot()

# r = preds.rolling(40, center=True).mean()
# r.activity.plot()


preds.loc[:, "roll"] = preds["activity"].rolling(30, center=True).apply(
    rolling_max, raw=True, kwargs={"threshold": 0.98, "mean_thresh": 0})

preds.tag.plot()
preds.roll.plot()

preds.loc[:, "res2"] = preds.tag + preds.roll

tp = len(preds.res2[preds.res2 == 3])
tn = len(preds.res2[preds.res2 == 0])
fp = len(preds.res2[preds.res2 == 2])
fn = len(preds.res2[preds.res2 == 1])

precision = tp/(tp+fp)
recall = tp/(tp+fn)
print(precision)
print(recall)
# %%


# %%
preds.tag.plot()
preds.event.plot()

preds.loc[:, "res"] = preds.tag + preds.event

tp = len(preds.res[preds.res == 3])
tn = len(preds.res[preds.res == 0])
fp = len(preds.res[preds.res == 2])
fn = len(preds.res[preds.res == 1])

precision = tp/(tp+fp)
recall = tp/(tp+fn)
print(precision)
print(recall)

# %%

start = preds.index.min()
end = preds.index.max()
summary_range = pd.date_range(start, end, freq="300ms")
res = pd.DataFrame({"tag": [0] * len(summary_range),
                    "event": [0]*len(summary_range)})
res.set_index(summary_range, inplace=True)

for stop in summary_range:
    if start == stop:
        continue
    if any(preds[start: stop].tag > 0):
        res.loc[stop, "tag"] = 1
    if any(preds[start: stop].event > 0):
        res.loc[stop, "event"] = 2
    start = stop

res.loc[:, "res"] = res.tag + res.event

preds.tag.plot()
# res.tag.plot()
# preds.event.plot()
res.event.plot()


tp = len(res.res[res.res == 3])
tn = len(res.res[res.res == 0])
fp = len(res.res[res.res == 2])
fn = len(res.res[res.res == 1])

precision = tp/(tp+fp)
recall = tp/(tp+fn)
print(precision)
print(recall)

# %%


def resample_max(x, threshold=0.98, mean_thresh=0.1):
    if any(x >= threshold) and x.mean() > mean_thresh:
        return 2
    return 0


def has_tag(x):
    if any(x) > 0:
        return 1
    return 0


resampled = preds.resample("500ms")

res = resampled.agg({"activity": resample_max,
                     "tag": has_tag})

res.activity.plot()
res.tag.plot()

# res = preds["activity"].resample("500ms").apply(
#     resample_max, threshold=0.98, mean_thresh=0.2)

# res.plot()
# preds.tag.plot()
# preds.activity.plot()

# %%
