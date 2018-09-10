import os

from utils.filemanager import FileManager

from gui.threads.FileHandler import FileHandler
from gui.utils.dataframeTableModel import DataFrameTableModel
from gui.utils.settings import Settings
from gui.widgets.dbmanager.ui.fileimport_ui import Ui_FileImport
from PySide2.QtCore import (QObject, QSortFilterProxyModel, QThread, Signal,
                            Slot)
from PySide2.QtGui import qApp
from PySide2.QtWidgets import QFileDialog, QMessageBox, QWizard

# TODO: put files in config

DEST_DIR = "wav"


class QFileManager(QObject, FileManager):
    logging = Signal(str, bool)
    filesLoaded = Signal()

    def __init__(self):
        QObject.__init__(self)
        settings = Settings()
        FileManager.__init__(self, sites=settings.sites_path)

    def log(self, text):
        self.logging.emit(text, False)

    def files_loaded(self):
        # TODO: change to use persistence model
        # qApp.save_data("recordings", self.file_infos, format="t")
        self.filesLoaded.emit()


class FileImport(QWizard, Ui_FileImport):

    def __init__(self):
        super(self.__class__, self).__init__()
        # Initialize UI
        self.setupUi(self)
        self.init_ui()
        self.file_manager = QFileManager()
        self.thread = QThread()
        self.file_handler = FileHandler()
        self.registerFields()
        self.linkEvents()

    def init_ui(self):
        self.site_manual.setVisible(not self.radio_site_auto.isChecked())
        self.checkbox_done.setVisible(False)

    def registerFields(self):
        self.page1.registerField("src_path*", self.input_src_path)
        self.page5.registerField("done*", self.checkbox_done)

    # Define callbacks when events happen
    def linkEvents(self):
        # Buttons
        self.btn_browse_src.clicked.connect(self.browse_src)
        #self.btn_start_import.clicked.connect(self.import_files)
        # self.btn_browse_dest.clicked.connect(self.browse_dest)
        # self.btn_import.clicked.connect(self.import_files)
        # self.btn_cancel.clicked.connect(self.wacConverter.requestInterruption)
        # Input fields
        # self.input_src_path.textChanged.connect(self.set_root)
        # self.input_dest_path.textChanged.connect(self.set_dest)
        # Radio
        self.radio_is_folder.buttonToggled.connect(self.folder_options)
        self.radio_site_info.buttonToggled.connect(self.site_info_options)
        # Checkbox
        self.checkbox_subfolders.toggled.connect(self.subfolders_options)
        self.checkbox_move.toggled.connect(self.display_move_options)
        # File manager
        self.file_manager.logging.connect(self.log)
        self.file_manager.filesLoaded.connect(self.show_files)
        # Wac conversion
        self.thread.started.connect(self.thread_started)
        # self.thread.finished.connect(self.thread_finished)
        self.file_handler.logging.connect(self.log)
        self.file_handler.update_progress.connect(self.update_progress)
        # self.file_handler.finished.connect(self.end_conversion)

    def display_move_options(self):
        self.move_options.setVisible(self.checkbox_move.isChecked())

    def initializePage(self, id):
        getattr(self, "initialize_page" + str(id), lambda: None)()

    # TODO : Validate manual entries

    def initialize_page1(self):
        site_info = {}
        # get information about site from comboboxes
        if (self.radio_site_auto.isChecked()):
            for i in range(1, 4):
                tmp = getattr(self, "combo_idx_" + str(i)).currentText().lower()
                site_info[tmp] = i
        else:
            site_info["site"] = self.input_site
            site_info["year"] = self.input_year
            site_info["plot"] = self.input_plot

        self.file_manager.options = {"folder": self.radio_folder.isChecked(),
                                     "recursive": self.checkbox_subfolders.isChecked(),
                                     "recorder": self.radio_recorders.button(self.radio_recorders.checkedId()).text(),
                                     "folder_hierarchy": self.radio_site_auto.isChecked(),
                                     "site_info": site_info}
        self.file_manager.get_files()

    def initialize_page2(self):
        self.move_options.setVisible(self.checkbox_move.isChecked())
        # TODO : add compression options
        self.compression_options.setEnabled(False)

    def initialize_page3(self):
        df = self.file_manager.file_infos
        self.to_wav = df.loc[df.ext == "wac", 'path'].tolist()
        if self.to_wav:
            print(self.to_wav)

    def initialize_page4(self):
        # Convert files to wac
        self.file_handler.set_args(root=self.input_src_path.text(), dest="",
                                   files=self.to_wav)
        self.file_handler.moveToThread(self.thread)
        self.thread.start()

    # Called when any radio button for folder or file is selected

    def folder_options(self):
        # Only enable subfolder option if import folder is selected
        self.checkbox_subfolders.setEnabled(self.radio_folder.isChecked())
        # If import files
        if self.radio_file.isChecked():
            # Allow user to enter site info manually
            self.radio_site_manual.setEnabled(True)
            # else if subfolders are checked
        elif self.checkbox_subfolders.isChecked():
            # Disable manual info and force automatic detection
            # This is because multiple site can be imported
            self.radio_site_manual.setEnabled(False)
            self.radio_site_auto.setChecked(True)
            self.site_auto.setVisible(True)
            self.site_manual.setVisible(False)

    def site_info_options(self):
        self.site_auto.setVisible(self.radio_site_auto.isChecked())
        self.site_manual.setVisible(not self.radio_site_auto.isChecked())

    def subfolders_options(self):
        self.radio_site_manual.setEnabled(not self.checkbox_subfolders.isChecked())
        if self.radio_folder.isChecked():
            self.radio_site_auto.setChecked(True)
            self.site_auto.setVisible(True)
            self.site_manual.setVisible(False)

    # Browse source directory

    def browse_src(self):
        self.browse(self.input_src_path, self.radio_folder.isChecked())
        # if self.radio_folder.isChecked() and self.input_src_path.text():
        # Create automatically a default path to dest dir if src is a folder
        # if not self.input_dest_path.text():
        #     self.input_dest_path.setText(self.input_src_path.text())
        # List all files to display
        # self.file_manager.get_all_files(self.checkbox_subfolders)
        # TODO: extract metadata
        # self.show_files()

        # Browse destination directory
    def browse_dest(self):
        self.browse(self.input_dest_path, True)

    # Generic method to browse for files
    def browse(self, text_input, is_folder):
        default = os.getcwd()
        if is_folder:
            # We want to select a folder
            if text_input.text():
                default = text_input.text()
            text = QFileDialog.getExistingDirectory(self, "Choose directory",
                                                    default)
            self.file_manager.root_dir = text
        else:
            # We want to select files
            # TODO : add formats in config
            (files, pattern) = QFileDialog.getOpenFileNames(
                self, "Choose files", default,
                "Audio files (*.wav, *.WAV, *.wac);;WAV files (*.wav, *.WAV);;WAC files (*.wac)")
            text = "; ".join(files)
            self.file_manager.file_paths = files

        # Update gui input
        text_input.setText(text)

    def show_files(self):
        if self.file_manager.file_infos.empty:
            self.table_files.setEnabled(False)
        else:
            model = self.file_manager.file_infos
            # TODO: date format in config/options
            model["date"] = model["date"].dt.strftime("%Y-%m-%d %H:%M:%S")
            model = DataFrameTableModel(model)
            proxyModel = QSortFilterProxyModel()
            proxyModel.setSourceModel(model)
            self.table_files.setModel(proxyModel)
            self.table_files.resizeColumnsToContents()
        # self.log_console.clear()
        # self.log_console.append("\n".join(self.file_manager.file_paths))
        self.lbl_status.setText("%d file(s) found" % len(self.file_manager.file_paths))

    # @Slot()
    # def import_files(self):
    #     # Convert files to wac
    #     self.file_handler.set_args(root=self.input_src_path.text(), dest="",
    #                                files=self.to_wav)
    #     self.file_handler.moveToThread(self.thread)
    #     self.thread.start()

    @Slot()
    def thread_started(self):
        self.convert_to_wac()
        self.remove_files()

        self.log_console.clear()
        self.checkbox_done.setChecked(True)

    def convert_to_wac(self):
        self.log_console.clear()
        self.file_handler.files_to_wav()

    def remove_files(self):
        self.lbl_converting.setEnabled(False)
        self.lbl_removing.setEnabled(True)
        self.progress_bar.setValue(0)
        self.file_handler.remove_wac()

    @Slot()
    def update_progress(self, progress):
        self.progress_bar.setValue(progress)

    @Slot()
    def log(self, text):
        print(text)
        self.log_console.append(text)

    def start_conversion(self):
        print("start")
        self.initProgressBar(len(self.file_manager.files))
        self.file_manager.start()
        self.btn_cancel.setEnabled(True)
        self.btn_import.setEnabled(False)

    @Slot()
    def end_conversion(self):
        print("cancel")
        self.progress_bar.setEnabled(False)
        self.progress_bar.setValue(0)
        self.btn_cancel.setEnabled(False)
        self.btn_import.setEnabled(True)

    def showAlert(self, text):
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.setIcon(QMessageBox.Critical)
        return (msgBox.exec_())

    def showConfirmBox(self, text, info):
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.setInformativeText(info)
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Ok)
        return (msgBox.exec_())

    def initProgressBar(self, maxValue):
        self.progress_bar.setEnabled(True)
        self.progress_bar.setMaximum(maxValue)
        # self.progressBar.setValue(0)
