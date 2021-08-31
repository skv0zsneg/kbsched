import sqlite3
from os import path
from contextlib import contextmanager

from .db_querys import create_tables_list


class DbHandler:
    def __init__(self, db_file_name: str):
        self.__db_file_name = db_file_name
        self.__path, _ = path.split(__file__)

    @contextmanager
    def __cursor(self):
        conn = sqlite3.connect(path.join(self.__path, self.__db_file_name))
        yield conn.cursor()
        conn.commit()

    def execute(self, *query):
        with self.__cursor() as cur:
            for q in query:
                cur.execute(q)


class SqliteStorage:
    def __init__(self, db_file_name: str):
        self.db_handler = DbHandler(db_file_name)
        self.db_handler.execute(*create_tables_list)
