from gui.widgets.common.page_widget import PageWidget

from gui.widgets.analysis.ui.analysis_ui import Ui_Analysis
import resource


class Analysis(PageWidget, Ui_Analysis):
    def __init__(self):
        print('analysis1: Memory usage: %s (kb)' %
              resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        super().__init__()
        self.setupUi(self)
        print('analysis2: Memory usage: %s (kb)' %
              resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        self.link_events()

    # Define callbacks when events happen
    def link_events(self):
        # Link menu actions
        pass
