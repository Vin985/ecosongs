# %%

import inspect
import os
import time

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
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
label_folder = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split/labels"


db_opts = {"database": "ecosongs", "db_type": "feather",
           "path": "/mnt/win/UMoncton/Doctorat/dev/ecosongs/src/db"}

dbmanager = dbutils.get_db_manager(**db_opts)
tables = TableManager(dbmanager)

# %%


recordings_df = tables.recordings.df
predictions_df = tables.activity_predictions.df
tags_df = tables.tags.df


predictions_df.merge(
    recordings_df[["id", "path"]], left_on="recording_id", right_on="id")


path = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split"
r = recordings_df.loc[recordings_df.path.str.startswith(path)]
r = r.loc[r.has_tags == 2]

# %%
tags = tags_df.loc[tags_df.recording_id.isin(r.id)]
preds = predictions_df.loc[predictions_df.recording_id.isin(tags.recording_id)]

# %%

det2 = SubsamplingDetector()
start = time.time()
opts, stats, events = det2.evaluate(preds, tags, {"min_activity": 0.9,
                                                  "min_duration": 0.1,
                                                  "end_threshold": 0.15})
end = time.time() - start
print("Lasted ", end)

# %%
# preds.loc[:, "datetime"] = pd.to_datetime(preds.time * 10**9)
# preds.set_index("datetime", inplace=True)
# p = preds[preds.recording_id == 80524]
# t = tags[tags.recording_id == 80524]
# e = events[events.recording_id == 80524]
# e.reset_index(inplace=True)
# e.set_index("datetime", inplace=True)

# p.activity.plot()
# e.tag.plot()
# e.event.plot()


# %%
