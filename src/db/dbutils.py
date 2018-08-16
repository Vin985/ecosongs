from db.sqlite import SQLiteManager


def get_db_manager(config):
    db = config.get("database", "type")
    if db == "sqlite":
        return (SQLiteManager(config))
    else:
        print("Please use a supported database")
