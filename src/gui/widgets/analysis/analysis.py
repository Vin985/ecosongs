from gui.widgets.common.page_widget import PageWidget

from gui.widgets.analysis.ui.analysis_ui import Ui_Analysis
import resource


class Analysis(PageWidget, Ui_Analysis):
    def __init__(self):
        super().__init__()
        self.opts = None
        self.setupUi(self)
        self.link_events()

    # Define callbacks when events happen
    def link_events(self):
        # Link menu actions
        self.analysis_tabs.currentChanged.connect(self.change_tab)

    def change_tab(self, index):
        tab = self.analysis_tabs.widget(index)
        tab.enter_tab(self.opts)

    def enter_page(self, opts):
        self.opts = opts
        tab = self.analysis_tabs.currentWidget()
        tab.enter_tab(self.opts)
