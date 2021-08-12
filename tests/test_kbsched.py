import unittest

import kbsched


class GetScheduleCases(unittest.TestCase):
    def setUp(self):
        self.schedule = kbsched.get_s()

    def tearDown(self):
        ...

    def test_get_current_day(self):
        """Проверка расписания на текущий день."""
        today_schedule = self.schedule.today

        self.assertIsInstance(today_schedule, tuple)




