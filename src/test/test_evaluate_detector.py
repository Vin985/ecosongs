# %%

import datetime
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

# %%


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


def get_metrics(df, expand_index=False):
    if not "res" in df.columns:
        df.loc[:, "res"] = df.tag + df.event

    tp = len(df.res[df.res == 3])
    tn = len(df.res[df.res == 0])
    fp = len(df.res[df.res == 2])
    fn = len(df.res[df.res == 1])

    if expand_index:
        df2 = df.loc[(df.tag_index != "") & (df.event > 0)]
        tmp = df2.tag_index.unique()
        matched_tags = set(",".join(tmp).split(","))
        all_tags = df.tag_index[df.tag_index != ""].unique()
        all_tags = set(",".join(all_tags).split(","))

    else:
        df2 = df.loc[(df.tag_index > -1) & (df.event > 0)]
        matched_tags = df2.tag_index.unique()
        all_tags = df.tag_index[df.tag_index > -1].unique()

    fn2 = len(all_tags) - len(matched_tags)

    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    recall2 = tp/(tp+fn2)
    return {"precision": precision, "recall": recall,
            "recall2": recall2, "tp": tp, "tn": tn,
            "fp": fp, "fn": fn, "fn2": fn2}

# %%


RECORDING = 80233
# RECORDING = 80534

predictions.loc[:, "tag"] = 0
predictions.loc[:, "tag_index"] = -1
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
    #preds.loc[preds.time.between(x["tag_start"], x["tag_end"]), "tag"] = 1
    #preds.loc[preds.time.between(x["tag_start"], x["tag_end"]), "tag_index"] = x.tag_index
    preds.loc[preds.time.between(x["tag_start"], x["tag_end"]), [
        "tag", "tag_index"]] = [1, x["tag_index"]]

for _, x in ev.iterrows():
    preds.loc[preds.time.between(
        x["event_start"], x["event_end"]), "event"] = 2

preds.activity.plot()
preds.tag.plot()
preds.event.plot()

# %%
get_metrics(preds)

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

roll = preds.copy()

roll.loc[:, "roll"] = roll["activity"].rolling(30, center=True).apply(
    rolling_max, raw=True, kwargs={"threshold": 0.98, "mean_thresh": 0})

roll.tag.plot()
roll.roll.plot()

roll.loc[:, "res"] = roll.tag + roll.roll

get_metrics(roll)

# tp = len(preds.res2[preds.res2 == 3])
# tn = len(preds.res2[preds.res2 == 0])
# fp = len(preds.res2[preds.res2 == 2])
# fn = len(preds.res2[preds.res2 == 1])

# precision = tp/(tp+fp)
# recall = tp/(tp+fn)
# print(precision)
# print(recall)

# %%

start = preds.index.min()
end = preds.index.max()
summary_range = pd.date_range(start, end, freq="300ms")
man_roll = pd.DataFrame({"tag": [0] * len(summary_range),
                         "event": [0]*len(summary_range)})
man_roll.set_index(summary_range, inplace=True)

for stop in summary_range:
    if start == stop:
        continue
    if any(preds[start: stop].tag > 0):
        man_roll.loc[stop, "tag"] = 1
    if any(preds[start: stop].event > 0):
        man_roll.loc[stop, "event"] = 2
    start = stop

man_roll.loc[:, "res"] = man_roll.tag + man_roll.event

preds.tag.plot()
# res.tag.plot()
# preds.event.plot()
man_roll.event.plot()

get_metrics(man_roll)

# %%


def resample_max(x, threshold=0.98, mean_thresh=0.1):
    if any(x >= threshold) and x.mean() > mean_thresh:
        return 2
    return 0


def has_tag(x):
    if any(x) > 0:
        return 1
    return 0


def get_tag_index(x):
    tmp = x[x > -1]
    idx = ",".join(list(map(str, tmp.unique())))
    return idx
    # return ",".join()


resampled = preds.resample("300ms")

res = resampled.agg({"activity": resample_max,
                     "tag": has_tag, "tag_index": get_tag_index})

res.rename(columns={"activity": "event"}, inplace=True)
res.event.plot()
res.tag.plot()


get_metrics(res, expand_index=True)
# res = preds["activity"].resample("500ms").apply(
#     resample_max, threshold=0.98, mean_thresh=0.2)

# res.plot()
# preds.tag.plot()
# preds.activity.plot()

# %%

res_ev = res.loc[res.event > 0]
res_ev.reset_index(inplace=True)


step = datetime.timedelta(milliseconds=300)
start = None
events = []
event_id = 1
print(len(res_ev))
for i, x in res_ev.iterrows():
    if not start:
        prev_time = x.datetime
        start = prev_time
        continue
    diff = x.datetime - prev_time
    if diff > step:
        end = prev_time + step
        events.append({"event_id": event_id, "recording_id": RECORDING,
                       "start": start, "end": end})
        event_id += 1
        start = x.datetime
    prev_time = x.datetime

events.append({"event_id": event_id, "recording_id": RECORDING,
               "start": start, "end": prev_time+step})


events = pd.DataFrame(events)
print(events)


# print(diff)
# print(x)

# %%
