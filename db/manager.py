from abc import ABC, abstractmethod


class DBManager(ABC):
    def __init__(self, config):
        pass

    def add(self):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    @abstractmethod
    def add_audio_file(self):
        pass

    def update(self):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    def delete(self):
        raise NotImplementedError(
            "Function not implemented for this DB manager")

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def terminate(self):
        pass
