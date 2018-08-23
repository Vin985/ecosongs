from abc import ABC, abstractmethod


class DBManager(ABC):
    def __init__(self, config):
        pass

    def add(self):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    def update(self):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    def delete(self):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    @abstractmethod
    def get_table(self, table):
        pass

    @abstractmethod
    def save_data(self, table):
        pass
