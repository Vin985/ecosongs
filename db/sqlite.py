import sqlite3

from db.manager import DBManager


class SQLiteManager(DBManager):
    def __init__(self, config):
        print("initializing SQLite Manager")
        self.conn = sqlite3.connect(config['name'] + 'db')
