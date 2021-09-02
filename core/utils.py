import enum


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
