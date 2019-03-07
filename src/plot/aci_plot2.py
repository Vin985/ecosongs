
import datetime
import math

import numpy as np
import pandas as pd

import feather
from plotnine import (aes, annotate, facet_grid, geom_errorbar, geom_line,
                      geom_point, geom_rect, geom_smooth, ggplot,
                      scale_x_continuous, xlab, xlim, ylab, facet_wrap, scale_colour_manual)


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

# The palette with black:
cbbPalette = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#0072B2", "#D55E00", "#CC79A7"]

# site_data = pd.read_excel("/home/vin/Doctorat/data/datasheet/2018/sites_deployment_2018.xlsx")
site_data = pd.read_excel("C:\\UMoncton\\Doctorat\\data\\datasheet\\2018\\sites_deployment_2018.xlsx")

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

res["panel"] = 0
res.loc[res.site == "Barrow", "panel"] = 1
res.loc[res.site == "East Bay", "panel"] = 2
res.loc[res.site == "Igloolik", "panel"] = 3
res.loc[res.site == "Canning River", "panel"] = 4
res.loc[res.site == "Burntpoint Creek", "panel"] = 5
res.loc[res.site == "Svalbard", "panel"] = 6
print(res)

(ggplot(data=res, mapping=aes(x='julian', y='ACI_mean', colour='site'))
    + xlab("Day")
    + ylab("Mean daily ACI (standardized)")
    # + facet_grid("site~", scales="free")
	+ facet_wrap("panel", nrow=2, ncol=3)
    + geom_point()
    # + geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
    + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
	+ scale_colour_manual(values=cbbPalette, guide=False)
    + scale_x_continuous(labels=label_x)).save("figs/ACI_all_testfacet5.png", height=10, width=16, dpi=150)

	