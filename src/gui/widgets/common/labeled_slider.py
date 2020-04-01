
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import Signal, Slot

from gui.widgets.common.ui.labeled_slider_ui import Ui_LabeledSlider
import sys


class LabeledSlider(QWidget, Ui_LabeledSlider):

    value_changed = Signal(int)

    def __init__(self, parent=None, text_pos="right", text_align="center", multiplier=1, unit=""):
        super().__init__(parent=parent)
        self.setupUi(self, text_pos=text_pos)
        self.link_events()
        self._multiplier = multiplier
        self._unit = unit
        self.update_value()

    def link_events(self):
        self.slider.sliderMoved.connect(self.update_value)
        self.slider.valueChanged.connect(self.update_value)

    def display_value(self):
        return round(self.slider.value() * self.multiplier, 2)

    def value(self):
        return self.slider.value()

    @property
    def multiplier(self):
        return self._multiplier

    @multiplier.setter
    def multiplier(self, value):
        self._multiplier = value
        self.update_value()

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
        self.update_value()

    @Slot()
    def update_value(self, value=None):
        text = str(self.display_value())
        if self.unit:
            text += " " + self.unit
        self.lbl_value.setText(text)
        self.value_changed.emit(value)

    def setOrientation(self, value):
        self.slider.setOrientation(value)

    def setMaximum(self, value):
        self.slider.setMaximum(value)

    def setMinimum(self, value):
        self.slider.setMinimum(value)

    def setSingleStep(self, value):
        self.slider.setSingleStep(value)

    def setValue(self, value):
        self.slider.setValue(value)

    def setSliderPosition(self, value):
        self.slider.setSliderPosition(value)

    def maximum(self):
        return self.slider.maximum()

    def minimum(self):
        return self.slider.minimum()

    def pageStep(self):
        return self.slider.pageStep()

    def singleStep(self):
        return self.slider.singleStep()

    def setPageStep(self, value):
        self.slider.setPageStep(value)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    rs = LabeledSlider(text_pos="top", multiplier=1)
    rs.show()
    app.exec_()
