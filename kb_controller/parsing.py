from typing import Any
from requests import get
from bs4 import BeautifulSoup
from collections import defaultdict


KEY_WORD_INSTITUTES = ('КБиСП',)
FILE_FORMAT = '.xlsx'


class Parse:
    def __init__(self, url: str):
        self.bs = BeautifulSoup(get(url).text, 'html.parser')

    def get_links_for_courses(self) -> defaultdict:
        course_links = defaultdict(list)
        for bs_link in self.bs.find_all('a', attrs={'class': 'uk-link-toggle'}):
            href = bs_link.get('href')
            if any(map(lambda w: w in href, KEY_WORD_INSTITUTES)) and FILE_FORMAT in href:
                course_number = bs_link.find('div', attrs={'class': 'uk-link-heading uk-margin-small-top'})
                course_links[course_number.text.strip()].append(href)
        return course_links

    def get_all_values_for_course(self): ...


class GetSchedule:
    def __init__(self, url: str, kb_model: Any = None):
        self.url = url
        self.kb_model = kb_model
        self.parse = Parse(self.url) 

    def get_links(self):
        course_links = self.parse.get_links_for_courses()
        for course_number, links in course_links.items():
            for link in links:
                # TODO: Пересмотреть логику связи таблиц в БД.
                self.kb_model.db.execute(
                    self.kb_model.schedule_links_table.insert_into('NULL', course_number, link)
                )


# if __name__ == "__main__":
#     p = Parse('https://www.mirea.ru/schedule/')
#     print(p.get_links_for_courses())
