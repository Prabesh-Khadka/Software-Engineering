# singleton_db.py

import sqlite3

class SingletonConnection:
    _instance = None

    def __new__(cls, db_file="DBMS.db"):
        if cls._instance is None:
            cls._instance = super(SingletonConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(db_file)
            cls._instance.connection.execute("PRAGMA foreign_keys = ON")
        return cls._instance

    def get_connection(self):
        return self.connection
    def close_connection(self):
        if self.connection:
            self.connection.close()
            SingletonConnection._instance = None