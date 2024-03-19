# Session Api
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import forms


def page_count(request):
    count = request.session.get('count', 0)
    newcount = count + 1
    request.session['count'] = newcount
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request, "secondapp/templates/count.html", {'count': newcount})


# Demo Application2
def name_view1(request):
    form = forms.NameForm()
    return render(request, "secondapp/templates/name1.html", {'form': form})


def age_view1(request):
    name = request.GET['name']
    request.session['name'] = name
    form = forms.AgeForm()
    return render(request, "secondapp/templates/age1.html", {'form': form})


def gf_view1(request):
    age = request.GET['age']
    request.session['age'] = age
    form = forms.GFForm()
    return render(request, "secondapp/templates/gf1.html", {'form': form})


def results_view1(request):
    gf = request.GET['gf']
    request.session['gf'] = gf
    return render(request, "secondapp/templates/results1.html")


def add_item_view(request):
    form = forms.ItemAddForm()
    if request.method == "POST":
        form = forms.ItemAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']
            request.session[name] = quantity
    return render(request, "secondapp/templates/add_item.html", {'form': form})


def display_item(request):
    return render(request, "secondapp/templates/display_items.html")


def signup_view(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/second/accounts/login/')
    return render(request, "secondapp/templates/signup.html", {'form': form})
