import pandas as pd
from plotnine import element_text, ggtitle, theme

from plot.events_plot import EventsPlot

if __name__ == "__main__":

    # subset = {"exclude": {"site": ["Cape Churchill", "Coats Island",
    #                                "Hochstetter", "Colville River Delta"],
    #                       "plot": ["SDHC_1", "SDHC_1 2"]}}
    subset = {"include": {"plot": ["IGLO_ARCH1", "IGLO_ARCH2", "IGLO_ARCH3",
                                   "IGLO_ARCH4", "IGLO_ARCH5", "IGLO_ARCH6", "IGLO_ARCH7", "IGLO_ARCH8"]}}

    save = {"path": "plot/figs",
            "height": 15,
            "width": 18,
            "dpi": 150,
            "filename": "test/test_wac2.png"}

    site_data = pd.read_excel(
        "/mnt/win/UMoncton/OneDrive - Université de Moncton/Ressources Audiomoth/sites_deployment_2018.xlsx")

    plt = EventsPlot(events="db/feather/song_events.feather",
                     recordings="db/feather/recordings.feather",
                     deployment_data=site_data,
                     opts={  # "julian_bounds": (164, 220),
                         "subset": subset,
                         # "save": save,
                         "facet_scales": "fixed",
                         "smoothed": True})

    # plt2 = plt.plot()
    # plt2 += theme(legend_position="none",
    #               text=element_text(size=12),
    #               axis_title=element_text(size=14, weight="bold"),
    #               strip_text=element_text(weight="bold"),
    #               plot_title=element_text(linespacing=1.5, size=14, weight="bold", va="center", ha="center", margin={'t': 100, 'b': 15}))
    # plt2 += ggtitle('Mean number and moving average (window =4) of detected bird songs by day and site')
    # plt2.save(**save)

    plt.plots_by_site(filename="plot/figs/All_sites_by_plot_wac.pdf")
