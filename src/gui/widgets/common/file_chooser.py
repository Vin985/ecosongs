
# import sys
# from PySide2.QtWidgets import QApplication

import os

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QFileDialog, QWidget

from gui.widgets.common.ui.file_chooser_ui import Ui_FileChooser

#from ui.file_chooser_ui import Ui_FileChooser


class FileChooser(QWidget, Ui_FileChooser):

    text_changed = Signal(str)

    def __init__(self, options=None, parent=None):
        super().__init__(parent=parent)
        self.options = options or {}
        self.setupUi(self)
        self.link_events()

    def link_events(self):
        self.btn_browse.clicked.connect(self.browse)
        self.input_path.textChanged.connect(self.text_changed.emit)

    def init_display(self):
        self.input_path.setText(self.options.get("default", ""))

    def browse(self):
        file_type = self.options["file_type"]
        if not file_type:
            raise AttributeError("No type of dialog type defined. Please add the 'file_type' option"
                                 "to the FileChooser class.")
        text = getattr(self, "choose_" + file_type)()
        # Update gui input
        if text:
            self.input_path.setText(text)

    def choose_folder(self):
        default = self.input_path.text() or os.getcwd()
        text = QFileDialog.getExistingDirectory(self, "Choose directory",
                                                default)
        return text

    def choose_files(self):
        default = self.input_path.text() or os.getcwd()
        file_filter = self.options.get("file_filter", "")
        (files, _) = QFileDialog.getOpenFileNames(
            self, "Choose files", default, file_filter)
        text = "; ".join(files)
        return text

    def choose_file(self):
        default = self.input_path.text() or os.getcwd()
        file_filter = self.options.get("file_filter", "")
        (file_name, _) = QFileDialog.getOpenFileName(
            self, "Choose file", default, file_filter)
        return file_name

    def choose_save_file(self):
        default = self.input_path.text() or os.getcwd()
        file_filter = self.options.get("file_filter", "")
        (text, _) = QFileDialog.getSaveFileName(
            self, "Choose file", default, file_filter)
        return text


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     options = {"file_type": "save_file",
#                "default": "/mnt/win/UMoncton/Doctorat/dev/ecosongs/src/gui/widgets/common/file_chooser.py"}
#     fc = FileChooser(options=options)
#     fc.show()
#     app.exec_()
