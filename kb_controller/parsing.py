import kb_model
import re
from typing import Any
from requests import get
from bs4 import BeautifulSoup


class Parse:
    def __init__(self, url: str):
        self.bs = BeautifulSoup(get(url).text, 'html.parser')

    def get_links_for_courses(self) -> list:
        # TODO: Слабая надежность валидности спарсенных ссылок.
        KEY_WORD = 'КБиСП'
        course_links = []
        for link in self.bs.find_all('a'):
            link_href = link.get('href')  
            if KEY_WORD in link_href:
                course_links.append(link_href)

        return course_links

    def get_all_values_for_course(self): ...


class GetSchedule:
    def __init__(self, url: str, kb_model: Any = None):
        self.url = url
        self.kb_model = kb_model
        self.parse = Parse(self.url) 

    def get_links(self):
        # TODO: Слабая надежность номера курса.
        course_links = self.parse.get_links_for_courses()
        for i, link in enumerate(course_links, start=1):
            self.kb_model.db.execute(
                self.kb_model.schedule_links_table.insert_into('NULL', str(i), link)
            )
