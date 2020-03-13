import time

import numpy as np
import pandas as pd

from analysis.detection.lib.tf_classifier import HOP_LENGTH, TFClassifier
from analysis.detection.predictions_utils import predictions2pdf


def mp_initialize_detector(model_options, weight_path, detection_options):
    global DETECTOR, DETECTION_OPTIONS
    DETECTOR = TFClassifier(model_options, weight_path)
    DETECTION_OPTIONS = detection_options


def mp_detect_songs_chunk(recordings):
    res = []
    for rec in recordings:
        res += mp_detect_songs(rec)
    return (res, len(recordings))


def mp_detect_songs(recording):
    if 'DETECTOR' in globals():
        tic = time.time()
        preds = []
        # TODO: see if we can optimize with the recording object
        preds = DETECTOR.classify(recording.path)

        len_in_s = preds.shape[0] * HOP_LENGTH / DETECTOR.sample_rate
        timeseq = np.linspace(0, len_in_s, preds.shape[0])
        res_df = pd.DataFrame(
            {"recording_id": recording.id, "time": timeseq, "activity": preds})
        # print(res_df)
        # with open('demo/predictions2.pkl', 'wb') as f:
        #     pickle.dump(test, f, -1)
        if DETECTION_OPTIONS.get("export_pdf", False):
            predictions2pdf(res_df, recording)
        # events = detect_songs_events(res_df, recording_id=recording.id,

        #                              detection_options=DETECTION_OPTIONS)
        # print("Took %0.3fs to detect events mp" % (time.time() - tic))
        # return events
        return [res_df]
    return None


# def detect_songs(recording, classifier, detection_options):
#     tic = time.time()
#     preds = []
#     # TODO: see if we can optimize with the recording object
#     preds = classifier.classify(recording.path)
#     len_in_s = preds.shape[0] * HOP_LENGTH / classifier.sample_rate
#     timeseq = np.linspace(0, len_in_s, preds.shape[0])
#     res_df = pd.DataFrame({"time": timeseq, "activity": preds})
#     events = detect_songs_events(
#         res_df, recording_id=recording.id, **detection_options)
#     print("Took %0.3fs to detect events" % (time.time() - tic))
#     return events
