from django.shortcuts import render
from secondapp.models import Student
from . import forms
import datetime

from .forms import LoginForm


def studentdata(request):
    student_list = Student.objects.all()
    my_dict = {'student_list': student_list}
    return render(request, 'product/templates/stud.html', context=my_dict)


def student_view(request):
    form = forms.StudentForm
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, 'product/templates/feedback.html',{'form':form})


def template_inheritace(request):
    msg2 = "this custom page 2"

    msg1 = "THis my own paGE"+msg2

    return render(request, 'secondapp/templates/base.html',{'msg1':msg1})


def template_inheritace1(request):
    my_date = datetime.datetime.now()
    # my_dict = {'insert_date': date1}

    return render(request, 'secondapp/templates/child.html',{'my_date': my_date})


def template_inheritace2(request):
    return render(request, 'secondapp/templates/Grand_child.html')


# Temprory Cookies(not setting any max_age)
def count_view(request):
    if 'count' in request.COOKIES:
        newcount = int(request.COOKIES['count'])+1
    else:
        newcount = 1
    response = render(request, 'secondapp/templates/count.html', {'count': newcount})
    response.set_cookie('count', newcount)
    return response


# Cookie Example3
def home_view(request):
    form = LoginForm(request.GET)
    return render(request, "secondapp/templates/home.html",{'form':form})


def date_time_view(request):
    # form = LoginForm(request.GET)

    name = request.GET['name']
    response = render(request, "secondapp/templates/datetime.html", {'name': name})
    response.set_cookie('name', name)
    return response


def result_view(request):
    name = request.COOKIES['name']
    date_time = datetime.datetime.now()
    my_dict = {'name': name, 'date_time': date_time}
    return render(request, 'secondapp/templates/result.html', my_dict)


# Cookie Example4
def name_view(request):
    return render(request, "secondapp/templates/name.html")


def age_view(request):
    name = request.GET['name']
    response = render(request, "secondapp/templates/age.html", {'name': name})
    response.set_cookie('name', name)
    return response


def gf_view(request):
    age = request.GET['age']
    name = request.COOKIES['name']
    response = render(request,'secondapp/templates/gf.html', {'name': name})
    response.set_cookie('age', age)
    return response


def results_view(request):
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    gfname = request.GET['gfname']
    response = render(request, 'secondapp/templates/results.html', {'name': name, 'age':age,'gfname':gfname})
    response.set_cookie('gfname', gfname)
    return response


# Perminent Cookies(Setting Max_age)
def index(request):
     return render(request, 'secondapp/templates/home1.html')


def additem(request):
    form = forms.ItemAddForm()
    response = render(request, 'secondapp/templates/additem.html', {'form':form})
    if request.method == "POST":
        form = forms.ItemAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name, quantity, 180)
    return response


def displayitem(request):
    return render(request, "secondapp/templates/showitems.html")



