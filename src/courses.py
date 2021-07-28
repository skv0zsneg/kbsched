class Courses:
    def __init__(self, parsed_courses):
        """Обертка для спарсенных курсов какого-либо института."""
        self._parsed_courses = parsed_courses
