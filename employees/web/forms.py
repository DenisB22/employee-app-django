from django import forms

from employees.web.models import Employee


class EmployeeBaseForm(forms.ModelForm):
    start_date = forms.DateField(input_formats=['%Y.%m.%d', '%Y/%m/%d', '%Y-%m-%d'])

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateForm(EmployeeBaseForm):
    pass


class EmployeeEditForm(EmployeeBaseForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'mobile', 'start_date', 'position', 'salary']


class EmployeeDeleteForm(EmployeeBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'mobile', 'start_date', 'position', 'salary']