import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('Marty', 'McFly')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        # student = Student('Marty', 'McFly')
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'Marty McFly')

    def test_email(self):
        # student = Student('Marty', 'McFly')
        print('test_email')
        self.assertEqual(self.student.email, 'marty.mcfly@email.com')

    def test_alert_santa(self):
        # student = Student('Marty', 'McFly')
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_apply_extension(self):
        # student = Student('Marty', 'McFly')
        print('test_apply_extension')
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    def test_course_schedule_success(self):


if __name__ == '__main__':
    unittest.main()
