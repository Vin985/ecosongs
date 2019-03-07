import datetime
import math
import sys

import feather
import pandas as pd
from plotnine import (aes, annotate, facet_grid, facet_wrap, geom_errorbar,
                      geom_line, geom_point, geom_rect, geom_smooth, ggplot,
                      scale_colour_manual, scale_x_continuous, xlab, xlim,
                      ylab)

sys.path.append("..")


def prepare_data(data):
    data["julian"] = data["date"].dt.dayofyear
    data["hour"] = data["date"].dt.hour
    data = data.sort_values(["site", "plot", "julian", "date"])
    data = data.loc[(data["julian"] > 155) & (data["julian"] < 220)]
    return data


def join_tuple(to_join, sep):
    to_join = list(filter(None, to_join))
    if len(to_join) > 1:
        return sep.join(to_join)
    return to_join[0]


def check_dates(df, site_data):
    plot = site_data.loc[site_data["plot"] == df.name]
    res = df
    if not plot.empty:
        start = plot.depl_start.iloc[0]
        end = plot.depl_end.iloc[0]
        if not pd.isnull(start):
            res = df.loc[(df["date"] > start) & (df["date"] < end)]
        res["lat"] = plot.lat.iloc[0]
        res["lon"] = plot.lon.iloc[0]
    res.ACI = (res.ACI - res.ACI.mean()) / res.ACI.std()
    return res


# The palette with black:
cbbPalette = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#0072B2", "#D55E00", "#CC79A7"]
sites_excl = ["Station Nord", "Cape Churchill", "Coats Island", "Hochstetter"]
plot_excl = ["BARW_8", "IGLO_10", "IGLO_H"]
site_data = pd.read_excel("/home/vin/Doctorat/data/datasheet/2018/sites_deployment_2018.xlsx")

# Load song events
all_events = feather.read_dataframe("song_events_mac.feather")
all_events["duration"] = all_events["end"] - all_events["start"]
events_grouped = all_events.groupby(["recording_id"], as_index=False).agg({"event_id": "count"})
events_grouped.rename(columns={'event_id': 'n_events'}, inplace=True)
events_grouped


recordings = feather.read_dataframe("recordings_mac.feather")
recs = recordings[["id", "date", "name", "site", "plot", "path"]]

events = events_grouped.merge(recs, left_on="recording_id", right_on="id")
events = prepare_data(events)

weird = events[events.n_events > 400]
print(weird.path.to_list())
events = events.loc[~events.site.isin(sites_excl)]
events = events.loc[~events["plot"].isin(plot_excl)]

site_data


data = events
column = "n_events"


def aggregate_mean(data, column):
    data["type"] = column
    data.rename(columns={column: "value"}, inplace=True)
    res = data.groupby(["site", "julian", "type"], as_index=False).agg({"value": "mean"})
    # res.columns = pd.Index(join_tuple(i, "_") for i in res.columns)
    return res


res = aggregate_mean(events, "n_events")
res


def label_x(dates):
    res = [(datetime.datetime(2018, 1, 1) + datetime.timedelta(x)).strftime("%d-%m") for x in dates]
    print(res)
    return res


(ggplot(data=res, mapping=aes(x='julian', y='value', colour='site')) +
    xlab("Day")
    + ylab("Mean number of detected songs")
 # + facet_grid("site~", scales="free")
 # + geom_line()
 + facet_wrap("site", nrow=6, ncol=2, scales="free_y")
    + geom_point()
 # + geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
    + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
 + # + scale_colour_manual(values=cbbPalette, guide=False)
    scale_x_continuous(labels=label_x)).save("figs/song_events_all_smoothed.png", height=10, width=16, dpi=150)

(ggplot(data=res, mapping=aes(x='julian', y='value', colour='site')) +
    xlab("Day")
    + ylab("Mean number of detected songs")
  # + facet_grid("site~", scales="free")
    + geom_line()
 + facet_wrap("site", nrow=6, ncol=2, scales="free_y") +
    geom_point()
 # + geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
 + # + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
 # + scale_colour_manual(values=cbbPalette, guide=False)
    scale_x_continuous(labels=label_x)).save("figs/song_events_all_nosmooth.png", height=10, width=16, dpi=150)
