
import datetime
import math

import numpy as np
import pandas as pd

import feather
from plotnine import (aes, annotate, facet_grid, geom_errorbar, geom_line,
                      geom_point, geom_rect, geom_smooth, ggplot,
                      scale_x_continuous, xlab, xlim, ylab)


def join_tuple(tuple, sep):
  tuple = list(filter(None, tuple))
  if len(tuple) > 1:
      return sep.join(tuple)
  return tuple[0]


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


sites = ["Igloolik", "East Bay", "Barrow", "Burntpoint Creek", "Canning River", "Svalbard"]
plot_excl = ["BARW_8"]

site_data = pd.read_excel("/home/vin/Doctorat/data/datasheet/2018/sites_deployment_2018.xlsx")

site_data

# aci = feather.read_dataframe("src/plots/ACI.feather")
aci = feather.read_dataframe("ACI.feather")
# aci.date = aci.date.dt.tz_localize("UTC")
aci = aci.loc[aci.site.isin(sites)]
aci = aci.loc[~aci["plot"].isin(plot_excl)]
aci["julian"] = aci["date"].dt.dayofyear
aci["hour"] = aci["date"].dt.hour
aci = aci.sort_values(["site", "plot", "julian", "date"])
aci = aci.loc[(aci["julian"] > 155) & (aci["julian"] < 220)]
aci = aci.loc[(aci["ACI"] < 50000)]
aci = aci.loc[aci["denoised"] == False]


res = aci.groupby(["plot"], as_index=False).apply(check_dates, site_data)
res = res.groupby(["site", "julian"], as_index=False).agg({"ACI": ["mean", "std"], "lat": "mean", "lon": "mean"})
res.columns = pd.Index(join_tuple(i, "_") for i in res.columns)
# print(aci.loc[aci["site"] == "Igloolik"])
# print(aci)
res
# res.to_feather("data_glm.feather")


def label_x(dates):
    res = [(datetime.datetime(2018, 1, 1) + datetime.timedelta(x)).strftime("%d-%m") for x in dates]
    print(res)
    return res


(ggplot(data=res, mapping=aes(x='julian', y='ACI_mean', colour='site'))
    + xlab("Day")
    + ylab("Mean daily ACI (standardized)")
    + facet_grid("site~", scales="free")
    #+ geom_point()
    #+ geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
    + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
    + scale_x_continuous(labels=label_x))  # .save("figs/ACI_all_noise_mavg_win4.png", height=14, width=8, dpi=150)


################
### Igloolik ###
################
iglo = res[res.site == "Igloolik"]
iglo_nest = pd.read_excel("/home/vin/Doctorat/data/datasheet/2018/IGLO/nest_IGLO_2018.xlsx")
iglo_nest.columns
iglo_nest["julian"] = iglo_nest.date.dt.dayofyear

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
 + geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
 + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
 + annotate("rect", xmin=[inc_start, hatch_start], xmax=[inc_end, hatch_end],
            ymin=-math.inf, ymax=math.inf, alpha=0.1, fill=["red", "blue"])
 + annotate("text", x=[inc_lbl_pos, hatch_lbl_pos], y=3.5, label=["Incubation", "Hatch"])
 # + geom_line(data = inc, mapping=aes(x="julian", y="uniqueID"), colour="black")
 #    + geom_smooth(data=inc, mapping=aes(x="julian", y="uniqueID"), colour="black", method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
 + scale_x_continuous(labels=label_x, limits=[xmin, xmax])).save("figs/ACI_IGLO_inc_hatch3.png", height=8, width=8, dpi=150)

iglo_inc = iglo_nest.groupby("julian", as_index=False).uniqueID.count().reset_index()

(ggplot(data=iglo_inc, mapping=aes(x="julian", y="uniqueID"))
    + xlab("Day")
    + ylab("Number of nest initiation/hatch")
    + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
    + annotate("rect", xmin=[inc_start, hatch_start], xmax=[inc_end, hatch_end],
               ymin=-math.inf, ymax=math.inf, alpha=0.1, fill=["red", "blue"])
    + annotate("text", x=[inc_lbl_pos, hatch_lbl_pos], y=11, label=["incubation", "hatch"])
    + scale_x_continuous(labels=label_x, limits=[xmin, xmax])).save("figs/Nest_IGLO.png", height=8, width=8, dpi=150)


#############
## BARROW ###
#############


res2 = res[res.site == "Barrow"]
barw_nest = pd.read_excel("/home/vin/Doctorat/data/datasheet/2018/BARW/BARW_incubation_hatch_dates_2018.xlsx", sheet_name=1)
barw_nest["julian"] = barw_nest.date.dt.dayofyear

inc_start = barw_nest[barw_nest.type == "incubation"].julian.min()
inc_end = barw_nest[barw_nest.type == "incubation"].julian.max()
inc_lbl_pos = inc_start + (inc_end - inc_start)/2
hatch_start = barw_nest[barw_nest.type == "hatch"].julian.min()
hatch_end = barw_nest[barw_nest.type == "hatch"].julian.max()
hatch_lbl_pos = hatch_start + (hatch_end - hatch_start)/2

xmin = min(inc_start, iglo.julian.min())
xmax = min(iglo_nest[iglo_nest.type == "hatch"].julian.max(), iglo.julian.max() + 2)

(ggplot(data=res2, mapping=aes(x='julian', y='ACI_mean', colour='site'))
 #+ facet_grid("panel~", scales="free")
 + xlab("Day")
 + ylab("Mean daily ACI (standardized)")
 + geom_point()
 + geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
 + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
 + annotate("rect", xmin=[inc_start, hatch_start], xmax=[inc_end, hatch_end],
            ymin=-math.inf, ymax=math.inf, alpha=0.1, fill=["red", "blue"])
 + annotate("text", x=[inc_lbl_pos, hatch_lbl_pos], y=4.5, label=["Incubation", "Hatch"])
 # + geom_line(data = inc, mapping=aes(x="julian", y="uniqueID"), colour="black")
 #    + geom_smooth(data=inc, mapping=aes(x="julian", y="uniqueID"), colour="black", method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
 + scale_x_continuous(labels=label_x, limits=[xmin, xmax])).save("figs/ACI_BARW_inc_hatch3.png", height=8, width=8, dpi=150)

inc = barw_nest.groupby("julian", as_index=False).uniqueID.count().reset_index()

(ggplot(data=inc, mapping=aes(x="julian", y="uniqueID"))
    + xlab("Day")
    + ylab("Number of nest initiation/hatch")
    + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
    + annotate("rect", xmin=[inc_start, hatch_start], xmax=[inc_end, hatch_end],
               ymin=-math.inf, ymax=math.inf, alpha=0.1, fill=["red", "blue"])
    + annotate("text", x=[inc_lbl_pos, hatch_lbl_pos], y=4.5, label=["incubation", "hatch"])
    + scale_x_continuous(labels=label_x, limits=[xmin, xmax])).save("figs/Nest_BARW.png", height=8, width=8, dpi=150)


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
    + scale_x_continuous(labels=label_x))  # .save("figs/ACI_EABA_mavg5.png", height=10, width=8, dpi=150)
