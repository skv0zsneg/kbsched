import sqlite3
from os import path, listdir
from contextlib import contextmanager

from .db_querys import (create_tables_list,
                        insert_into_week_table_query,
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
                    DbCreateTableQuery)


class DbHandler:
    def __init__(self, db_file_name: str):
        self.__db_file_name = db_file_name
        self.path, _ = path.split(__file__)

    @contextmanager
    def __cursor(self):
        conn = sqlite3.connect(path.join(self.path, self.__db_file_name))
        yield conn.cursor()
        conn.commit()

    def execute(self, *query):
        with self.__cursor() as cur:
            for q in query:
                cur.execute(q)


class SqliteStorage:
    def __init__(self, db_file_name: str):
        self.db_handler = DbHandler(db_file_name)

        # -- initialize db --
        if db_file_name not in listdir(self.db_handler.path):
            self.db_handler.execute(*DbCreateTableQuery.get_all_create_table_query())
            self.fill_table_with_default_values()

    def fill_table_with_default_values(self):
        for field in WeekDefault:
            self.db_handler.execute(insert_into_week_table_query(week_odd_or_even=field.week_name))
        for field in DayOfTheWeekDefault:
            self.db_handler.execute(insert_into_day_of_week_table_query(day_of_week_name=field.ru_name))
        for field in LessonTimeDefault:
            self.db_handler.execute(insert_into_lesson_time_table_query(lesson_time_from=field.time_from,
                                                                        lesson_time_to=field.time_to))
        for field in CourseDefault:
            self.db_handler.execute(insert_into_course_table_query(course_number=field.number_int))

    def insert_into_schedule_table(self): ...

    def insert_into_kbsp_group_table(self, kbsp_group_names: tuple):
        for name in kbsp_group_names:
            self.db_handler.execute(insert_into_kbsp_group_table_query(kbsp_group_name=name))

    def insert_into_sub_type_table(self, sub_type_name: tuple):
        for name in sub_type_name:
            self.db_handler.execute(insert_into_sub_type_table_query(sub_type_name=name))

    def insert_into_subject_table(self, subject_name: tuple):
        for name in subject_name:
            self.db_handler.execute(insert_into_subject_table_query(subject_name=name))

    def insert_into_teacher_table(self, teacher_name: tuple):
        for name in teacher_name:
            self.db_handler.execute(insert_into_teacher_table_query(teacher_name=name))
