import logging
import resource
import sys

from pandarallel import pandarallel
from PySide2.QtWidgets import QApplication

from db import dbutils
from db.tablemanager import TableManager
from gui.ecosongsUI import EcosongsUI
from gui.utils.settings import Settings

pandarallel.initialize()


class Ecosongs(QApplication):
    def get_recordings(self, df=True):
        if df:
            return self.tables.recordings.df
        return self.tables.recordings.recordings

    def load_recordings(self, indexes):
        return self.tables.recordings.load_recordings(indexes)

    def __init__(self, argv):
        super().__init__(argv)
        self.setOrganizationName("ecosongs")
        self.setOrganizationDomain("CRCEco")
        self.setApplicationName("ecosongs")
        settings = Settings()

        db_opts = settings.group_to_dict("database")
        if not db_opts:
            print("adding database defaults")
            # TODO: Change defaults!
            db_opts.update(
                {"database": "ecosongs", "db_type": "feather", "path": "db",}
            )

        self.dbmanager = dbutils.get_db_manager(**db_opts)
        self.tables = TableManager(self.dbmanager)
        print(
            "Ecosongs init: Memory usage: %s (kb)"
            % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        )


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print(
        "Main: Memory usage: %s (kb)"
        % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    )
    app = Ecosongs(sys.argv)
    print(
        "Main2: Memory usage: %s (kb)"
        % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    )
    ui = EcosongsUI()

    ui.showMaximized()
    sys.exit(app.exec_())
