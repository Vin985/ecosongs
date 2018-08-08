from db.models import RecordingModel
from gui.widgets.dbmanager.ui.fileimport_ui import Ui_FileImport
from PySide2.QtWidgets import QWidget


class FileImport(QWidget, Ui_FileImport):
    def __init__(self, recordings=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
