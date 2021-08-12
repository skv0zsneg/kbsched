"""
    made by @skvozsneg
"""
from core import init_bd

DB_FILE_NAME = 'kb.db'


def get_s():
    db = init_bd(DB_FILE_NAME)


if __name__ == "__main__":
    get_s()
