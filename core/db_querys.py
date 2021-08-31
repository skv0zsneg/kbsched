"""File for db query's"""

#################################
# START: Creating table query's #
#################################

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
        schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
        day_of_week_id INTEGER,
        week_id INTEGER,
        lesson_time_id INTEGER,
        subject_id INTEGER,
        sub_type_id INTEGER,
        teacher_id INTEGER,
        kbsp_group_id INTEGER,
        FOREIGN KEY (day_of_week_id) 
            REFERENCES day_of_week (day_of_week_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        FOREIGN KEY (week_id) 
            REFERENCES week (week_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        FOREIGN KEY (lesson_time_id) 
            REFERENCES lesson_time (lesson_time_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        FOREIGN KEY (subject_id) 
            REFERENCES subject (subject_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        FOREIGN KEY (sub_type_id) 
            REFERENCES sub_type (sub_type_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        FOREIGN KEY (teacher_id) 
            REFERENCES teacher (teacher_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        FOREIGN KEY (kbsp_group_id)
            REFERENCES kbsp_group (kbsp_group_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION                             
    )
"""

###############################
# END: Creating table query's #
###############################


###############################
# START: Insert table query's #
###############################

def insert_into_teacher_table(teacher_name: str) -> str:
    return f"""
        INSERT INTO teacher
        VALUES (NULL, '{teacher_name}')
    """


def insert_into_kbsp_group_table(kbsp_group_name: str) -> str:
    return f"""
        INSERT INTO kbsp_group
        VALUES (NULL, '{kbsp_group_name}')
    """


def insert_into_day_of_week_table(day_of_week_name: str) -> str:
    return f"""
        INSERT INTO day_of_week
        VALUES (NULL, '{day_of_week_name}')
    """


def insert_into_subject_table(subject_name: str) -> str:
    return f"""
        INSERT INTO subject
        VALUES (NULL, '{subject_name}')
    """


def insert_into_week_table(week_odd_or_even: bool) -> str:
    return f"""
        INSERT INTO week
        VALUES (NULL, '{int(week_odd_or_even)}')
    """


def insert_into_sub_type_table(sub_type_name: str) -> str:
    return f"""
        INSERT INTO sub_type
        VALUES (NULL, '{sub_type_name}')
    """


def insert_into_lesson_time_table(lesson_time_from: str,
                                  lesson_time_to: str) -> str:
    return f"""
        INSERT INTO lesson_time
        VALUES (NULL, '{lesson_time_from}', '{lesson_time_to}')
    """


def insert_into_schedule_table(day_of_week_id: str,
                               week_id: str,
                               lesson_time_id: str,
                               subject_id: str,
                               sub_type_id: str,
                               teacher_id: str,
                               kbsp_group_id: str) -> str:
    return f"""
        INSERT INTO schedule
        VALUES (
            NULL,
            '{day_of_week_id}',
            '{week_id}',
            '{lesson_time_id}',
            '{subject_id}',
            '{sub_type_id}',
            '{teacher_id}',
            '{kbsp_group_id}'
        )
    """

#############################
# END: Insert table query's #
#############################


###########################
# START: Lists of query's #
###########################

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

#########################
# END: Lists of query's #
#########################
