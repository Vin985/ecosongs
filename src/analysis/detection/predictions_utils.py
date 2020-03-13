import os

import librosa.display
import matplotlib.pyplot as plt
import pandas as pd


def predictions2pdf(predictions, recording):
    fig = plt.figure(figsize=(15, 5))

    # plot spectrogram
    sp1 = fig.add_subplot(211)
    librosa.display.specshow(recording.create_spectrogram().spec)
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


def detect_songs_events(predictions, recording_id=-1, detection_options=None):
    predictions = predictions[["time", "activity"]]
    detection_options = detection_options or {}
    min_activity = detection_options.get("min_activity", 0.85)
    min_duration = detection_options.get("min_duration", 0.1)
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
