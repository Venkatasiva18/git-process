from django import forms
from secondapp.models import Student, Company


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class LoginForm(forms.Form):
    name = forms.CharField()
    Username = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)


class ItemAddForm(forms.Form):
    itemname = forms.CharField()
    quantity = forms.CharField()


class NameForm(forms.Form):
    name = forms.CharField()


class AgeForm(forms.Form):
    age = forms.IntegerField()


class GFForm(forms.Form):
    gf = forms.CharField()


from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']








