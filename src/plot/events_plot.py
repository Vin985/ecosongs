import feather
import pandas as pd
from plotnine import (aes, annotate, facet_grid, facet_wrap, geom_errorbar,
                      geom_line, geom_point, geom_rect, geom_smooth, ggplot,
                      scale_colour_manual, scale_x_continuous, xlab, xlim,
                      ylab)

from .plot import Plot
from .utils import exclude_rows, join_tuple, label_x


class EventsPlot(Plot):

    def __init__(self, events=None, recordings=None, plot_data=None, opts=None):
        super().__init__(plot_data, opts)
        self.events = events
        self.recordings = recordings
        if not plot_data:
            if events and recordings:
                # create final data from events and recordings
                self.create_plot_data(events, recordings)
            else:
                raise AttributeError(('Either "plot_data" with all relevant information'
                                      ' for plotting, paths to files containing'
                                      ' events and recordings data'
                                      ' or dataframes with this information should be provided'))

    def create_plot_data(self, events, recordings):
        self.get_events()

    def get_data(self, name):
        data = getattr(self, name)
        if not isinstance(data, pd.DataFrame):
            if isinstance(data, str):
                # events is a path, load data file
                path = data
                setattr(self, name + "_path", path)
                setattr(self, name, feather.read_dataframe(path))
            else:
                print("Unsupported type provided for " + name)

    def get_events(self):
        # verify that events are correctly loaded
        self.get_data("events")
        self.get_data("recordings")

        events = self.aggregate_events()
        events = self.get_recordings_info(events)
        events = exclude_rows(events, self.opts)
        res = self.check_data_columns(events)
        print(res)
        self.plot_data = res

    def aggregate_events(self):
        # TODO change aggregation options
        if "agg_by" in self.opts:
            agg_by = self.opts["agg_by"]
        else:
            agg_by = "count"
        res = self.events.groupby(["recording_id"], as_index=False).agg({"event_id": agg_by})
        res.rename(columns={'event_id': 'n_events'}, inplace=True)
        return res

    def get_recordings_info(self, events):
        # TODO: externalize columns selection
        recs = self.recordings[["id", "date", "name", "site", "plot"]]
        res = events.merge(recs, left_on="recording_id", right_on="id")
        return res

    def check_data_columns(self, data):
        # if "duration" not in data:
        #     data["duration"] = data["end"] - data["start"]
        if "julian" not in data:
            data["julian"] = data["date"].dt.dayofyear
        if "hour" not in data:
            data["hour"] = data["date"].dt.hour
        data = data.sort_values(["site", "plot", "julian", "date"])
        if "julian_bounds" in self.opts:
            min_j, max_j = self.opts["julian_bounds"]
            data = data.loc[(data["julian"] > min_j) & (data["julian"] < max_j)]
        return data

    def aggregate_mean(self, data, column):
        data["type"] = column
        data.rename(columns={column: "value"}, inplace=True)
        res = data.groupby(["site", "julian", "type"], as_index=False).agg({"value": "mean"})
        # res.columns = pd.Index(join_tuple(i, "_") for i in res.columns)
        return res

    def plot(self):
        # cbbPalette = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#0072B2", "#D55E00", "#CC79A7"]
        res = self.aggregate_mean(self.plot_data, "n_events")
        self.plt = ggplot(data=res, mapping=aes(x='julian', y='value', colour='site'))
        self.plt += xlab("Day")
        self.plt += ylab("Mean number of detected songs")
        # + facet_grid("site~", scales="free")
        # + geom_line()
        self.plt += facet_wrap("site", nrow=6, ncol=3, scales="free_y")
        self.plt += geom_point()
        # + geom_errorbar(aes(ymin="ACI_mean - ACI_std", ymax="ACI_mean + ACI_std"))
        self.plt += geom_smooth(method="mavg", se=False,
                                method_args={"window": 4, "center": True, "min_periods": 1})
        # + scale_colour_manual(values=cbbPalette, guide=False)
        self.plt += scale_x_continuous(labels=label_x)

        self.plt.save("plot/figs/TEST_SECLASS.png", height=10, width=16, dpi=150)
