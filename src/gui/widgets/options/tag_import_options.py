
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QRegExpValidator, QValidator
from PySide2.QtCore import QRegExp

from gui.widgets.options.ui.tag_import_options_ui import \
    Ui_TagImportOptions


class TagImportOptions(QWidget, Ui_TagImportOptions):

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.link_events()

    def init_ui(self):
        # TODO: load from config file
        extensions_rx = QRegExp("(\\.\\w+)(;\\s*\\.\\w+)*")
        self.extensions_validator = QRegExpValidator(extensions_rx)
        # self.input_extensions.setValidator(extensions_validator)

    def link_events(self):
        self.input_extensions.textChanged.connect(self.validate_entry)

    def validate_entry(self, text):
        state, _, _ = self.extensions_validator.validate(text, 0)
        if state == QValidator.State.Intermediate:
            self.input_extensions.setStyleSheet(
                "QLineEdit { background: rgb(255, 229, 204)}")
        elif state == QValidator.State.Invalid:
            self.input_extensions.setStyleSheet(
                "QLineEdit { background: rgb(255, 153, 153)}")
        else:
            self.input_extensions.setStyleSheet("")

    def get_options(self):
        import_options = {"label_folder": self.input_tag_folder.text(),
                          "suffix": self.input_suffix.text(),
                          "extensions": self.input_extensions.text().split(";")}

        opts = {"task_options": import_options,
                "save": self.checkbox_save.isChecked(),
                "overwrite": self.checkbox_overwrite.isChecked()}
        return opts
