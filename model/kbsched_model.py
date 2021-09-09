from .db_handler import DbHandler


class KbschedModel:
    def __init__(self, db_file_name: str):
        self.db = DbHandler(db_file_name)
