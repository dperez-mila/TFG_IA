
import sqlite3
from . import DataManagement


class SQLiteDataManagement(DataManagement):
    
    def __init__(self, db_path: str):
        self._db_path = db_path
        self._connection = None
        self._cursor = None

    def connect(self):
        self._connection = sqlite3.connect(self._db_path)
        self._cursor = self._connection.cursor()
    
    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()
    
    def execute_query(self, query: str, params: tuple = ()):
        if not self._cursor:
            raise Exception("DataBase connection is not established!")
        self._cursor.execute(query, params)
        self._connection.commit()
    
    def fetch_results(self):
        if not self._cursor:
            raise Exception("DataBase connection is not established!")
        return self._cursor.fetchall()
    
    def get_description(self):
        return self._cursor.description
    
    