"""
    made by @skvozsneg
"""
from model import KbschedModel


DB_FILE_NAME = 'kb.db'


if __name__ == "__main__":
    model = KbschedModel(DB_FILE_NAME)
    model.create_tables()
    model.fill_default()
