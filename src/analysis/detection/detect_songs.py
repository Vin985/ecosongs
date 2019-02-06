import pickle

import os
import pickle
import sys
import zipfile

import matplotlib.pyplot as plt
import numpy as np
import yaml
from six.moves import urllib
import pandas as pd

from analysis.detection.lib.tf_classifier import HOP_LENGTH, TFClassifier


preds = []

print("->  Making predictions for biotic")

with open('models/biotic/network_opts.yaml' % classifier_type) as f:
    options = yaml.load(f)

model_path = 'tf_models/%s/weights_99.pkl-1' % classifier_type

predictor = TFClassifier(options, model_path)
# preds[classifier_type] = predictor.classify('demo/SW154LA-3527_20130705_0909.wav')
preds = predictor.classify('/home/vin/Doctorat/data/acoustic/field/test2.wav')

print("-> ...Done")


with open('demo/predictions2.pkl', 'rb') as f:
    predictions = pickle.load(f)


def detect_songs_events(predictions, min_activity=0.6, min_duration=0):
    event_id = 0
    ongoing = False
    events = {}
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
                events[event_id] = {"start": start, "end": end}
    return events


events = detect_songs_events(predictions)
print(events)
len(events)
