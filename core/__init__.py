"""
    Ядро модуля kpsched.
"""
from .sql_db import DbHandler


def init_bd(db_file_name: str):
    """Инициализация Базы даынных.

    :param db_file_name: Полное имя базы данных.
    """
    return DbHandler(db_file_name=db_file_name)


