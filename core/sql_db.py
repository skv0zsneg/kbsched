import sqlite3
from os import path
from typing import Union
from contextlib import contextmanager

DB_FILE_NAME = 'kb.db'


class DbHandler:
    def __init__(self, db_file_name: str):
        self.__db_file_name = db_file_name
        self.__path, _ = path.split(__file__)

    @contextmanager
    def __cursor(self):
        conn = sqlite3.connect(path.join(self.__path, self.__db_file_name))
        yield conn.cursor()

    def _execute(self, query: Union[str, list]):
        with self.__cursor() as cur:
            cur.execute(query)
            cur.commit()



class SqliteStorage:
    def __init__(self, db_file_name: str):
        self.db_handler = DbHandler(db_file_name)
        with self.db_handler.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS teacher (
                    tch_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS kbsp_group (
                    kg_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    kg_name TEXT NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS day_of_week (
                    dw_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dw_name TEXT NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS subject (
                    sub_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sub_name TEXT NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS week (
                    week_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    odd_even INTEGER NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS sub_type (
                    st_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    st_name INTEGER NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS lesson_time (
                    lt_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    time_from TIME NOT NULL,
                    time_to TIME NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS schedule (
                    sch_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    FOREIGN KEY (dw_id) 
                        REFERENCES day_of_week (dw_id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION,
                    FOREIGN KEY (week_id) 
                        REFERENCES week (week_id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION,
                    FOREIGN KEY (lt_id) 
                        REFERENCES lesson_time (lt_id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION,
                    FOREIGN KEY (sub_id) 
                        REFERENCES subject (sub_id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION,
                    FOREIGN KEY (st_id) 
                        REFERENCES sub_type (st_id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION,
                    FOREIGN KEY (tch_id) 
                        REFERENCES teacher (tch_id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION,
                    FOREIGN KEY (kg_id)
                        REFERENCES kbsp_group (kg_id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION                             
                )
            """)


if __name__ == "__main__":
    db = SqliteStorage(DB_FILE_NAME)
