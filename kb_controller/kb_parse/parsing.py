import requests
from bs4 import BeautifulSoup

from .enums import Links


class ParseHandler:
    def __init__(self, url: str):
        self.url = url


if __name__ == "__main__":
    ParseHandler(url=Links.MIREA_SCHEDULE.url)
