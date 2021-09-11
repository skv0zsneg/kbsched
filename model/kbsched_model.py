from .db_handler import DbHandler
from .table_handler import TableHandler
from .enums import DayOfTheWeekDefault, WeekDefault, CourseDefault, LessonTimeDefault


TEACHER_TABLE_DATA = ('teacher', [
        ('teacher_id', 'INTEGER', 'PRIMARY KEY AUTOINCREMENT'), 
        ('teacher_name', 'TEXT', 'NOT NULL')
    ])
KBSP_GROUP_DATA = ('kbsp_group', [
        ('kbsp_group_id', 'INTEGER', 'PRIMARY KEY AUTOINCREMENT'),
        ('kbsp_group_name', 'TEXT', 'NOT NULL')
    ])
DAY_OF_THE_WEEK_DATA = ('day_of_the_week', [
        ('day_of_the_week_id', 'INTEGER', 'PRIMARY KEY AUTOINCREMENT'),
        ('day_of_week_name', 'TEXT', 'NOT NULL')
    ])
SUBJECT_DATA = ('subject', [
        ('subject_id', 'INTEGER', 'PRIMARY KEY AUTOINCREMENT'),
        ('subject_name', 'TEXT', 'NOT NULL')
    ])
WEEK_DATA = ('week', [
        ('week_id', 'INTEGER', 'PRIMARY KEY AUTOINCREMENT'),
        ('week_odd_or_even', 'TEXT', 'NOT NULL')
    ])
SUBJECT_TYPE_DATA = ('subject_type', [
        ('subject_type_id', 'INTEGER', 'PRIMARY KEY AUTOINCREMENT'),
        ('subject_type_name', 'TEXT', 'NOT NULL')
    ])
LESSON_TIME_DATA = ('lesson_time', [
        ('lesson_time_id', 'INTEGER', 'PRIMARY KEY AUTOINCREMENT'),
        ('lesson_time_from', 'TIME', 'NOT NULL'),
        ('lesson_time_to', 'TIME', 'NOT NULL')
    ])
COURSE_DATA = ('course', [
        ('course_id', 'INTEGER', 'PRIMARY KEY AUTOINCREMENT'),
        ('course_number', 'INTEGER', 'NOT NULL')
    ])
SCHEDULE_DATA = ('schedule', [
        ('schedule_id', 'INTEGER', 'PRIMARY KEY AUTOINCREMENT'),
        ('day_of_the_week_id', 'INTEGER', None),
        ('week_id', 'INTEGER', None),
        ('lesson_time_id', 'INTEGER', None),
        ('subject_id', 'INTEGER', None),
        ('subject_type_id', 'INTEGER', None),
        ('teacher_id', 'INTEGER', None),
        ('kbsp_group_id', 'INTEGER', None),
        ('course_id', 'INTEGER', None)
    ])
SCHEDULE_FOREIGN_KEYS_DATA = [('day_of_the_week_id',
                               'day_of_the_week',
                               'ON DELETE CASCADE ON UPDATE NO ACTION'),
                              ('week_id',
                               'week',
                               'ON DELETE CASCADE ON UPDATE NO ACTION'),
                              ('lesson_time_id',
                               'lesson_time',
                               'ON DELETE CASCADE ON UPDATE NO ACTION'),
                              ('subject_id',
                               'subject',
                               'ON DELETE CASCADE ON UPDATE NO ACTION'),
                              ('subject_type_id',
                               'subject_type',
                               'ON DELETE CASCADE ON UPDATE NO ACTION'),
                              ('teacher_id',
                               'teacher',
                               'ON DELETE CASCADE ON UPDATE NO ACTION'),
                              ('kbsp_group_id',
                               'kbsp_group',
                               'ON DELETE CASCADE ON UPDATE NO ACTION'),
                              ('course_id',
                               'course',
                               'ON DELETE CASCADE ON UPDATE NO ACTION')]




class KbschedModel:
    def __init__(self, db_file_name: str):
        self.db = DbHandler(db_file_name)

        self.teacher_table = TableHandler(*TEACHER_TABLE_DATA)
        self.kbsp_group_table = TableHandler(*KBSP_GROUP_DATA)
        self.day_of_the_week_table = TableHandler(*DAY_OF_THE_WEEK_DATA)
        self.subject_table = TableHandler(*SUBJECT_DATA)
        self.week_table = TableHandler(*WEEK_DATA)
        self.subject_type_table = TableHandler(*SUBJECT_TYPE_DATA)
        self.lesson_time_table = TableHandler(*LESSON_TIME_DATA)
        self.course_table = TableHandler(*COURSE_DATA)
        self.schedule_table = TableHandler(*SCHEDULE_DATA)
    
    def create_tables(self):
        self.db.execute(self.teacher_table.create_table(if_not_exist=True))
        self.db.execute(self.kbsp_group_table.create_table(if_not_exist=True))
        self.db.execute(self.day_of_the_week_table.create_table(if_not_exist=True))
        self.db.execute(self.subject_table.create_table(if_not_exist=True))
        self.db.execute(self.week_table.create_table(if_not_exist=True))
        self.db.execute(self.subject_type_table.create_table(if_not_exist=True))
        self.db.execute(self.lesson_time_table.create_table(if_not_exist=True))
        self.db.execute(self.course_table.create_table(if_not_exist=True))
        self.db.execute(self.schedule_table.create_table(foreign_keys=SCHEDULE_FOREIGN_KEYS_DATA, if_not_exist=True))
    
    def fill_default(self):
        for val in DayOfTheWeekDefault:
            self.db.execute(self.day_of_the_week_table.insert_into('NULL', val.ru_name))
        for val in WeekDefault:
            self.db.execute(self.week_table.insert_into('NULL', val.week_name))
        for val in CourseDefault:
            self.db.execute(self.course_table.insert_into('NULL', val.number_str))
        for val in LessonTimeDefault:
            self.db.execute(self.lesson_time_table.insert_into('NULL', val.time_from, val.time_to))
