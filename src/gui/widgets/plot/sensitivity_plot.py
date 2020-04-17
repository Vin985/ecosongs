from PySide2.QtCore import Slot, qApp
from PySide2.QtWidgets import QApplication, QWidget

import pyqtgraph as pg
import pandas as pd

from gui.widgets.plot.ui.sensitivity_plot_ui import Ui_SensitivityPlot


class SensitivityPlot(QWidget, Ui_SensitivityPlot):
    def __init__(self):
        super().__init__()
        self.data = None
        self.setupUi(self)
        self.link_events()

    # Define callbacks when events happen
    def link_events(self):
        self.btn_plot.clicked.connect(self.plot)

    def plot(self):
        self.load_data()
        if self.data is not None:
            plt = self.plot_layout.addPlot()
            self.data.min_activity = pd.to_numeric(self.data.min_activity)
            points = pg.ScatterPlotItem(
                x=self.data.min_activity, y=self.data.precision)

            points.sigClicked.connect(self.click)
            plt.addItem(points)

    def click(self, points):
        print(points)

    def load_data(self):
        audio_folder = "/mnt/win/UMoncton/OneDrive - Université de Moncton/Data/Reference/split"

        options_table = qApp.tables.analysis_options
        detector_data_table = qApp.tables.detector_statistics

        options_df = options_table.get_rows_by_column(
            "analysis_type", ["detector_sensitivity"])
        options_df = options_table.expand_options(options_df)
        options_df = options_df.loc[options_df["audio_path"] == audio_folder]
        print(options_df)

        data = options_df.merge(detector_data_table.df,
                                left_on="id", right_on="analysis_options")
        self.data = data.drop_duplicates()
