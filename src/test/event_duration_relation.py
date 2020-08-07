#%%
import inspect
import math
import os
import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyqtgraph as pg
from pyqtgraph.graphicsItems.AxisItem import AxisItem
from pyqtgraph.Qt import QtCore, QtGui
from sklearn import linear_model

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
try:
    from db import dbutils
    from analysis.detection.detectors.standard_detector import StandardDetector
except Exception:
    print("Woops, module EventsPlot not found")


# raw_matches = pd.read_csv("src/test/db/matches.csv")
raw_matches = pd.read_csv("db/matches2.csv")
tags_df = pd.read_csv("db/tags2.csv")
events_df = pd.read_csv("db/events2.csv")
# raw_matches = raw_matches.astype({"tag": "category"})

# matches2 = raw_matches.drop_duplicates("tag_id").copy()

#%%
events_total_dur = (
    events_df[["recording_id", "event_duration"]].groupby("recording_id").apply(sum)
)["event_duration"].reset_index()


def get_duration_relation(tags, events):
    events_duration = (
        events[["recording_id", "event_duration"]].groupby("recording_id").apply(sum)
    )["event_duration"].reset_index()
    tags_duration = (
        tags.groupby("recording_id")
        .apply(StandardDetector.tags_active_duration)
        .reset_index()
    )
    merged = tags_duration.merge(events_duration).rename(columns={0: "tags_duration"})
    regr = linear_model.LinearRegression()
    X = merged["tags_duration"].values.reshape(-1, 1)
    Y = merged["event_duration"].values.reshape(-1, 1)
    # Train the model using the training sets
    regr.fit(X, Y)

    plt.scatter(X, Y, color="black")
    plt.plot(X, regr.predict(X), color="blue", linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()

    r2 = regr.score(X, Y)
    print(r2)
    return r2


#%%

res1 = get_duration_relation(tags_df, events_df)
res2 = get_duration_relation(tags_df.loc[tags_df.background == False], events_df)

# res3 = get_duration_relation(tags_df, events_df.loc[events_df.matched == 1])

