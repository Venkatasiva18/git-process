from django.shortcuts import render, redirect

from crud import forms
from crud.models import Employeeinfo
from crud.forms import EmployeeInfoForm


def show_view(request):
    employees = Employeeinfo.objects.all()
    return render(request, "crud/templates/index.html", {'employees': employees})


def insert_view(request):
    form = forms.EmployeeInfoForm()
    if request.method == "POST":
        form = forms.EmployeeInfoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/crud/shows/')
    return render(request, "insert.html", {'form': form})


def delete_view(request, pk):
    employee = Employeeinfo.objects.get(id=pk)
    employee.delete()
    return redirect('/crud/shows/')


def update_view(request, pk):
    employee = Employeeinfo.objects.get(pk=pk)
    form = forms.EmployeeInfoForm()
    if request.method == "POST":
        form = forms.EmployeeInfoForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/crud/shows/')
    return redirect(request, "crud/templates/update.html", {'emp': employee, 'form': form})



