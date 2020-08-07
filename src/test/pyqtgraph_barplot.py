#%%

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pandas as pd

from pyqtextra.pyqtgraph.RotateAxisItem import RotateAxisItem


# raw_matches = pd.read_csv("src/test/db/matches.csv")
raw_matches = pd.read_csv("db/matches.csv")
raw_matches = raw_matches.astype({"tag": "category"})

matches2 = raw_matches.drop_duplicates("tag_id").copy()
matches2["matched"] = "not matched"
matches2.loc[matches2.event_id > -1, "matched"] = "matched"

count_long = (
    matches2.groupby(["matched", "tag"])
    .agg({"tag": "count"})
    .rename(columns={"tag": "n_tags"})
    .reset_index()
    .astype({"matched": "category", "tag": "category"})
)


#%%
types = count_long.matched.cat.categories
x = np.arange(len(count_long.tag.cat.categories))
colors = ["r", "b"]

nbars = len(types)


bar_width = 0.8 / nbars
bg = {}
start_pos = 1 - (bar_width * nbars / 2)
for i in range(0, len(types)):
    x0 = x + start_pos + i * bar_width
    y = count_long.loc[count_long.matched == types[i], "n_tags"]
    bg[types[i]] = pg.BarGraphItem(
        x0=x0, height=y, width=bar_width, brush=colors[i], name=types[i]
    )

print(bg)

#%%
pg.setConfigOptions(foreground="#000000", background="w")
plt = pg.plot()
plt.addLegend()
plt.setWindowTitle("pyqtgraph example: BarGraphItem")
for item in bg.values():
    plt.addItem(item)

# axis = RotateAxisItem("bottom").setTicks(
#     [list(enumerate(count_long.tag.cat.categories, 1))]
# )

axis = RotateAxisItem("bottom", angle=-90)
axis.setTicks([list(enumerate(count_long.tag.cat.categories, 1))])
plt.setAxisItems({"bottom": axis})

# win.addItem(axis)


# Final example shows how to handle mouse clicks:
class BarGraph(pg.BarGraphItem):
    def mouseClickEvent(self, event):
        print("clicked")


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == "__main__":
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        QtGui.QApplication.instance().exec_()
