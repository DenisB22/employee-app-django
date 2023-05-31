# Generated by Django 4.2.1 on 2023-05-27 10:34

import django.core.validators
from django.db import migrations, models
import employees.web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, validators=[employees.web.models.validate_first_name], verbose_name='First Name')),
                ('last_name', models.CharField(max_length=40, validators=[employees.web.models.validate_first_name], verbose_name='Last Name')),
                ('mobile', models.CharField(max_length=9, validators=[employees.web.models.validate_mobile], verbose_name='Mobile')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('position', models.CharField(choices=[('Junior Developer', 'Junior Developer'), ('Senior Developer', 'Senior Developer'), ('Team Lead', 'Team Lead'), ('Project Manager', 'Project Manager'), ('CEO', 'CEO')], max_length=50, verbose_name='Position')),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Salary')),
                ('employee_id', models.CharField(max_length=6, validators=[employees.web.models.validate_employee_id], verbose_name='Employee ID')),
            ],
        ),
    ]