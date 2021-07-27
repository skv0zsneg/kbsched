"""
    made by @skvozsneg

    Программа misrsched парсит расписание с сайта расписания МИРЭА (https://www.mirea.ru/schedule/) для всех институтов,
    а на выходе дает простой доступ к списоку институов, в котором есть список курсов, в которых находится расписания по
    дням недели так далее. Подробнее в документации.
"""
from enum import Enum


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
    def __init__(self):
        """Базовый класс для Расписания."""


class Fti(Schedule):
    def __init__(self):
        """Класс для работы с институтом ФТИ."""
        super().__init__()


class Itigu(Schedule):
    ...


class It(Schedule):
    ...


class Ik(Schedule):
    ...


class Ikbisp(Schedule):
    ...


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





