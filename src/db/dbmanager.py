from abc import ABC, abstractmethod


class DBManager(ABC):
    def __init__(self, config):
        pass

    def save(self, table, data, update=False):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    def update(self, table, data):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    def delete(self, table, data):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    @abstractmethod
    def get_table(self, table):
        pass
