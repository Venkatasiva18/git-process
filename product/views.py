from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):
    date = datetime.datetime.now()
    msg = 'Hello Guest!!! Very Good'
    h = int(date.strftime('%H'))
    if h < 12:
        msg += 'Morning!!!'
    elif h < 16:
        msg += 'Afternoon!!!'
    elif h < 21:
        msg += 'Evening!!!'
    else:
        msg = "Hello Guest!!! Very Good Night!!!"
    my_dict = {'insert_date': date, 'insert_msg': msg}
    return render(request, 'product/templates/index.html', context=my_dict)


def wish(request):
    date = datetime.datetime.now()
    my_dict = {'insert_date': date}
    return render(request, "product/templates/wish.html", context=my_dict)


def moviesinfo(request):
    my_dict = {
        'head_msg': 'Movies Information',
        'sub_msg1': 'Sonali getting slowly cured',
        'sub_msg2': 'Bahaubali-3 is just planning',
        'sub_msg3': 'Salman Khan ready to marriage',
        'photo': 'images/oskar-smethurst-B1GtwanCbiw-unsplash.jpg'

    }
    return render(request, "product/templates/news.html", context=my_dict)


def sportsinfo(request):
    my_dict = {
        'head_msg': 'Sports Information',
        'sub_msg1': 'Anushka Sharma is Wife of Virat Kohli',
        'sub_msg2': 'Virat can break sachin sir recoed',
        'sub_msg3': '2023 india lift the World Cup',
        'photo': 'images/gettyimages-111507587-594x594.jpg'

    }
    return render(request, "product/templates/news.html", context=my_dict)


def politicsinfo(request):
    my_dict = {
        'head_msg': 'Politics Information',
        'sub_msg1': 'Who is Next Cm In Andhra Pradesh?',
        'sub_msg2': 'Who is Next President of India?',
        'sub_msg3': 'What happened Next One year in indian Politics?',
        'photo': 'images/istockphoto-173932687-1024x1024.jpg'

    }
    return render(request, "product/templates/news.html", context=my_dict)


def head(request):
    return render(request, "product/templates/head.html")


from product.models import Employee


def empdata(request):
    emp_list = Employee.objects.all()
    my_dict = {'emp_list': emp_list}
    return render(request, 'product/templates/emp.html', context=my_dict)


from . import forms


def studentinputview(request):
    form = forms.StudentForm()
    if request.method == "POST":
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            print("Form Validation Success and printing data")
            print("Name:", form.cleaned_data['name'])
            print("Marks:", form.cleaned_data['marks'])

    return render(request, "product/templates/input.html", {'form': form})


def feedbackview(request):
    form = forms.FeedBackForm()
    if request.method == "POST":
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            print("Form Validating Success and Printing Data")
            print("Name:", form.cleaned_data["name"])
            print("Roll No:", form.cleaned_data["rollno"])
            print("Email:", form.cleaned_data["email"])
            print("FeedBack:", form.cleaned_data["feedback"])
    return render(request, "product/templates/feedback.html", {'form': form})


def feedbackview2(request):
    form = forms.FeedBackForm2()
    if request.method == "POST":
        form = forms.FeedBackForm2(request.POST)
        if form.is_valid():
            print("Form Validating Success and Printing Data")
            print("Name:", form.cleaned_data["name"])
            print("Email:", form.cleaned_data["email"])
            print("FeedBack:", form.cleaned_data["feedback"])
            print("Roll No:", form.cleaned_data["rollno"])
        else:
            print("Feed back characters are not valid")
    return render(request, "product/templates/feedback.html", {'form': form})


def feedbackview1(request):
    form = forms.FeedBackForm1()
    if request.method == "POST":
        form = forms.FeedBackForm1(request.POST)
        if form.is_valid():
            print("Form Validating Success and Printing Data")
            print("Name:", form.cleaned_data["name"])
            print("Roll No:", form.cleaned_data["rollno"])
        else:
            print("Validation Error")
    return render(request, "product/templates/feedback.html", {'form': form})


def feedbackview3(request):
    form = forms.FeedBackForm3()
    if request.method == "POST":
        form = forms.FeedBackForm3(request.POST)
        if form.is_valid():
            print("Form Validating Success and Printing Data")
            print("Name:", form.cleaned_data["name"])
            print("Roll No:", form.cleaned_data["rollno"])
            print("Email:", form.cleaned_data["email"])
            print("FeedBack:", form.cleaned_data["feedback"])
        else:
            print("Validation Error")
    return render(request, "product/templates/feedback.html", {'form': form})


def feedbackview4(request):
    form = forms.PassWordForm()
    if request.method == "POST":
        form = forms.PassWordForm(request.POST)
        if form.is_valid():
            print("Form Validating Success and Printing Data")
            print("Name:", form.cleaned_data["name"])
            print("Roll No:", form.cleaned_data["rollno"])
            print("Email:", form.cleaned_data["email"])
            print("FeedBack:", form.cleaned_data["feedback"])
            print("BOT:", form.cleaned_data["bot_handler"])

        else:
            print("Validation Error")

    return render(request, "product/templates/feedback.html", {'form': form})


def session(request):
    request.session.set_test_cookie()
    return HttpResponse('<h1>Index Page</h1>')


def check_View(request):
    if request.session.test_cookie_worked():
        print("Cookies worked properly")
        return HttpResponse ("page")

        # request.session.delete_test_cookie()
        # return HttpResponse('<h1>Checking Page</h1>')



def session1(request):
    request.session.set_test_cookie()
    return HttpResponse("<h2>Siva</h2>")
def check1_View(request):
    if request.session.test_cookie_worked():
        print("Cookies worked properly")
        request.session.delete_test_cookie()
        return HttpResponse('<h1>Index Page</h1>')

