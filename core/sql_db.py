import sqlite3
from typing import Any
from os import path, listdir
from contextlib import contextmanager

from .db_querys import (insert_into_week_table_query,
                        insert_into_day_of_week_table_query,
                        insert_into_kbsp_group_table_query,
                        insert_into_lesson_time_table_query,
                        insert_into_schedule_table_query,
                        insert_into_sub_type_table_query,
                        insert_into_subject_table_query,
                        insert_into_teacher_table_query,
                        insert_into_course_table_query)

from .enums import (DayOfTheWeekDefault,
                    LessonTimeDefault,
                    WeekDefault,
                    CourseDefault,
                    DbCreateTableQuery,
                    DbInsertIntoTableQuery)


class DbHandler:
    def __init__(self, db_file_name: str):
        self.__db_file_name = db_file_name
        self.path, _ = path.split(__file__)

    @contextmanager
    def __cursor(self):
        conn = sqlite3.connect(path.join(self.path, self.__db_file_name))
        yield conn.cursor()
        conn.commit()

    # TODO: Сделать обощенный execute для параметров и без них!
    def execute(self, query, *params): ...

    def execute_with_no_params(self, *query):
        with self.__cursor() as cur:
            for q in query:
                cur.execute(q)

    def execute_with_params(self, *parameters, query):
        with self.__cursor() as cur:
            cur.execute(query, parameters=[parameters])


class SqliteStorage:
    def __init__(self, db_file_name: str):
        self.db = DbHandler(db_file_name)

        # -- initialize db --
        if db_file_name not in listdir(self.db.path):
            self.db.execute(*DbCreateTableQuery.get_all_create_table_query())
            self.fill_db_with_default_values()

    def fill_db_with_default_values(self):
        for field in DayOfTheWeekDefault:
            self.db.execute(DbInsertIntoTableQuery.INSERT_INTO_DAY_OF_THE_WEEK_TABLE.query,
                            field.ru_name)
        for field in LessonTimeDefault:
            self.db.execute(DbInsertIntoTableQuery.INSERT_INTO_LESSON_TIME_TABLE.query,
                            field.time_from,
                            field.time_to)
        for field in WeekDefault:
            self.db.execute(DbInsertIntoTableQuery.INSERT_INTO_WEEK_TABLE.query,
                            field.week_name)
        for field in CourseDefault:
            self.db.execute(DbInsertIntoTableQuery.INSERT_INTO_COURSE_TABLE.query,
                            field.int_number)
