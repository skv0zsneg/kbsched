"""File for db query's"""

CREATE_TEACHER_TABLE = """
    CREATE TABLE IF NOT EXISTS teacher (
        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_name TEXT NOT NULL
    )
"""

CREATE_KBSP_GROUP_TABLE = """
    CREATE TABLE IF NOT EXISTS kbsp_group (
        kbsp_group_id INTEGER PRIMARY KEY AUTOINCREMENT,
        kbsp_group_name TEXT NOT NULL
    )
"""

CREATE_DAY_OF_THE_WEEK_TABLE = """
    CREATE TABLE IF NOT EXISTS day_of_week (
        day_of_week_id INTEGER PRIMARY KEY AUTOINCREMENT,
        day_of_week_name TEXT NOT NULL
    )
"""

CREATE_SUBJECT_TABLE = """
    CREATE TABLE IF NOT EXISTS subject (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT NOT NULL
    )
"""

CREATE_WEEK_TABLE = """
    CREATE TABLE IF NOT EXISTS week (
        week_id INTEGER PRIMARY KEY AUTOINCREMENT,
        week_odd_or_even INTEGER NOT NULL
    )
"""

CREATE_SUBJECT_TYPE_TABLE = """
    CREATE TABLE IF NOT EXISTS sub_type (
        sub_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sub_type_name INTEGER NOT NULL
    )
"""

CREATE_LESSON_TIME_TABLE = """
    CREATE TABLE IF NOT EXISTS lesson_time (
        lesson_time_id INTEGER PRIMARY KEY AUTOINCREMENT,
        lesson_time_from TIME NOT NULL,
        lesson_time_to TIME NOT NULL
    )
"""

CREATE_SCHEDULE_TABLE = """
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
"""


create_tables_list = [
    CREATE_TEACHER_TABLE,
    CREATE_KBSP_GROUP_TABLE,
    CREATE_DAY_OF_THE_WEEK_TABLE,
    CREATE_SUBJECT_TABLE,
    CREATE_WEEK_TABLE,
    CREATE_SUBJECT_TYPE_TABLE,
    CREATE_LESSON_TIME_TABLE,
    CREATE_SCHEDULE_TABLE
]

