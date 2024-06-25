import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.full_name, 'John Doe')

    def test_alert_santa(self):
        student = Student('John', 'Doe')
        student.alert_santa()

        self.assertTrue(student.naughty_list)
    
    def test_email(self):
        studentemail = Student('Test', 'Testsson')

        self.assertEqual(email._first_name._last_name@email.com, 'test.testsson@email.com')

if __name__ == '__main__':
    unittest.main()