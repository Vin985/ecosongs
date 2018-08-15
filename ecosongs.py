#!/usr/bin/env python


from gui.ecosongs_ui import Ui_Ecosongs
from PySide2.QtCore import Slot
#from PySide2.QtCore import QFile, QTextStream
from PySide2.QtWidgets import QApplication, QMainWindow


class Ecosongs(QMainWindow, Ui_Ecosongs):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.loadConfig()
        self.linkEvents()

    def loadConfig(self):
        pass

    # Define callbacks when events happen
    def linkEvents(self):
        # Link menu actions
        self.linkActions()

        # Navigation: change page when icon is clicked
        self.sidebar.currentRowChanged.connect(self.pages.setCurrentIndex)

    def linkActions(self):
        self.aExit.triggered.connect(self.exit)

    def initProgressBar(self, maxValue):
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximum(maxValue)
        #self.progressBar.setValue(0)

    @Slot()
    def exit(self):
        QApplication.quit()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # f = QFile("gui/resources/qss/custom.qss")
    # f.open(QFile.ReadOnly)
    # res = QTextStream(f).readAll()
    # print(res)
    # app.setStyleSheet(res)
    ui = Ecosongs()  # We set the form to be our ExampleApp (design)
    ui.showMaximized()
    sys.exit(app.exec_())
