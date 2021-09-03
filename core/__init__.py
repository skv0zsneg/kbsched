"""
    Ядро модуля kbsched.
"""
from .sql_db import SqliteStorage
from .db_querys import create_tables_list


def init_bd(db_file_name: str) -> SqliteStorage:
    """Инициализация Базы даынных.

    :param db_file_name: Полное имя базы данных.
    """
    return SqliteStorage(db_file_name=db_file_name)


def init_upd(): ...


