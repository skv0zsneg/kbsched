"""File for db query's"""


###############################
# START: Insert table query's #
###############################

def insert_into_teacher_table_query(teacher_name: str) -> str:
    return f"""
        INSERT INTO teacher
        VALUES (NULL, '{teacher_name}')
    """


def insert_into_kbsp_group_table_query(kbsp_group_name: str) -> str:
    return f"""
        INSERT INTO kbsp_group
        VALUES (NULL, '{kbsp_group_name}')
    """


def insert_into_day_of_week_table_query(day_of_week_name: str) -> str:
    return f"""
        INSERT INTO day_of_week
        VALUES (NULL, '{day_of_week_name}')
    """


def insert_into_subject_table_query(subject_name: str) -> str:
    return f"""
        INSERT INTO subject
        VALUES (NULL, '{subject_name}')
    """


def insert_into_week_table_query(week_odd_or_even: str) -> str:
    return f"""
        INSERT INTO week
        VALUES (NULL, '{week_odd_or_even}')
    """


def insert_into_sub_type_table_query(sub_type_name: str) -> str:
    return f"""
        INSERT INTO sub_type
        VALUES (NULL, '{sub_type_name}')
    """


def insert_into_lesson_time_table_query(lesson_time_from: str,
                                        lesson_time_to: str) -> str:
    return f"""
        INSERT INTO lesson_time
        VALUES (NULL, '{lesson_time_from}', '{lesson_time_to}')
    """


def insert_into_course_table_query(course_number: str) -> str:
    return f"""
        INSERT INTO course
        VALUES (NULL, '{course_number}')
    """


def insert_into_schedule_table_query(day_of_week_id: str,
                                     week_id: str,
                                     lesson_time_id: str,
                                     subject_id: str,
                                     sub_type_id: str,
                                     teacher_id: str,
                                     kbsp_group_id: str,
                                     course_id: str) -> str:
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
            '{kbsp_group_id}',
            '{course_id}'
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
    CREATE_SCHEDULE_TABLE,
    CREATE_COURSE_TABLE
]

#########################
# END: Lists of query's #
#########################
