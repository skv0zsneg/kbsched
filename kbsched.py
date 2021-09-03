"""
    made by @skvozsneg
"""
from core import init_bd, init_upd


DB_FILE_NAME = 'kb.db'


class KbSched:
    def __init__(self):
        self.db = init_bd(DB_FILE_NAME)
        self.upd = init_upd()


if __name__ == "__main__":
    my_schedule = KbSched()
