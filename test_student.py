import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('Marty', 'McFly')

        self.assertEqual(student.full_name, 'Marty McFly')

if __name__ == '__main__':
    unittest.main()