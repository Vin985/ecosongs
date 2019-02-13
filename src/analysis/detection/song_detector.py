import time

import numpy as np
import pandas as pd

from analysis.detection.lib.tf_classifier import HOP_LENGTH, TFClassifier


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
        res_df = pd.DataFrame({"time": timeseq, "activity": preds})
        # with open('demo/predictions2.pkl', 'wb') as f:
        #     pickle.dump(test, f, -1)

        events = detect_songs_events(res_df, recording_id=recording.id, **DETECTION_OPTIONS)
        print("Took %0.3fs to detect events mp" % (time.time() - tic))
        return events
    return None


def detect_songs(recording, classifier, detection_options):
    tic = time.time()
    preds = []
    # TODO: see if we can optimize with the recording object
    preds = classifier.classify(recording.path)
    len_in_s = preds.shape[0] * HOP_LENGTH / classifier.sample_rate
    timeseq = np.linspace(0, len_in_s, preds.shape[0])
    res_df = pd.DataFrame({"time": timeseq, "activity": preds})
    events = detect_songs_events(res_df, recording_id=recording.id, **detection_options)
    print("Took %0.3fs to detect events" % (time.time() - tic))
    return events


def detect_songs_events(predictions, recording_id=-1, min_activity=0.6, min_duration=0):
    event_id = 0
    ongoing = False
    events = []
    start = 0
    end = 0
    # def detect_songs_events(predictions):
    for time, activity in predictions.itertuples(index=False):
        # Check if prediction is above a defined threshold
        if activity > min_activity:
            # If not in a song, create a new event
            if not ongoing:
                ongoing = True
                event_id += 1
                start = time
        elif ongoing:
            # If below the threshold and in an active event, end it
            ongoing = False
            end = time
            # log event if its duration is greater than minimum threshold
            if (end - start) > min_duration:
                events.append({"event_id": event_id, "recording_id": recording_id,
                               "start": start, "end": end})
    return events
