from datetime import datetime, time

from django.core import exceptions, validators
from django.db import models


def validate_first_name(first_name):
    if len(first_name) < 2:
        raise exceptions.ValidationError('The first name must be a minimum of 2 characters')


def validate_last_name(last_name):
    if len(last_name) < 2:
        raise exceptions.ValidationError('The last name must be a minimum of 2 characters')


def validate_mobile(mobile):
    if len(mobile) < 9:
        raise exceptions.ValidationError('The mobile must be a minimum of 9 numbers')


def validate_start_date(start_date):
    start_date = str(start_date)

    if '.' not in start_date and '/' not in start_date and '-' not in start_date:
        raise exceptions.ValidationError('Please enter the date in one of the following formats: YYYY-MM-DD, YYYY/MM/DD, YYYY.MM.DD')
    else:
        start_date_list = []

        if '.' in start_date:
            start_date_list = start_date.split('.')

        elif '-' in start_date:
            start_date_list = start_date.split('-')

        elif '/' in start_date:
            start_date_list = start_date.split('/')

        year = start_date_list[0]
        month = start_date_list[1]
        day = start_date_list[2]

        if len(year) != 4 or len(month) != 2 or len(day) != 2:
            raise exceptions.ValidationError(
                'Please enter the date in one of the following formats: YYYY-MM-DD, YYYY/MM/DD, YYYY.MM.DD')

        year_int = int(start_date_list[0])
        month_int = int(start_date_list[1])
        day_int = int(start_date_list[2])

        if year_int < 1950 or year_int > 2023:
            raise exceptions.ValidationError('The year must be between 1950 and 2023')

        if month_int < 1 or month_int > 12:
            raise exceptions.ValidationError('The month must be between 1 and 12')

        if day_int < 1 or day_int > 31:
            raise exceptions.ValidationError('The day must be between 1 and 31')


def validate_salary(salary):
    if 'BGN' in salary:
        salary_as_int = int(salary.split(' ')[1])
        if salary_as_int < 0:
            raise exceptions.ValidationError('The salary must be a positive number')
    else:
        raise exceptions.ValidationError('Please enter currency - BGN, in this format: BGN "salary"')


def validate_employee_id(employee_id):
    try:
        numeric_id = int(employee_id[2:])

    except ValueError:
        numeric_id = None

    if employee_id[0] != 'S' or employee_id[1] != '-' or numeric_id is None:
        raise exceptions.ValidationError('Invalid employee ID')

    if len(employee_id) != 6:
        raise exceptions.ValidationError('Invalid employee ID')

    id = Employee.objects.filter(employee_id=employee_id)
    if id:
        raise exceptions.ValidationError('Employee with this ID already exists')


def reformat_date(date_str):
    # date_parts = []

    # Split the date string by the '.' separator
    if '.' in date_str:
        date_parts = date_str.split('.')
    elif '/' in date_str:
        date_parts = date_str.split('/')
    elif '-' in date_str:
        date_parts = date_str.split('-')

    # Rearrange the date parts to match the desired format
    formatted_date = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"

    return formatted_date


class Employee(models.Model):
    MAX_LEN_FIRST_NAME = 40
    MAX_LEN_LAST_NAME = 40
    MAX_LEN_MOBILE = 9
    MAX_LEN_POSITION = 50
    MAX_LEN_SALARY = 10
    MAX_LEN_EMPLOYEE_ID = 6
    MIN_VALUE_SALARY = 0

    JUNIOR_DEVELOPER = 'Junior Developer'
    SENIOR_DEVELOPER = 'Senior Developer'
    TEAM_LEAD = 'Team Lead'
    PROJECT_MANAGER = 'Project Manager'
    CEO = 'CEO'

    POSITIONS = (
        (JUNIOR_DEVELOPER, JUNIOR_DEVELOPER),
        (SENIOR_DEVELOPER, SENIOR_DEVELOPER),
        (TEAM_LEAD, TEAM_LEAD),
        (PROJECT_MANAGER, PROJECT_MANAGER),
        (CEO, CEO),
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validate_first_name,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validate_first_name,
        ),
        null=False,
        blank=False,
    )

    mobile = models.CharField(
        verbose_name='Mobile',
        max_length=MAX_LEN_MOBILE,
        validators=(
            validate_mobile,
        ),
        null=False,
        blank=False,
    )

    start_date = models.DateField(
        verbose_name='Start Date',
        validators=(
            validate_start_date,
        ),
        null=False,
        blank=False,
    )

    # start_date = models.CharField(
    #     verbose_name='Start Date',
    #     max_length=50,
    #     null=False,
    #     blank=False,
    # )

    position = models.CharField(
        verbose_name='Position',
        max_length=MAX_LEN_POSITION,
        choices=POSITIONS,
        null=False,
        blank=False,
    )

    salary = models.CharField(
        verbose_name='Salary',
        max_length=MAX_LEN_SALARY,
        null=False,
        blank=False,
        validators=(
            validate_salary,
        ),
    )

    employee_id = models.CharField(
        verbose_name='Employee ID',
        max_length=MAX_LEN_EMPLOYEE_ID,
        validators=(
            validate_employee_id,
        ),
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)

    def save(self, *args, **kwargs):
        if isinstance(self.start_date, str):
            # Reformat the date if it is a string
            print(self.start_date)
            self.start_date = reformat_date(self.start_date)
        elif isinstance(self.start_date, datetime):
            # Convert datetime object to a string and reformat
            self.start_date = reformat_date(self.start_date.strftime('%d.%m.%Y'))

        super().save(*args, **kwargs)
