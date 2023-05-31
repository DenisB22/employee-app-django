from datetime import datetime

from django.core import exceptions
from django.test import TestCase

from employees.web.models import Employee, validate_first_name, validate_last_name, validate_mobile, validate_salary, \
    validate_employee_id


# Create your tests here.

class EmployeeTestCase(TestCase):

    def setUp(self):
        start_date = datetime(year=2022, month=1, day=1)

        Employee.objects.create(
            employee_id='S-9123',
            first_name='John',
            last_name='Snow',
            mobile='123456789',
            start_date=start_date,
            position='Junior Developer',
            salary='BGN 1300',
        )

    def test_employee_creation(self):
        # Test the creation of an employee
        employee = Employee.objects.get(employee_id='S-9123')
        self.assertEqual(employee.first_name, 'John')
        self.assertEqual(employee.last_name, 'Snow')
        self.assertEqual(employee.mobile, '123456789')
        self.assertEqual(employee.start_date.isoformat(), '2022-01-01')
        self.assertEqual(employee.position, 'Junior Developer')
        self.assertEqual(employee.salary, 'BGN 1300')


class ValidationTests(TestCase):
    def test_validate_first_name(self):
        with self.assertRaises(exceptions.ValidationError):
            validate_first_name('A')

    def test_validate_last_name(self):
        with self.assertRaises(exceptions.ValidationError):
            validate_last_name('A')

    def test_validate_mobile(self):
        with self.assertRaises(exceptions.ValidationError):
            validate_mobile('1234')

    def test_validate_salary(self):
        with self.assertRaises(exceptions.ValidationError):
            validate_salary('USD 1000')

    def test_validate_employee_id(self):
        start_date = datetime(year=2022, month=1, day=1)

        Employee.objects.create(
            employee_id='S-1234',
            first_name='John',
            last_name='Snow',
            mobile='123456789',
            start_date=start_date,
            position='Junior Developer',
            salary='BGN 1300',
        )

        with self.assertRaises(exceptions.ValidationError):
            validate_employee_id('S-1234')

    def test_validate_employee_id_invalid(self):
        with self.assertRaises(exceptions.ValidationError):
            validate_employee_id('1234')


