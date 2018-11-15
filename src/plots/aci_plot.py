
import datetime

import numpy as np
import pandas as pd

import feather
from plotnine import (aes, facet_grid, geom_line, geom_smooth, ggplot,
                      scale_x_continuous)

sites = ["Igloolik", "East Bay", "Barrow", "Burntpoint Creek", "Canning River", "Svalbard"]

site_data = pd.read_excel("/home/vin/Doctorat/data/datasheet/2018/sites_deployment_2018.xlsx")

site_data

# aci = feather.read_dataframe("src/plots/ACI.feather")
aci = feather.read_dataframe("ACI.feather")
aci = aci.loc[aci.site.isin(sites)]
aci["julian"] = aci["date"].dt.dayofyear
aci["hour"] = aci["date"].dt.hour
aci = aci.sort_values(["site", "plot", "julian", "date"])
aci = aci.loc[(aci["julian"] > 155) & (aci["julian"] < 220)]
aci = aci.loc[(aci["ACI"] < 50000)]
res = aci.loc[aci["denoised"] == False]


def check_dates(df, site_data):
    plot = site_data.loc[site_data["plot"] == df.name]
    res = df
    if not plot.empty:
        start = plot.depl_start.iloc[0]
        end = plot.depl_end.iloc[0]
        if not pd.isnull(start):
            res = df.loc[(df["date"] > start) & (df["date"] < end)]
    res.ACI = (res.ACI - res.ACI.mean()) / res.ACI.std()
    return res


res = res.groupby(["plot"]).apply(check_dates, site_data)
res

res = res.groupby(["site", "julian"]).ACI.mean()
res = res.reset_index()
res
# print(aci.loc[aci["site"] == "Igloolik"])
# print(aci)


def label_x(dates):
    res = [(datetime.datetime(2018, 1, 1) + datetime.timedelta(x)).strftime("%d-%m") for x in dates]
    print(res)
    return res


(ggplot(data=res, mapping=aes(x='julian', y='ACI', colour='site'))
    + facet_grid("site~", scales="free")
    + geom_line()
    + geom_smooth(method="mavg", se=False, method_args={"window": 4, "center": True, "min_periods": 1})
    + scale_x_continuous(labels=label_x))  # .save("figs/ACI_all_noise_mavg.png", height=10, width=8, dpi=150)

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
