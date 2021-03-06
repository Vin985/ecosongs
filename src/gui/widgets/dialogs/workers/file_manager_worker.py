import pandas as pd
from PySide2.QtCore import QObject, Signal

from db.tables.recordings import RecordingsTable
from gui.threads.parallel_worker import ParallelWorker
from gui.utils.settings import Settings
from utils.file_manager import FileManager


class FileManagerWorker(QObject, ParallelWorker, FileManager):
    filesLoaded = Signal()

    converting = Signal()
    removing = Signal()
    renaming = Signal()
    saving = Signal()
    tosave = Signal()
    logging = Signal(str)
    progressed = Signal(int)

    def log(self, text):
        self.logging.emit(text)

    def update_progress(self, step=1):
        if self.with_progress:
            self.progress += step
            print("progress: " + str(self.progress))
            self.progressed.emit(int(self.progress / self.nitems * 100))

    def __init__(self):
        QObject.__init__(self)
        ParallelWorker.__init__(self)
        settings = Settings()
        FileManager.__init__(self, sites=settings.sites_path)
        self.options["multiprocess"] = False
        self.to_save = None

    def import_files(self):
        self.convert_files(self.to_wav)
        self.remove_wac()
        self.rename_files()
        self.save_recordings()

    def files_loaded(self):
        # TODO: change to use persistence model
        # qApp.save_data("recordings", self.file_infos, format="t")
        self.filesLoaded.emit()

    def convert_files(self, files):
        print("converting")
        self.converting.emit()
        # self.open_archive()
        self.map(files, self.convert_file)
        # self.close_archive()

    def remove_wac(self):
        # TODO: finish handling this
        self.removing.emit()
        if self.options["remove_wac"]:
            pass
            # self.map(self.to_wav, os.remove)

    def rename_files(self):
        # TODO: add checkbox test in option files
        self.renaming.emit()
        self.rename(
            rename=self.options["rename"],
            create_links=self.options["create_links"],
            overwrite=self.options["overwrite"],
        )
        # if self.options["create_links"]:
        #     self.create_links()
        # cols = self.file_infos.loc[:, ["path", "old_name", "name"]]
        # new_paths = [self.get_new_path(*row)
        #              for row in cols.itertuples(index=False)]
        # tmp = list(zip(self.file_infos.loc[:, "path"], new_paths))
        # self.map(tmp, self.rename_file_tuple)

    def save_recordings(self):
        self.saving.emit()
        print("saving")
        to_save = self.file_infos.loc[
            :, self.file_infos.columns.intersection(RecordingsTable.COLUMNS)
        ]
        to_save["date"] = pd.to_datetime(to_save["date"])
        # TODO: import tags with files?
        to_save.loc[:, "has_tags"] = 0
        self.to_save = to_save
        self.tosave.emit()
