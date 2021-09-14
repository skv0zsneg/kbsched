from enum import Enum


class Links(Enum):
    MIREA_SCHEDULE = (0, 'https://www.mirea.ru/schedule/')

    def __init__(self, _id, url):
        self._id = _id
        self.url = url
