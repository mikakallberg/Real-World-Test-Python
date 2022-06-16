import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch  # to test for bugs beyond dev control


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        # student = Student("John", "Doe")
        print('test_full_name')
        self.assertEqual(self.student.full_name, "John Doe")

    def test_email(self):
        # student = Student("John",  "Doe")
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(
            self.student.end_date, old_end_date + timedelta(days=5))

    def test_alert_santa(self):
        # student = Student("John",  "Doe")
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)
    
    # successful test, should pass
    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        # Fail test, should fail
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")


if __name__ == "__main__":
    unittest.main()
