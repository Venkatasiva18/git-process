from django.urls import path
from secondapp import views, views1, views2
urlpatterns = [
    path("", views.studentdata, name="studentdata"),
    path("model/", views.student_view, name="Student_view"),
    path("inherit/", views.template_inheritace, name="template_inheritance"),
    path("time/", views.template_inheritace1, name="template_inheritance1"),
    path("grand/", views.template_inheritace2, name="template_inheritance2"),
    path("count/", views.count_view, name="count_view"),
    path("home/", views.home_view, name="home_view"),
    path("first/", views.date_time_view, name="date_time_view"),
    path("result/", views.result_view, name="result_view"),
    path("name/", views.name_view),
    path("age/", views.age_view),
    path("gf/", views.gf_view, name="gf_view"),
    path("results/", views.results_view),
    path("index/", views.index),
    path("add/", views.additem),
    path("display/", views.displayitem, name="displayitem"),
    path("pagecount/", views1.page_count, name="page_count"),
    path("name1/", views1.name_view1, name="name_view1"),
    path("age1/", views1.age_view1, name="age_view1"),
    path("gf1/", views1.gf_view1, name="gf_view1"),
    path("results1/", views1.results_view1, name="results_view1"),

    path("items/", views1.add_item_view, name="add_item_view"),
    path("show/", views1.display_item, name="display_item"),
    path("login/", views1.signup_view, name="signup_view"),
    path("class/", views2.Hello.as_view(), name="Hello"),
    path("temp/", views2.TemplateCBV.as_view()),
    path("list/", views2.CollegeListview.as_view()),
    path("company/", views2.CompanyListView.as_view(), name="companies"),
    path("detail/<pk>", views2.CompanyDetailView.as_view(), name="detail"),
    # path("create/", views2.SchoolCreateView.as_view()),
    path("create/", views2.CompanyCreateView.as_view(), name='create'),
    path("update/<pk>", views2.CompanyUpdateView.as_view(), name='update'),
    path("delete/<pk>", views2.CompanyDeleteView.as_view(), name='delete')

]
