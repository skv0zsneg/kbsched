import enum


class DbCreateTableQuery(enum.Enum):
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
            week_odd_or_even TEXT NOT NULL
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
    CREATE_COURSE_TABLE = """
        CREATE TABLE IF NOT EXISTS course (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_number INTEGER NOT NULL
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
            course_id INTEGER,
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
                ON UPDATE NO ACTION,
            FOREIGN KEY (course_id) 
                REFERENCES course (course_id)
                ON DELETE CASCADE
                ON UPDATE NO ACTION                      
        )
    """

    def __init__(self, query):
        self.query = query

    @staticmethod
    def get_all_create_table_query():
        return tuple(field.query for field in list(DbCreateTableQuery))


class DbInsertIntoTableQuery(enum.Enum):
    INSERT_INTO_TEACHER_TABLE = """
        INSERT INTO teacher
        VALUES (?,?)
    """
    INSERT_INTO_KBSP_GROUP_TABLE = """
        INSERT INTO kbsp_group
        VALUES (?,?)
    """
    INSERT_INTO_DAY_OF_THE_WEEK_TABLE = """
        INSERT INTO day_of_week
        VALUES (?,?)
    """
    INSERT_INTO_SUBJECT_TABLE = """
        INSERT INTO subject
        VALUES (?,?)
    """
    INSERT_INTO_WEEK_TABLE = """
        INSERT INTO week
        VALUES (?,?)
    """
    INSERT_INTO_SUB_TYPE_TABLE = """
        INSERT INTO sub_type
        VALUES (?,?)
    """
    INSERT_INTO_LESSON_TIME_TABLE = """
        INSERT INTO lesson_time
        VALUES (?,?,?)
    """
    INSERT_INTO_COURSE_TABLE = """
        INSERT INTO course
        VALUES (?,?)
    """
    INSERT_INTO_SCHEDULE_TABLE = """
        INSERT INTO schedule
        VALUES (?,?,?,?,?,?,?,?,?)
    """

    def __init__(self, query):
        self.query = query


class WeekDefault(enum.Enum):
    ODD = (0, 'I', False)
    EVEN = (1, 'II', True)

    def __init__(self, _id, week_name, bool_val):
        self._id = _id
        self.week_name = week_name
        self.bool_val = bool_val


class DayOfTheWeekDefault(enum.Enum):
    MON = (0, 'Понедельник', 'Monday')
    TUE = (1, 'Вторник', 'Tuesday')
    WED = (2, 'Среда', 'Wednesday')
    THU = (3, 'Четверг', 'Tuesday')
    FRI = (4, 'Пятница', 'Friday')
    SAT = (5, 'Суббота', 'Saturday')
    SUN = (6, 'Воскресенье', 'Sunday')

    def __init__(self, _id, ru_name, en_name):
        self._id = _id
        self.ru_name = ru_name
        self.en_name = en_name


class LessonTimeDefault(enum.Enum):
    L1 = (0, '9:00', '10:30')
    L2 = (1, '10:40', '12:10')
    L3 = (2, '12:40', '14:10')
    L4 = (3, '14:20', '15:50')
    L5 = (4, '16:20', '17:50')
    L6 = (5, '18:00', '19:30')
    L7 = (6, '18:30', '20:00')
    L8 = (7, '20:10', '21:40')

    def __init__(self, _id, time_from, time_to):
        self._id = _id
        self.time_from = time_from
        self.time_to = time_to


class CourseDefault(enum.Enum):
    C1 = (0, 1, '1')
    C2 = (1, 2, '2')
    C3 = (2, 3, '3')
    C4 = (3, 4, '4')
    C5 = (4, 5, '5')

    def __init__(self, _id, number_int, number_str):
        self._id = _id
        self.number_int = number_int
        self.number_str = number_str
