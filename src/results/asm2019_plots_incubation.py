import datetime
import inspect
import math
import os

import feather
import pandas as pd
from plotnine import (aes, annotate, facet_grid, facet_wrap, geom_errorbar,
                      geom_line, geom_point, geom_rect, geom_smooth, ggplot,
                      save_as_pdf_pages, scale_colour_manual,
                      scale_x_continuous, theme, theme_classic, xlab, xlim,
                      ylab, ylim)
from plotnine.facets.facet_wrap import n2mfrow

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
print(currentdir)
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
try:
    from plot.events_plot import EventsPlot
except Exception:
    print("Woops, module EventsPlot not found")


def label_x(dates):
    res = [(datetime.datetime(2018, 1, 1) + datetime.timedelta(x)
            ).strftime("%d-%m") for x in dates]
    print(res)
    return res


if __name__ == "__main__":

    # subset = {"exclude": {"site": ["Cape Churchill", "Coats Island",
    #                                "Hochstetter", "Colville River Delta"],
    #                       "plot": ["SDHC_1", "SDHC_1 2"]}}
    subset = {"include": {"site": ["Igloolik", "East Bay", "Barrow", "Burntpoint Creek", "Canning River", "Svalbard"]},
              "exclude": {"plot": "BARW_8"}}

    save = {"path": "../plot/figs",
            "height": 10,
            "width": 16,
            "dpi": 150,
            "filename": "asm2019_songevents_compare.png"}

    site_data = pd.read_excel(
        "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/sites_deployment_2018.xlsx")

    plt = EventsPlot(events="../plot/data/song_events_mac2.feather",
                     recordings="../plot/data/recordings_mac.feather",
                     deployment_data=site_data,
                     opts={  # "julian_bounds": (164, 220),
                         "subset": subset,
                         # "save": save,
                         "facet_scales": "fixed",
                         "facet_nrow": 2,
                         "smoothed": True})


plt.create_plot_data()


def create_file_name(type, site, prefix, suffix):
    return "_".join(filter(None, [prefix, type, site, suffix]))


def incubation_plot(data, site, nest_data_path, save=True, ext=".png", prefix="", suffix=""):
    df = data.loc[data.site == site]

    df_nest = pd.read_excel(nest_data_path)
    df_nest["julian"] = df_nest.date.dt.dayofyear
    df_nest.loc[df_nest.type == "incubation", "julian"]

    inc_start = df_nest[df_nest.type == "incubation"].julian.min()
    inc_end = df_nest[df_nest.type == "incubation"].julian.max()
    inc_lbl_pos = inc_start + (inc_end - inc_start) / 2
    hatch_start = df_nest[df_nest.type == "hatch"].julian.min()
    hatch_end = min(df_nest[df_nest.type ==
                            "hatch"].julian.max(), df.julian.max() + 2)
    hatch_lbl_pos = hatch_start + (hatch_end - hatch_start) / 2

    xmin = min(inc_start, df.julian.min())
    xmax = min(df_nest[df_nest.type == "hatch"].julian.max(),
               df.julian.max() + 2)

    yrange = (df.value.max() - df.value.min())
    bufmin = .1 * yrange
    bufmax = .15 * yrange
    ymin = df.value.min() - bufmin
    ymax = df.value.max() + bufmax

    se_plot = (ggplot(data=df, mapping=aes(x='julian', y='value', colour='site'))
               + xlab("Day")
               + ylab("Mean daily events detected")
               + geom_point()
               + theme_classic()
               + theme(legend_position="none")
               + geom_smooth(method="mavg", se=False,
                             method_args={"window": 4, "center": True, "min_periods": 1})
               + annotate("rect", xmin=[inc_start, hatch_start], xmax=[inc_end, hatch_end],
                          ymin=-math.inf, ymax=math.inf, alpha=0.1, fill=["red", "blue"])
               + annotate("text", x=[inc_lbl_pos, hatch_lbl_pos],
                          y=df.value.max() + .1 * yrange, label=["Incubation initiation", "Hatching"])
               + scale_x_continuous(labels=label_x, limits=[xmin, xmax])
               + ylim(ymin, ymax))

    df_inc = df_nest.groupby(
        ["julian", "type"], as_index=False).uniqueID.count().reset_index().copy()
    inc_plot = (ggplot(data=df_inc, mapping=aes(x="julian", y="uniqueID"))
                + xlab("Day")
                + ylab("Number of nest initiation/hatch")
                + theme_classic()
                # + geom_line()
                + geom_smooth(data=df_inc.loc[df_inc["type"] == "incubation"], linetype="dashed",
                              method="mavg", se=False,
                              method_args={"window": 4, "center": True, "min_periods": 1})
                + geom_smooth(data=df_inc.loc[df_inc["type"] == "hatch"], linetype="dotted",
                              method="mavg", se=False,
                              method_args={"window": 4, "center": True, "min_periods": 1})
                + scale_x_continuous(labels=label_x, limits=[xmin, xmax]))

    if save:
        se_name = create_file_name("sound_events", site, prefix, suffix)
        se_plot.save("figs/" + se_name + ".png", height=8, width=8, dpi=150)
        inc_name = create_file_name("incubation", site, prefix, suffix)
        inc_plot.save("figs/" + inc_name + ".png", height=8, width=8, dpi=150)
    return (se_plot, inc_plot)


