import datetime
import math
import os
import sys

import feather
import pandas as pd
from plotnine import (aes, annotate, facet_grid, facet_wrap, geom_errorbar,
                      geom_line, geom_point, geom_rect, geom_smooth, ggplot,
                      scale_colour_manual, scale_x_continuous, xlab, xlim,
                      ylab)

from audio.recording import RecordingTable
from db import dbutils

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
sites = ["Barrow"]
plot_excl = ["BARW_8"]
site_data = pd.read_excel("/home/vin/Doctorat/data/datasheet/2018/sites_deployment_2018.xlsx")

# Load song events
all_events = feather.read_dataframe("/home/vin/Doctorat/dev/ecosongs/src/db/feather/song_events_BARROW.feather")
all_events["duration"] = all_events["end"] - all_events["start"]
events_grouped = all_events.groupby(["recording_id"], as_index=False).agg({"event_id": "count"})
events_grouped.rename(columns={'event_id': 'n_events'}, inplace=True)
events_grouped
dbmanager = dbutils.get_db_manager(database="ecosongs",
                                   type="hdf5",
                                   path="../db")
recordings_table = RecordingTable(dbmanager=dbmanager)
recordings = recordings_table.df
recs = recordings[["id", "date", "name", "site", "plot"]]

events = events_grouped.merge(recs, left_on="recording_id", right_on="id")
events = prepare_data(events)

events

# Load ACI
aci = feather.read_dataframe("/home/vin/Doctorat/dev/ecosongs/src/plots/ACI.feather")
aci = aci.loc[aci.site.isin(sites)]
aci = aci.loc[~aci["plot"].isin(plot_excl)]
aci = aci[["ACI", "date", "site", "plot"]]
aci = prepare_data(aci)
aci

data = events
column = "n_events"
data
res


def aggregate_mean(data, column):
    data["type"] = column
    data.rename(columns={column: "value"}, inplace=True)
    res = data.groupby(["site", "julian", "type"], as_index=False).agg({"value": "mean"})
    # res.columns = pd.Index(join_tuple(i, "_") for i in res.columns)
    return res


res = pd.concat([aggregate_mean(events, "n_events"), aggregate_mean(aci, "ACI")])

# res = aci.groupby(["plot"], as_index=False).apply(check_dates, site_data)
# res = res.groupby(["site", "julian"], as_index=False).agg({"ACI": ["mean", "std"], "lat": "mean", "lon": "mean"})
# res.columns = pd.Index(join_tuple(i, "_") for i in res.columns)
# print(aci.loc[aci["site"] == "Igloolik"])
# print(aci)
res
# res.to_feather("data_glm.feather")


def label_x(dates):
    res = [(datetime.datetime(2018, 1, 1) + datetime.timedelta(x)).strftime("%d-%m") for x in dates]
    print(res)
    return res


(ggplot(data=res, mapping=aes(x='julian', y='value', colour='type'))
    + xlab("Day")
    + ylab("Mean number of detected songs")
    + facet_grid("type~", scales="free")
    # + geom_line()
	# + facet_wrap("type", nrow=2, ncol=1)
    + geom_point()
    # + geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
    + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
	+ scale_colour_manual(values=cbbPalette, guide=False)
    + scale_x_continuous(labels=label_x)).save("figs/song_events_aci_BARROW_mean_smoothed.png", height=10, width=16, dpi=150)

(ggplot(data=res, mapping=aes(x='julian', y='n_events_sum', colour='site'))
    + xlab("Day")
    + ylab("Total number of detected songs")
    # + facet_grid("site~", scales="free")
	# + facet_wrap("site", nrow=2, ncol=3)
    + geom_point()
    # + geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
    + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
	+ scale_colour_manual(values=cbbPalette, guide=False)
    + scale_x_continuous(labels=label_x)).save("figs/song_events_BARW0_sum.png", height=10, width=16, dpi=150)

#################
### Denoising ###
#################

# Test sans bruit
aci2 = aci.loc[aci["site"] == "East Bay"]
res2 = aci2.groupby(["denoised", "julian"]).mean()
res2 = res2.reset_index()
# res2 = aci2

(ggplot(data=res2, mapping=aes(x='julian', y='ACI', colour='denoised'))
    + facet_grid("denoised~", scales="free")
    # + geom_line()
    + geom_smooth(method="mavg", se=False, method_args={"window": 3, "center": True, "min_periods": 1})
    + scale_x_continuous(labels=label_x)).save("figs/ACI_EABA_denoising.png", height=10, width=8, dpi=150)


################
### Igloolik ###
################
iglo = res[res.site == "Igloolik"]
iglo_nest = pd.read_excel("/home/vin/Doctorat/data/datasheet/2018/IGLO/nest_IGLO_2018.xlsx")
iglo_nest.columns
iglo_nest["julian"] = iglo_nest.date.dt.dayofyear
iglo_nest.loc[iglo_nest.type == "incubation", "julian"] += 4

inc_start = iglo_nest[iglo_nest.type == "incubation"].julian.min()
inc_end = iglo_nest[iglo_nest.type == "incubation"].julian.max()
inc_lbl_pos = inc_start + (inc_end - inc_start)/2
hatch_start = iglo_nest[iglo_nest.type == "hatch"].julian.min()
hatch_end = min(iglo_nest[iglo_nest.type == "hatch"].julian.max(), iglo.julian.max() + 2)
hatch_lbl_pos = hatch_start + (hatch_end - hatch_start)/2

