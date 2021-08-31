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

# TODO: MUST BE FIXED sqlite3.OperationalError: near "week_id": syntax error

CREATE_SCHEDULE_TABLE = """
    CREATE TABLE IF NOT EXISTS schedule (
        schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
        day_of_week_id INTEGER,
        FOREIGN KEY (day_of_week_id) 
            REFERENCES day_of_week (day_of_week_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        week_id INTEGER,
        FOREIGN KEY (week_id) 
            REFERENCES week (week_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        lesson_time_id INTEGER,
        FOREIGN KEY (lesson_time_id) 
            REFERENCES lesson_time (lesson_time_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        subject_id INTEGER,
        FOREIGN KEY (subject_id) 
            REFERENCES subject (subject_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        sub_type_id INTEGER,
        FOREIGN KEY (sub_type_id) 
            REFERENCES sub_type (sub_type_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) 
            REFERENCES teacher (teacher_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        kbsp_group_id INTEGER,
        FOREIGN KEY (kbsp_group_id)
            REFERENCES kbsp_group (kbsp_group_id)
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
