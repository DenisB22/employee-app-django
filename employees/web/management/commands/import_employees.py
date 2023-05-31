import datetime

from django.core.management import BaseCommand, CommandError
import pandas as pd
from dateutil import parser

from employees.web.models import Employee


class Command(BaseCommand):
    help = 'Import employees from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        excel_file = kwargs['excel_file']

        try:
            df = pd.read_excel(excel_file)
        except Exception as e:
            raise CommandError(f'Error reading Excel file: {str(e)}')

        for index, row in df.iterrows():
            first_name = row['First Name']
            last_name = row['Last Name']
            mobile = row['Mobile']
            position = row['Position*']
            salary = row['Salary']
            employee_id = row['Employee ID']

            start_date = row['Start Date']

            employee = Employee(
                first_name=first_name,
                last_name=last_name,
                mobile=mobile,
                start_date=start_date,
                position=position,
                salary=salary,
                employee_id=employee_id
            )
            employee.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))
