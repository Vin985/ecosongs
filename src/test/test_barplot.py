#%%

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.graphicsItems.AxisItem import AxisItem
import numpy as np
import pandas as pd
import math


class RotateAxisItem(AxisItem):
    def __init__(self, *args, angle=90, **kwargs):
        print("init rotate")
        super().__init__(*args, **kwargs)
        self._angle = angle
        self._height_updated = False

    def drawPicture(self, p, axisSpec, tickSpecs, textSpecs):

        p.setRenderHint(p.Antialiasing, False)
        p.setRenderHint(p.TextAntialiasing, True)

        ## draw long line along axis
        pen, p1, p2 = axisSpec
        p.setPen(pen)
        p.drawLine(p1, p2)
        p.translate(0.5, 0)  ## resolves some damn pixel ambiguity

        ## draw ticks
        for pen, p1, p2 in tickSpecs:
            p.setPen(pen)
            p.drawLine(p1, p2)

        # Draw all text
        if self.style["tickFont"] is not None:
            p.setFont(self.style["tickFont"])
        p.setPen(self.textPen())
        max_width = 0

        for rect, flags, text in textSpecs:
            p.save()  # save the painter state

            p.translate(rect.center())  # move coordinate system to center of text rect
            p.rotate(self._angle)  # rotate text
            p.translate(-rect.center())  # revert coordinate system

            x_offset = math.ceil(
                math.fabs(math.sin(math.radians(self._angle)) * rect.width())
            )
            if self._angle < 0:
                x_offset = -x_offset
            p.translate(
                x_offset / 2, 0
            )  # Move the coordinate system (relatively) downwards

            p.drawText(rect, flags, text)
            p.restore()  # restore the painter state
            offset = math.fabs(x_offset)
            max_width = offset if max_width < offset else max_width

        #  Adjust the height
        if not self._height_updated:
            self.setHeight(self.height() + max_width + 50)
            self._height_updated = True


raw_matches = pd.read_csv("src/test/db/matches.csv")
# raw_matches = pd.read_csv("db/matches.csv")
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