(iglo_se, iglo_inc) = incubation_plot(plt.plot_data, "Igloolik",
                                      "/home/vin/Doctorat/data/datasheet/2018/IGLO/IGLO_nest_2018.xlsx",
                                      # save=False,
                                      prefix="asm2019")
(barw_se, barw_inc) = incubation_plot(plt.plot_data, "Barrow",
                                      "/home/vin/Doctorat/data/datasheet/2018/BARW/BARW_nest_2018.xlsx",
                                      # save=False,
                                      prefix="asm2019")


def join_tuple(tuple, sep):
    tuple = list(filter(None, tuple))
    if len(tuple) > 1:
        return sep.join(tuple)
    return tuple[0]


def check_dates(df, site_data):
    plot = site_data.loc[site_data["plot"] == df.name]
    res = df.copy()
    # res.reset_index()
    if not plot.empty:
        start = plot.depl_start.iloc[0]
        end = plot.depl_end.iloc[0]
        if not pd.isnull(start):
            res = res.loc[(df["date"] > start) & (df["date"] < end)]
        res["lat"] = plot.lat.iloc[0]
        res["lon"] = plot.lon.iloc[0]
    # res.ACI = (res.ACI - res.ACI.mean()) / res.ACI.std()
    return res


sites = ["Igloolik", "East Bay", "Barrow",
         "Burntpoint Creek", "Canning River", "Svalbard"]
plot_excl = ["BARW_8"]

# The palette with black:
cbbPalette = ["#000000", "#E69F00", "#56B4E9",
              "#009E73", "#0072B2", "#D55E00", "#CC79A7"]

site_data = pd.read_excel(
    "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/sites_deployment_2018.xlsx")
# site_data = pd.read_excel(
#     "C:\\UMoncton\\Doctorat\\data\\datasheet\\2018\\sites_deployment_2018.xlsx")

# aci = feather.read_dataframe("src/plots/ACI.feather")
aci = feather.read_dataframe("data/ACI.feather")
print(aci)
# aci.date = aci.date.dt.tz_localize("UTC")
aci = aci.loc[aci.site.isin(sites)]
aci = aci.loc[~aci["plot"].isin(plot_excl)]
aci["julian"] = aci["date"].dt.dayofyear
aci["hour"] = aci["date"].dt.hour
aci = aci.sort_values(["site", "plot", "julian", "date"])
aci = aci.loc[(aci["julian"] > 155) & (aci["julian"] < 220)]
aci = aci.loc[(aci["ACI"] < 50000)]
aci = aci.loc[aci["denoised"] == False]

print(aci.loc[aci["plot"] == "EABA_1"])
aci = aci.reset_index()
res = aci.groupby(["plot"], as_index=False).apply(check_dates, site_data)
print(res)
res.index = res.index.droplevel()
print(res)
res = res.groupby(["site", "julian"], as_index=False).agg(
    {"ACI": ["mean", "std"]})
res.columns = pd.Index(join_tuple(i, "_") for i in res.columns)
res

# plt.plot()
# print(plt.plot_data)
#
# # plt2 = plt.plot()
# # plt2 += theme(legend_position="none",
# #               text=element_text(size=12),
# #               axis_title=element_text(size=14, weight="bold"),
# #               strip_text=element_text(weight="bold"),
# #               plot_title=element_text(linespacing=1.5, size=14, weight="bold", va="center", ha="center", margin={'t': 100, 'b': 15}))
# # plt2 += ggtitle('Mean number and moving average (window =4) of detected bird songs by day and site')
# # plt2.save(**save)
#
# # plt.plots_by_site(filename="plot/figs/All_sites_by_plot_wac.pdf")
