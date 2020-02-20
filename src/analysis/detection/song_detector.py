import os
import time

import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analysis.detection.lib.tf_classifier import HOP_LENGTH, TFClassifier
from db.models import TableModel


# class SongEventsTable(TableModel):
#     TABLE_NAME = "song_events"
#     COLUMNS = ["event_id", "recording_id", "start", "end"]

#     def __init__(self, df=None, dbmanager=None):
#         TableModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)

#     def add(self, new, save=False, replace=True):
#         # TODO: check duplicates
#         # TODO: add idx column?
#         # TODO: check duplicates
#         print(self.df)
#         new = self.check_ids(new)
#         if replace:
#             to_remove = new["recording_id"].unique()
#             self.df = self.df.loc[~self.df.recording_id.isin(to_remove)]
#         self.df = self.df.append(new, ignore_index=True, sort=True)
#         if save:
#             self.save()
#         # self.update(save=save)

#     def get_events(self, recording_id):
#         return self.df[self.df["recording_id"] == recording_id]


# class SongsSummaryTable(TableModel):
#     TABLE_NAME = "songs_summary"
#     COLUMNS = ["recording_id", "n_events", "path", "name"]

#     def __init__(self, df=None, dbmanager=None):
#         TableModel.__init__(self, self.COLUMNS, df=df, dbmanager=dbmanager)


def mp_initialize_detector(model_options, weight_path, detection_options):
    global DETECTOR, DETECTION_OPTIONS
    DETECTOR = TFClassifier(model_options, weight_path)
    DETECTION_OPTIONS = detection_options


def mp_detect_songs_chunk(recordings):
    res = []
    for rec in recordings:
        res += mp_detect_songs(rec)
    return (res, len(recordings))


def predictions2pdf(predictions, recording):
    fig = plt.figure(figsize=(15, 5))

    # plot spectrogram
    sp1 = fig.add_subplot(211)
    librosa.display.specshow(recording.spectrogram.spec)
    # plot activity
    sp2 = fig.add_subplot(212)
    sp2.plot(predictions["time"], predictions["activity"],
             'g', label='biotic activity')
    sp2.set_xlim([0, max(predictions["time"])])
    # fig.xlabel('Time (s)')
    #sp2.ylabel('Activity level')
    # fig.legend()

    # Save plots
    save_dir = 'plots/pdf/'
    print(os.getcwd())
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    fig.savefig(save_dir + recording.name + "_events.pdf")


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


def detect_songs(recording, classifier, detection_options):
    tic = time.time()
    preds = []
    # TODO: see if we can optimize with the recording object
    preds = classifier.classify(recording.path)
    len_in_s = preds.shape[0] * HOP_LENGTH / classifier.sample_rate
    timeseq = np.linspace(0, len_in_s, preds.shape[0])
    res_df = pd.DataFrame({"time": timeseq, "activity": preds})
    events = detect_songs_events(
        res_df, recording_id=recording.id, **detection_options)
    print("Took %0.3fs to detect events" % (time.time() - tic))
    return events


def detect_songs_events(predictions, recording_id=-1, detection_options=None):
    detection_options = detection_options or {}
    min_activity = detection_options.get("min_activity", 0.85)
    min_duration = detection_options.get("min_duration", 0.1)
    # min_interval = detection_options.get("min_interval", 0.1)
    end_threshold = detection_options.get("end_threshold", 0.6)
    event_id = 0
    ongoing = False
    events = []
    start = 0
    end = 0
    # def detect_songs_events(predictions):
    for pred_time, activity in predictions.itertuples(index=False):
        # Check if prediction is above a defined threshold
        if activity > min_activity:
            # If not in a song, create a new event
            if not ongoing:
                ongoing = True
                event_id += 1
                start = pred_time
        elif ongoing:
            # if above an end threshold, consider it as a single event
            if activity > end_threshold:
                continue
            # If below the threshold and in an active event, end it
            ongoing = False
            end = pred_time
            # log event if its duration is greater than minimum threshold
            if (end - start) > min_duration:
                events.append({"event_id": event_id, "recording_id": recording_id,
                               "start": start, "end": end})
    events = pd.DataFrame(events)
    return events
