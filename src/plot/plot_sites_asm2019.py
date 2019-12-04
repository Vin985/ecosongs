import inspect
import os

import pandas as pd
from plotnine import element_text, ggtitle, theme

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
print(currentdir)
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
try:
    from plot.events_plot import EventsPlot
except Exception:
    print("Woops, module EventsPlot not found")


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
                         "save": save,
                         "facet_scales": "fixed",
                         "facet_nrow": 2,
                         "smoothed": True})

    plt.plot()
    print(plt.plot_data)

    # plt2 = plt.plot()
    # plt2 += theme(legend_position="none",
    #               text=element_text(size=12),
    #               axis_title=element_text(size=14, weight="bold"),
    #               strip_text=element_text(weight="bold"),
    #               plot_title=element_text(linespacing=1.5, size=14, weight="bold", va="center", ha="center", margin={'t': 100, 'b': 15}))
    # plt2 += ggtitle('Mean number and moving average (window =4) of detected bird songs by day and site')
    # plt2.save(**save)

    # plt.plots_by_site(filename="plot/figs/All_sites_by_plot_wac.pdf")
