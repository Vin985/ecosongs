import datetime

import feather
from plotnine import (aes, facet_grid, geom_point, geom_smooth, ggplot,
                      scale_x_continuous)


def label_x(dates):
    res = [(datetime.datetime(2018, 1, 1) + datetime.timedelta(x)).strftime("%d-%m") for x in dates]
    print(res)
    return res


recordings = feather.read_dataframe("Recordings.feather")
recordings["julian"] = recordings["date"].dt.dayofyear

(ggplot(data=recordings, mapping=aes(x='julian', y='plot', colour='plot'))
    + geom_point()
    + scale_x_continuous(labels=label_x))  # .save("ACI_all_noise.png", height=10, width=8, dpi=150)
