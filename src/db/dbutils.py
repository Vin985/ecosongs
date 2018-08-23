from db.hdf5manager import HDF5Manager
from db.sqlite import SQLiteManager

# def get_db_manager(config):
#     db = config.get("database", "type")
#     if db == "sqlite":
#         return (SQLiteManager(config))
#     else:
#         print("Please use a supported database")


dbs = {"sqlite": SQLiteManager, "hdf5": HDF5Manager}


def get_db_manager(database, type, *args, **kwargs):
    if type not in dbs:
        raise NotImplementedError(
            "DB manager is not implemented")

    return dbs[type](database, *args, **kwargs)
