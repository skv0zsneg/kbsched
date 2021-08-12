import sqlite3
from os import path
from contextlib import contextmanager


class DbHandler:
    def __init__(self, db_file_name):
        self.__db_file_name = db_file_name
        self.__path, _ = path.split(__file__)

    @contextmanager
    def cursor(self):
        conn = sqlite3.connect(path.join(self.__path, self.__db_file_name))
        yield conn.cursor()


class SqliteStorage:
    ...


if __name__ == "__main__":
    t = DbHandler('kb.db')


