from db.sqlite import SQLiteManager


def getDBManager(config):
    # TODO: Check if type exists
    db = config['type']
    if db == "sqlite":
        return (SQLiteManager(config))
    else:
        print("Please use a supported database")
