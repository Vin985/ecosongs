
import datetime

import feather
from plotnine import (aes, facet_grid, geom_line, geom_smooth, ggplot,
                      scale_x_continuous)

sites = ["Igloolik", "East Bay", "Barrow", "Burntpoint Creek", "Canning River", "Svalbard"]

# aci = feather.read_dataframe("src/plots/ACI.feather")
aci = feather.read_dataframe("ACI.feather")
aci["julian"] = aci["date"].dt.dayofyear
aci["hour"] = aci["date"].dt.hour
aci = aci.sort_values(["site", "plot", "julian", "date"])
aci = aci.loc[(aci["julian"] > 155) & (aci["julian"] < 220)]
aci = aci.loc[(aci["ACI"] < 50000)]
res = aci.loc[aci["denoised"] == False]
res = res.groupby(["site", "julian"]).mean()
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
    # + geom_line()
    + geom_smooth(method="mavg", method_args={"window": 5})
    + scale_x_continuous(labels=label_x)).save("figs/ACI_all_noise_mavg.png", height=10, width=8, dpi=150)

# Test sans bruit
aci2 = aci.loc[aci["site"] == "East Bay"]
res2 = aci2.groupby(["denoised", "julian"]).mean()
res2 = res2.reset_index()
# res2 = aci2

(ggplot(data=res2, mapping=aes(x='julian', y='ACI', colour='denoised'))
    + facet_grid("denoised~", scales="free")
    # + geom_line()
    + geom_smooth(method="mavg", method_args={"window": 5})
    + scale_x_continuous(labels=label_x))  # .save("figs/ACI_EABA_mavg5.png", height=10, width=8, dpi=150)
