#%%
import inspect
import os
import time
import traceback
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
import feather

# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, "/mnt/win/UMoncton/Doctorat/dev/ecosongs/src")
try:
    # os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    from analysis.detection.lib.tf_classifier import HOP_LENGTH, CityNetClassifier1
    from db import dbutils
    from db.tablemanager import TableManager
    from analysis.detection.detectors import DETECTORS
except Exception:
    print("Woops, module not found")


def get_model(model_opts):
    stream = open(model_opts["options_file"], "r")
    model_options = yaml.load(stream, Loader=yaml.Loader) or {}
    model_options["resample"] = False
    model_options["remove_noise"] = False
    weight_path = model_opts["weight_path"]

    model = CityNetClassifier1(model_options, weight_path)
    return model


def get_predictions(recordings, model, hop_length=HOP_LENGTH):
    res = []
    for recording in recordings.itertuples():
        preds = []
        res_df = pd.DataFrame()
        # TODO: see if we can optimize with the recording object
        try:
            preds = model.classify(recording.path)
            len_in_s = preds.shape[0] * hop_length / model.sample_rate
            timeseq = np.linspace(0, len_in_s, preds.shape[0])
            res_df = pd.DataFrame(
                {"recording_id": recording.id, "time": timeseq, "activity": preds}
            )
        except Exception:
            print("Error classifying recording: ", recording.path)
            print(traceback.format_exc())
        res.append(res_df)
    res = pd.concat(res)
    return res


def evaluate_model(model_options, detector):
    if not os.path.exists(model_options["save_dest"]):
        model = get_model(model_options)
        predictions = get_predictions(recordings, model)
        predictions.reset_index(drop=True).to_feather(model_options["save_dest"])
    else:
        predictions = feather.read_dataframe(model_options["save_dest"])
    res = detector.evaluate(predictions, tags, {})
    return res


#%%

db_path = Path("../test_db/")


recordings = feather.read_dataframe(db_path / "recordings.feather")
tags = feather.read_dataframe(db_path / "tags.feather")

evaluator = DETECTORS["standard"]

#%%
model1_opts = {
    "options_file": "../models/biotic/network_opts.yaml",
    "weight_path": "../models/biotic/biotic",
    "save_dest": db_path / "predictions_model1.feather",
}

res1 = evaluate_model(model1_opts, evaluator)

#%%
model2_opts = {
    "name": "citynet1.1",
    "model_root": "../models/",
    "options_file": "../models/citynet1.1/network_opts.yaml",
    "weight_path": "../models/citynet1.1/weights_1.pkl-1",
    "save_dest": db_path / "predictions_citynet1.1.feather",
    "save_dest_root": db_path,
}

res2 = evaluate_model(model2_opts, evaluator)


#%%


# db_opts = {
#     "database": "ecosongs",
#     "db_type": "feather",
#     "path": "/mnt/win/UMoncton/Doctorat/dev/ecosongs/src/db",
# }

# dbmanager = dbutils.get_db_manager(**db_opts)
# tables = TableManager(dbmanager)

# audio_folder_root = Path(
#     "/mnt/win/UMoncton/McGill University/Tommy O'Neill Sanger - Labeled Recordings"
# )
# audio_files = [str(path) for path in audio_folder_root.rglob("*.WAV")]


# db_path = Path("../test_db/")
# test_dbs = {
#     "recordings": db_path / "recordings.feather",
#     "tags": db_path / "tags.feather",
#     "predictions": db_path / "predictions.feather",
# }


# if not os.path.exists(test_dbs["recordings"]):
#     recordings_df = tables.recordings.df
#     recordings = recordings_df.loc[recordings_df.path.isin(audio_files)].reset_index(
#         drop=True
#     )
#     recordings.to_feather(test_dbs["recordings"])
# else:
#     recordings = feather.read_dataframe(test_dbs["recordings"])

# if not os.path.exists(test_dbs["tags"]):
#     tags_df = tables.tags.df
#     tags = tags_df.loc[tags_df.recording_id.isin(recordings.id)].reset_index(drop=True)
#     tags.to_feather(test_dbs["tags"])
# else:
#     tags = feather.read_dataframe(test_dbs["tags"])
