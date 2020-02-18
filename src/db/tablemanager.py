import utils.commons as utils

from .models import TableModel
import os


class TableManager:

    TABLE_MODULE = "db.tables"

    def __init__(self, dbmanager=None):
        if not dbmanager:
            raise ValueError("A database manager must be provided")
        self._dbmanager = dbmanager

    @staticmethod
    def table_classname(name):
        return "".join(name.title().split("_")) + "Table"

    def get_class(self, name):
        try:
            model_name = self.table_classname(name)
            mod = __import__(".".join([self.TABLE_MODULE, name]),
                             fromlist=[model_name])
            cls = getattr(mod, model_name)
            if not issubclass(cls, TableModel):
                raise ImportError("%s must subclass %s" %
                                  (model_name, TableModel))
        except ModuleNotFoundError:
            print(utils.fullclassname(TableModel))
            msg = ("No class named {0} was found."
                   " Please create a class that extends {1} and place it"
                   " in db.tables").format(model_name, utils.fullclassname(TableModel))
            raise ImportError(msg)
        return cls

    def __getattr__(self, name):
        print("Dynamically loading " + self.table_classname(name))
        cls = self.get_class(name)
        instance = cls(dbmanager=self._dbmanager)
        self.__setattr__(name, instance)
        return self.__getattribute__(name)

    def get_table(self, name, *args, **kwargs):
        cls = self.get_class(name)
        instance = cls(*args, dbmanager=self._dbmanager, **kwargs)
        return instance

    def list_tables(self):
        module_path = os.path.join(*self.TABLE_MODULE.split("."))
        path = os.path.join(os.getcwd(), module_path)
        tables = [os.path.splitext(f)[0] for f in os.listdir(path) if os.path.isfile(
            os.path.join(path, f)) and f.endswith(".py")]
        return tables
