#%%
import inspect
import os
import time
import traceback

import numpy as np
import pandas as pd
import yaml

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
try:
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    from analysis.detection.lib.tf_classifier import HOP_LENGTH, CityNetClassifier1
except Exception:
    print("Woops, module not found")

model_opts = {
    "model_root_dir": "analysis/detection/models",
    "classifier": "biotic",
    "options_file": "analysis/detection/models/biotic/network_opts.yaml",
    "weights_file": "analysis/detection/models/biotic/weights_99.pkl-1",
}

stream = open("src/analysis/detection/models/biotic/network_opts.yaml", "r")
model_options = yaml.load(stream, Loader=yaml.Loader) or {}
model_options["resample"] = False
model_options["remove_noise"] = False
weight_path = "src/test/biotic/biotic"

detector = CityNetClassifier1(model_options, weight_path)

file_path = "src/test/example.wav"

tic = time.time()
preds = []
res_df = pd.DataFrame()
try:
    preds = detector.classify(file_path)

    len_in_s = preds.shape[0] * HOP_LENGTH / detector.sample_rate
    timeseq = np.linspace(0, len_in_s, preds.shape[0])
    res_df = pd.DataFrame({"recording_id": 1, "time": timeseq, "activity": preds})
    print(res_df)
except Exception:
    print(traceback.format_exc())
    print("Error classifying recording: ", file_path)
