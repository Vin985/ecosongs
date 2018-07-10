#!/usr/bin/env python


from gui.EcosongsUI import Ui_Ecosongs
from PySide2.QtWidgets import QApplication, QMainWindow

FILE_EXT = ".wac"
DEST_DIR = "wav"


class Ecosongs(QMainWindow, Ui_Ecosongs):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.linkEvents()

    # Define callbacks when events happen
    def linkEvents(self):
        pass
        # Button pushed
        #self.srcBrowseBtn.clicked.connect(self.browseSrc)
        #self.convertBtn.clicked.connect(self.convert)

        # ComboBox
        #self.srcPathInput.textChanged.connect(self.setRoot)
        #self.destPathInput.textChanged.connect(self.setDest)
        # Checkbox
        #self.isFolder.toggled.connect(self.folder_opt)
        #Thread
        #self.wacConverter.started.connect(self.start_thread)
        #self.wacConverter.converting.connect(self.log)

    def initProgressBar(self, maxValue):
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximum(maxValue)
        #self.progressBar.setValue(0)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    ui = Ecosongs()  # We set the form to be our ExampleApp (design)
    ui.show()
    sys.exit(app.exec_())
