import os

from PySide2.QtCore import QSortFilterProxyModel, Qt, QThread, Signal, Slot
from PySide2.QtGui import qApp
from PySide2.QtWidgets import QFileDialog, QMessageBox, QWizard

from gui.utils.dataframeTableModel import DataFrameTableModel
from gui.widgets.dbmanager.QFileManager import QFileManager
from gui.widgets.dbmanager.ui.fileimport_ui import Ui_FileImport

# TODO: put files in config

DEST_DIR = "wav"


class FileImport(QWizard, Ui_FileImport):
    get_infos = Signal()
    import_files = Signal()
    list_files_convert = Signal()

    def __init__(self):
        super().__init__()
        # Initialize UI
        self.setupUi(self)
        self.init_ui()
        self.file_manager = QFileManager()

        self.init_thread()
        self.registerFields()
        self.linkEvents()
        self.setWizardStyle(QWizard.ClassicStyle)

    def init_thread(self):
        self.worker_thread = QThread()
        self.file_manager.moveToThread(self.worker_thread)
        self.finished.connect(self.worker_thread.quit)
        self.worker_thread.finished.connect(self.file_manager.deleteLater)
        self.worker_thread.start()

    def init_ui(self):
        self.site_manual.setVisible(not self.radio_site_auto.isChecked())
        self.checkbox_done.setVisible(False)

    def registerFields(self):
        self.page1.registerField("src_path*", self.input_src_path)
        self.page5.registerField("done*", self.checkbox_done)

    # Define callbacks when events happen
    def linkEvents(self):
        # Signals emitted
        self.get_infos.connect(
            self.file_manager.get_infos)
        self.import_files.connect(
            self.file_manager.import_files)
        self.list_files_convert.connect(
            self.file_manager.get_files_to_convert)

        # Signals received
        # File manager
        self.file_manager.converting.connect(
            self.converting_files, type=Qt.BlockingQueuedConnection)
        self.file_manager.removing.connect(
            self.removing_files, type=Qt.BlockingQueuedConnection)
        self.file_manager.renaming.connect(
            self.renaming_files, type=Qt.BlockingQueuedConnection)
        self.file_manager.saving.connect(
            self.saving_files, type=Qt.BlockingQueuedConnection)
        self.file_manager.logging.connect(
            self.log, type=Qt.BlockingQueuedConnection)
        self.file_manager.filesLoaded.connect(
            self.show_files, type=Qt.BlockingQueuedConnection)
        self.file_manager.progressed.connect(
            self.update_progress, type=Qt.BlockingQueuedConnection)
        self.file_manager.tosave.connect(self.save_files)
        # Buttons
        self.btn_browse_src.clicked.connect(self.browse_src)
        self.btn_browse_dest.clicked.connect(self.browse_dest)
        # Radio
        self.radio_is_folder.buttonToggled.connect(self.folder_options)
        self.radio_site_info.buttonToggled.connect(self.site_info_options)
        # Checkbox
        self.checkbox_subfolders.toggled.connect(self.subfolders_options)
        self.checkbox_move.toggled.connect(self.display_move_options)

    def display_move_options(self):
        self.move_options.setVisible(self.checkbox_move.isChecked())

    def initializePage(self, id):
        getattr(self, "initialize_page" + str(id), lambda: None)()

    # TODO : Validate manual entries

    def initialize_page1(self):
        site_info = {}
        # get information about site from comboboxes
        if self.radio_site_auto.isChecked():
            for i in range(1, 4):
                tmp = getattr(self, "combo_idx_" + str(i)
                              ).currentText().lower()
                site_info[tmp] = i
        else:
            site_info["site"] = self.input_site
            site_info["year"] = self.input_year
            site_info["plot"] = self.input_plot

        self.file_manager.options = {"folder": self.radio_folder.isChecked(),
                                     "recursive": self.checkbox_subfolders.isChecked(),
                                     "recorder": self.radio_recorders.button(self.radio_recorders.checkedId()).text(),
                                     "folder_hierarchy": self.radio_site_auto.isChecked(),
                                     "site_info": site_info,
                                     "save_file_info": self.checkbox_save_info.isChecked(),
                                     "load_file_info": self.checkbox_load_info.isChecked()}
        self.get_infos.emit()
        # self.file_manager.get_files()

    def initialize_page2(self):
        self.move_options.setVisible(self.checkbox_move.isChecked())
        # TODO : add compression options
        self.compression_options.setEnabled(False)

    def initialize_page3(self):
        self.list_files_convert.emit()

    def initialize_page4(self):
        # Convert files to wac
        self.file_manager.set_args(dest="")
        opts = {"rename": self.checkbox_rename.isChecked(),
                "move": self.checkbox_move.isChecked(),
                "create_links": self.checkbox_link.isChecked(),
                "remove_wac": False,
                "overwrite": self.checkbox_overwrite.isChecked()
                }
        self.file_manager.options.update(opts)
        self.file_manager.dest_dir = self.input_dest_path.text()
        self.import_files.emit()

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
        self.radio_site_manual.setEnabled(
            not self.checkbox_subfolders.isChecked())
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
        # TODO modify browse to accomodate for destination

    # Generic method to browse for files
    def browse(self, text_input, is_folder):
        default = os.getcwd()
        if is_folder:
            # We want to select a folder
            if text_input.text():
                default = text_input.text()
            text = QFileDialog.getExistingDirectory(self, "Choose directory",
                                                    default)
            # TODO remove this line
            self.file_manager.root_dir = text
        else:
            # We want to select files
            # TODO : add formats in config
            (files, _) = QFileDialog.getOpenFileNames(
                self, "Choose files", default,
                "Audio files (*.wav *.WAV *.wac);;WAV files (*.wav *.WAV);;WAC files (*.wac)")
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
        self.lbl_status.setText("%d file(s) found" %
                                self.file_manager.file_infos.shape[0])

    @Slot()
    def converting_files(self):
        self.log_console.clear()

    @Slot()
    def removing_files(self):
        self.lbl_converting.setEnabled(False)
        self.lbl_removing.setEnabled(True)
        self.progress_bar.setValue(0)

    @Slot()
    def renaming_files(self):
        self.lbl_removing.setEnabled(False)
        self.lbl_renaming.setEnabled(True)
        self.progress_bar.setValue(0)
        if self.checkbox_rename.isChecked():
            pass

    @Slot()
    def saving_files(self):
        self.lbl_renaming.setEnabled(False)
        self.lbl_saving.setEnabled(True)
        self.progress_bar.setValue(0)

    def save_files(self):
        print("saving for real")
        print(self.file_manager.to_save)
        qApp.tables.recordings.add(self.file_manager.to_save, save=True,
                                   replace=self.checkbox_reimport.isChecked())
        self.checkbox_done.setChecked(True)

    @Slot()
    def update_progress(self, progress):
        print(progress)
        self.progress_bar.setValue(progress)

    @Slot()
    def log(self, text):
        if self.currentId() == 1:
            self.lbl_status.setText(text)
        else:
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
