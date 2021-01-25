import unittest
from unittest import TestCase
from test_simple_employee import Employee
from unittest.mock import patch


class TestEmployee(TestCase):

    def setUp(self):
        self.employee = Employee(first='John', last='Braun', pay=1500.50)

    def test_email_employee(self):
        message = self.employee.email
        self.assertEqual('John.Braun@email.com', message)

    def test_full_name_employee(self):
        message = self.employee.fullname
        self.assertEqual(f'John Braun', message)

    def test_apply_raise(self):
        self.employee.apply_raise()
        self.assertEqual(self.employee.pay, 1575)

    def test_make_true_request(self):
        with patch('test_simple_employee.requests.get') as mock:
            mock.return_value.ok = 200
            mock.return_value.text = 'Person info'
            request = self.employee.monthly_schedule('June')
            print(request)
            self.assertEqual(request, 'Person info')

    def test_make_bad_request(self):
        with patch('test_simple_employee.requests.get') as mock:
            mock.return_value.response.ok = 0
            mock.return_value.text = 'Bad Response!'
            request = self.employee.monthly_schedule('June')
            print(request)
            self.assertEqual(request, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
