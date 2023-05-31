from django.urls import path, include

from employees.web.views import index, create_employee, details_employee, edit_employee, delete_employee


urlpatterns = (
    path('', index, name='index'),
    path('employee/', include([
        path('create/', create_employee, name='create employee'),
        path('details/<int:id>/', details_employee, name='details employee'),
        path('edit/<int:id>/', edit_employee, name='edit employee'),
        path('delete/<int:id>/', delete_employee, name='delete employee'),
    ])),
)