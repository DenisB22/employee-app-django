from django.shortcuts import render, redirect, get_object_or_404

from employees.web.forms import EmployeeCreateForm, EmployeeEditForm, EmployeeDeleteForm
from employees.web.models import Employee

from rest_framework import viewsets

from employees.web.serializers import EmployeeSerializer


# Create your views here.

def get_employee():
    try:
        pass
    except Employee.DoesNotExist:
        return None


def index(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees,
    }

    # return render(request, '../templates/base.html', context)
    return render(request, '../templates/core/index.html', context)


def create_employee(request):

    if request.method == 'GET':
        form = EmployeeCreateForm()

    else:
        form = EmployeeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)

    context = {
        'form': form,
    }

    return render(request, '../templates/employee/employee-create.html', context)


def details_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    context = {
        'employee': employee,
    }

    return render(request, '../templates/employee/employee-details.html', context)


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'GET':
        form = EmployeeEditForm(instance=employee)
    else:
        form = EmployeeEditForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)

    context = {
        'employee': employee,
        'form': form,
    }

    return render(request, '../templates/employee/employee-edit.html', context)


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'GET':
        form = EmployeeDeleteForm(instance=employee)
    else:
        form = EmployeeDeleteForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)

    context = {
        'employee': employee,
        'form': form,
    }

    return render(request, '../templates/employee/employee-delete.html', context)


# Django REST Framework
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
