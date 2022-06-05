import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('Marty', 'McFly')

        self.assertEqual(student.full_name, 'Marty McFly')


    def test_email(self):
        student = Student('Marty', 'McFly')

        self.assertEqual(student.email, 'marty.mcfly@email.com')


    def test_alert_santa(self):
        student = Student('Marty', 'McFly')
        student.alert_santa()

        self.assertTrue(student.naughty_list)


if __name__ == '__main__':
    unittest.main()