xmin = min(inc_start, iglo.julian.min())
xmax = min(iglo_nest[iglo_nest.type == "hatch"].julian.max(), iglo.julian.max() + 2)

(ggplot(data=iglo, mapping=aes(x='julian', y='ACI_mean', colour='site'))
 #+ facet_grid("panel~", scales="free")
 + xlab("Day")
 + ylab("Mean daily ACI (standardized)")
 + geom_point()
 # + geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
 + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
 + annotate("rect", xmin=[inc_start, hatch_start], xmax=[inc_end, hatch_end],
            ymin=-math.inf, ymax=math.inf, alpha=0.1, fill=["red", "blue"])
 + annotate("text", x=[inc_lbl_pos, hatch_lbl_pos], y=1.8, label=["Incubation end", "Hatch"])
 # + geom_line(data = inc, mapping=aes(x="julian", y="uniqueID"), colour="black")
 #    + geom_smooth(data=inc, mapping=aes(x="julian", y="uniqueID"), colour="black", method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
 + scale_x_continuous(labels=label_x, limits=[xmin, xmax])).save("figs/ACI_IGLO_endinc_noerr.png", height=8, width=8, dpi=150)

iglo_inc = iglo_nest.groupby("julian", as_index=False).uniqueID.count().reset_index()

(ggplot(data=iglo_inc, mapping=aes(x="julian", y="uniqueID"))
    + xlab("Day")
    + ylab("Number of nest initiation/hatch")
    + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
    + annotate("rect", xmin=[inc_start, hatch_start], xmax=[inc_end, hatch_end],
               ymin=-math.inf, ymax=math.inf, alpha=0.1, fill=["red", "blue"])
    + annotate("text", x=[inc_lbl_pos, hatch_lbl_pos], y=11, label=["incubation", "hatch"])
    + scale_x_continuous(labels=label_x, limits=[xmin, xmax])).save("figs/Nest_IGLO_endinc.png", height=8, width=8, dpi=150)


#############
## BARROW ###
#############


barw = res[res.site == "Barrow"]
barw_nest = pd.read_excel("/home/vin/Doctorat/data/datasheet/2018/BARW/BARW_incubation_hatch_dates_2018.xlsx", sheet_name=1)
barw_nest["julian"] = barw_nest.date.dt.dayofyear
barw_nest.loc[barw_nest.type == "incubation", "julian"] += 4

inc_start = barw_nest[barw_nest.type == "incubation"].julian.min()
inc_end = barw_nest[barw_nest.type == "incubation"].julian.max()
inc_lbl_pos = inc_start + (inc_end - inc_start)/2
hatch_start = barw_nest[barw_nest.type == "hatch"].julian.min()
hatch_end = barw_nest[barw_nest.type == "hatch"].julian.max()
hatch_lbl_pos = hatch_start + (hatch_end - hatch_start)/2

xmin = min(inc_start, barw.julian.min())
xmax = min(barw_nest[barw_nest.type == "hatch"].julian.max(), barw.julian.max() + 2)

(ggplot(data=res2, mapping=aes(x='julian', y='ACI_mean', colour='site'))
 #+ facet_grid("panel~", scales="free")
 + xlab("Day")
 + ylab("Mean daily ACI (standardized)")
 + geom_point()
 # + geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
 + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
 + annotate("rect", xmin=[inc_start, hatch_start], xmax=[inc_end, hatch_end],
            ymin=-math.inf, ymax=math.inf, alpha=0.1, fill=["red", "blue"])
 + annotate("text", x=[inc_lbl_pos, hatch_lbl_pos], y=2.1, label=["Incubation end", "Hatch"])
 # + geom_line(data = inc, mapping=aes(x="julian", y="uniqueID"), colour="black")
 #    + geom_smooth(data=inc, mapping=aes(x="julian", y="uniqueID"), colour="black", method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
 + scale_x_continuous(labels=label_x, limits=[xmin, xmax])).save("figs/ACI_BARW_incend.png", height=8, width=8, dpi=150)

inc = barw_nest.groupby("julian", as_index=False).uniqueID.count().reset_index()

(ggplot(data=inc, mapping=aes(x="julian", y="uniqueID"))
    + xlab("Day")
    + ylab("Number of nest initiation/hatch")
    + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
    + annotate("rect", xmin=[inc_start, hatch_start], xmax=[inc_end, hatch_end],
               ymin=-math.inf, ymax=math.inf, alpha=0.1, fill=["red", "blue"])
    + annotate("text", x=[inc_lbl_pos, hatch_lbl_pos], y=4.5, label=["incubation", "hatch"])
    + scale_x_continuous(labels=label_x, limits=[xmin, xmax])).save("figs/Nest_BARW_incend.png", height=8, width=8, dpi=150)


res3 = aci.loc[aci.site == "Barrow"]
res3 = res3.groupby(["plot"], as_index=False).apply(check_dates, site_data)
res3.reset_index()
res3 = res3.groupby(["plot", "julian"], as_index=False).agg({"ACI": ["mean", "std"], "lat": "mean", "lon": "mean"})
res3.columns = pd.Index(join_tuple(i, "_") for i in res3.columns)
res3
(ggplot(data=res3, mapping=aes(x='julian', y='ACI_mean', colour='plot'))
    + xlab("Day")
    + ylab("Mean daily ACI (standardized)")
    + facet_grid("plot~", scales="free")
    + geom_point()
    + geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
    + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
    + scale_x_continuous(labels=label_x))  # .save("figs/ACI_BARW_plots2.png", height=12, width=8, dpi=150)
