from django import forms
from crud.models import Employeeinfo


class EmployeeInfoForm(forms.ModelForm):
    class Meta:
        model = Employeeinfo
        fields = '__all__'

