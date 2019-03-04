from db.feathermanager import FeatherManager
from db.hdf5manager import HDF5Manager
from db.sqlite import SQLiteManager

# def get_db_manager(config):
#     db = config.get("database", "type")
#     if db == "sqlite":
#         return (SQLiteManager(config))
#     else:
#         print("Please use a supported database")


DATABASES = {"sqlite": SQLiteManager, "hdf5": HDF5Manager, "feather": FeatherManager}


def get_db_manager(db_type, **kwargs):
    print(kwargs)
    if db_type not in DATABASES:
        raise NotImplementedError(
            "DB manager is not implemented")

    return DATABASES[db_type](**kwargs)
