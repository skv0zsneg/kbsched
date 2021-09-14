from kb_model import KbschedModel


DB_FILE_NAME = 'kb.db'


class KbschedController:
    def __init__(self):
        self.kb_model = KbschedModel(DB_FILE_NAME)
        # self.kb_view = kb_view

    def run(self):
        self.kb_model.create_tables()
        self.kb_model.fill_default()
