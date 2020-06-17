from abc import ABC, abstractmethod


class DBManager(ABC):
    SAVE_EXTENSION = ""

    def __init__(self):
        pass

    def save(self, table, data):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    def update(self, table, data):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    def delete(self, table, data):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    def export_table(self, data, dest_path):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    def import_table(self, src_path):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    @abstractmethod
    def get_table(self, table=None, path=None):
        pass
