import sqlite3
import typing
from os import path, listdir
from contextlib import contextmanager


class DbHandler:
    def __init__(self, db_file_name: str):
        self.__db_file_name = db_file_name
        self.path, _ = path.split(__file__)

        self.initialize()

    @contextmanager
    def __cursor(self):
        conn = sqlite3.connect(path.join(self.path, self.__db_file_name))
        yield conn.cursor()
        conn.commit()

    def execute(self, *query):
        with self.__cursor() as cur:
            for q in query:
                cur.execute(q)

    def initialize(self):
        if self.__db_file_name not in listdir(self.path):
            with open(path.join(self.path, self.__db_file_name), 'w'):
                pass
