# %%

import os
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
try:
    from db import dbutils
    from db.tablemanager import TableManager
    from analysis.detection.detectors.standard_detector import StandardDetector
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
# %%

path = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split"
r = recordings_df.loc[recordings_df.path.str.startswith(path)]
r = r.loc[r.has_tags == 2]

# %%
tags = tags_df.loc[tags_df.recording_id.isin(r.id)]
preds = predictions_df.loc[predictions_df.recording_id.isin(tags.recording_id)]


# %%

det = StandardDetector()

det.evaluate(preds, tags, {"min_activity": 0.9,
                           "min_duration": 0.35,
                           "end_threshold": 0.15})

# %%

stats = tables.detector_statistics.df
max_precision = stats.loc[stats.precision == max(stats.precision)]
opts = tables.analysis_options.df
max_prec_opt = opts.loc[opts.id == max_precision.analysis_options.values[0]]
print(max_prec_opt.values[0])

# Best F1 score
det.evaluate(preds, tags, {"min_activity": 0.9,
                           "min_duration": 0.35,
                           "end_threshold": 0.15})

# %%

stats = tables.detector_statistics.df
max_precision = stats.loc[stats.precision == max(stats.precision)]
opts = tables.analysis_options.df
max_prec_opt = opts.loc[opts.id == max_precision.analysis_options.values[0]]
print(max_prec_opt.values[0])

# Best precision
det.evaluate(preds, tags, {"min_activity": 0.95,
                           "min_duration": 0.49,
                           "end_threshold": 0.15})


# %%

# Max recall
stats = tables.detector_statistics.df
max_recall = stats.loc[stats.recall == max(stats.recall)]
opts = tables.analysis_options.df
max_recall_opt = opts.loc[opts.id == max_recall.analysis_options.values[0]]
print(max_recall_opt.values[0])

# Best recall: 0.97 (precision=0.67, F1_score=0.79)
det.evaluate(preds, tags, {"min_activity": 0.6,
                           "min_duration": 0.01,
                           "end_threshold": 0.6})
