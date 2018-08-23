import sqlite3

from db.dbmanager import DBManager


class SQLiteManager(DBManager):
    def __init__(self, config):
        print("initializing SQLite Manager")
        dbname = config.get("database", "name")
        self.connection = sqlite3.connect(dbname + 'db')
        #self.init_db()

    def init_db(self):
        # Create table
        self.connection.execute('''CREATE TABLE audiofile IF NOT EXISTS
             (id text, trans text, symbol text, qty real, price real)''')

    def add_audio_file(self, recording):
        pass

    def get(self, x):
        print(x)

    def terminate(self):
        self.connection.close()
