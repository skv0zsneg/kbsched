"""
    made by @skvozsneg

    Программа misrsched парсит расписание с сайта расписания МИРЭА (https://www.mirea.ru/schedule/) для всех институтов,
    а на выходе дает простой доступ к списоку институов, в котором есть список курсов, в которых находится расписания по
    дням недели так далее. Подробнее в документации.
"""
from enum import Enum

from src.courses import Courses

class Institutes(Enum):
    FTI = (0, 'Физико-технологический институт')
    ITIGU = (1, 'Институт инновационных технологий и государственного управления')
    IT = (2, 'Институт информационных технологий')
    IK = (3, 'Институт кибернетики')
    IKBISP = (4, 'Институт комплексной безопасности и специального приборостроения')
    IRITS = (5, 'Институт радиотехнических и телекоммуникационных систем')
    ITHT = (6, 'Институт тонких химических технологий им. М.В. Ломоносова')
    IEP = (7, 'Институт экономики и права')
    IVIZO = (8, 'Институт вечернего и заочного образования')

    def __init__(self, _id, name):
        self._id = _id
        self.name = name


class Schedule:
    def __init__(
            self,
            parsed_courses=None,
            *args,
            **kwargs,

    ):
        """Базовый класс для Расписания.

        :param courses: Спарсенное расписание курсов.
        :param *args: Доп элементы.
        :param **kwargs: Доп элементы типа {ключ: значение}.
        """
        self.courses = Courses(parsed_courses)


class Fti(Schedule):
    ...


class Itigu(Schedule):
    ...


class It(Schedule):
    ...


class Ik(Schedule):
    ...


class Ikbisp(Schedule):
    def __init__(self):
        super().__init__()


class Irits(Schedule):
    ...


class Itht(Schedule):
    ...


class Iep(Schedule):
    ...


class Ivizo(Schedule):
    ...


def get_schedule(institute: Institutes) -> Schedule:
    """Фабричный метод.

    :param institute: Институт МИРЭА.
    :return: Экемпляр класса Schedule.
    """
    factory_dict = {
        Institutes.FTI: Fti,
        Institutes.ITIGU: Itigu,
        Institutes.IT: It,
        Institutes.IK: Ik,
        Institutes.IKBISP: Ikbisp,
        Institutes.IRITS: Irits,
        Institutes.ITHT: Itht,
        Institutes.IEP: Iep,
        Institutes.IVIZO: Ivizo,
    }
    return factory_dict[institute]()





