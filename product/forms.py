from django import forms
from django.core import validators

class StudentForm(forms.Form):
    name = forms.CharField(max_length=200)
    marks = forms.IntegerField()


# Student Feed Back Form
class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)


# Django's inbuilt Core Validators
class FeedBackForm2(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])


# Custom Validators in forms

def starts_with_s(value):
    if value[0].lower() != 's':
        raise forms.ValidationError("Name should starts with s|S")


class FeedBackForm1(forms.Form):
    name = forms.CharField(validators=[starts_with_s])
    rollno = forms.IntegerField()


# Validation of Total form directly by using a sing;e clean Method:

class FeedBackForm3(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])

    def clean(self):
        print("Print All form Validations if all conditions are True")
        total_cleaned_data = super().clean()
        inputname = total_cleaned_data['name']
        if inputname[0].lower() != 'd':
            raise forms.ValidationError('Name Should Starts with d|D')
        elif len(inputname)<4:
            raise forms.ValidationError('Minimum Characters of Name should Be 4 ')

        inputrollno = total_cleaned_data['rollno']
        if inputrollno <= 0:
            raise forms.ValidationError("Roll No should be>0")

    def clean_email(self):
        inputemail = self.cleaned_data['email']

        return inputemail


class PassWordForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Re Enter Password', widget=forms.PasswordInput)
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):
        total_cleaned_data = super().clean()
        fpwd = total_cleaned_data['password']
        spwd = total_cleaned_data['rpassword']
        if fpwd != spwd:
            raise forms.ValidationError("Both Passwords must be matched")
        bot_handler_value = total_cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError("Request from Bot.....cannot be submitted")




