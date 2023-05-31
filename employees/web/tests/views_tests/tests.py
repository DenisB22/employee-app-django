from datetime import datetime
from time import strftime
from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse

from employees.web.forms import EmployeeCreateForm, EmployeeEditForm, EmployeeDeleteForm
from employees.web.models import Employee


class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '../templates/core/index.html')


class CreateEmployeeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_employee_get(self):
        response = self.client.get(reverse('create employee'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '../templates/employee/employee-create.html', )
        self.assertIsInstance(response.context['form'], EmployeeCreateForm)

    def test_create_employee_post_valid_form(self):
        start_date = '2022.01.01'

        data = {
            'employee_id': 'S-9123',
            'first_name': 'John',
            'last_name': 'Snow',
            'mobile': '123456789',
            'start_date': start_date,
            'position': 'Junior Developer',
            'salary': 'BGN 1300',
        }

        response = self.client.post(reverse('create employee'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.count(), 1)

    def test_create_employee_post_invalid_form(self):
        start_date = '2022.01.01'

        data = {
            'employee_id': 'S3',
            'first_name': 'John',
            'last_name': 'Snow',
            'mobile': '123456789',
            'start_date': start_date,
            'position': 'Junior Developer',
            'salary': 'BGN 1300',
        }

        response = self.client.post(reverse('create employee'), data)

        self.assertEqual(Employee.objects.count(), 0)


class DetailsEmployeeViewTest(TestCase):
    def setUp(self):

        self.client = Client()
        # start_date = '2022.01.01'

        start_date = datetime(year=2022, month=1, day=1)

        self.employee = Employee.objects.create(
            employee_id='S-9123',
            first_name='John',
            last_name='Snow',
            mobile='123456789',
            start_date=start_date,
            position='Junior Developer',
            salary='BGN 1300',
        )

    def test_details_employee(self):
        response = self.client.get(reverse('details employee', args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '../templates/employee/employee-details.html', )
        self.assertEqual(self.employee, response.context['employee'])


class EditEmployeeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        start_date = datetime(year=2022, month=1, day=1)

        self.employee = Employee.objects.create(
            employee_id='S-9123',
            first_name='John',
            last_name='Snow',
            mobile='123456789',
            start_date=start_date,
            position='Junior Developer',
            salary='BGN 1300',
        )

    def test_edit_employee_get(self):
        response = self.client.get(reverse('edit employee', args=[self.employee.id]))
        self.assertTemplateUsed(response, '../templates/employee/employee-edit.html')
        self.assertEqual(self.employee, response.context['employee'])
        self.assertIsInstance(response.context['form'], EmployeeEditForm)
        self.assertContains(response, 'value="John"')

    def test_edit_employee_post_valid_form(self):
        start_date = '2022.01.01'
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'mobile': '987654321',
            'start_date': start_date,
            'position': 'Senior Developer',
            'salary': 'BGN 7000',
        }
        response = self.client.post(reverse('edit employee', args=[self.employee.id]), data)
        # self.assertRedirects(response, reverse('index'))

        updated_employee = Employee.objects.get(id=self.employee.id)
        self.assertEqual(updated_employee.mobile, '987654321')
        self.assertEqual(updated_employee.position, 'Senior Developer')
        self.assertEqual(updated_employee.salary, 'BGN 7000')


class DeleteEmployeeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        start_date = datetime(year=2022, month=1, day=1)

        self.employee = Employee.objects.create(
            employee_id='S-9123',
            first_name='John',
            last_name='Snow',
            mobile='123456789',
            start_date=start_date,
            position='Junior Developer',
            salary='BGN 1300',
        )

    def test_delete_employee_get(self):
        response = self.client.get(reverse('delete employee', args=[self.employee.id]))
        self.assertTemplateUsed(response, '../templates/employee/employee-delete.html')
        self.assertEqual(self.employee, response.context['employee'])
        self.assertIsInstance(response.context['form'], EmployeeDeleteForm)

    def test_delete_employee_post_valid_form(self):
        start_date = '2022.01.01'
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'mobile': '987654321',
            'start_date': start_date,
            'position': 'Senior Developer',
            'salary': 'BGN 7000',
        }

        response = self.client.post(reverse('delete employee', args=[self.employee.id]), data)

        self.assertFalse(Employee.objects.filter(id=self.employee.id).exists())

