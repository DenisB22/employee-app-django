web: gunicorn employees.wsgi
release: python manage.py migrate
release: python manage.py import_employees employee_table.xlsx