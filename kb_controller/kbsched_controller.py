from kb_model import KbschedModel
from .parsing import GetSchedule


DB_FILE_NAME = 'kb.db'
MIREA_SCHEDULE_LINK = 'https://www.mirea.ru/schedule/'


class KbschedController:
    def __init__(self):
        self.kb_model = KbschedModel(DB_FILE_NAME)
        # self.kb_view = kb_view
        self.parsing = GetSchedule(MIREA_SCHEDULE_LINK, self.kb_model)

    def run(self):
        self.kb_model.create_tables()
        if not self.kb_model.get_all_elements(self.kb_model.day_of_the_week_table):
            self.kb_model.fill_default()
        if not self.kb_model.get_all_elements(self.kb_model.schedule_links_table):
            self.parsing.get_links()
        if not self.kb_model.get_all_elements(self.kb_model.schedule_table):
            self.parsing.parse_for_course(2)
