from django.urls import path
from product import views
urlpatterns = [
    path("", views.index, name="index"),
    path("wish/", views.wish, name="wish"),
    path("movies/", views.moviesinfo, name="moviesinfo"),
    path("sports/", views.sportsinfo, name="sportsinfo"),
    path("politics/", views.politicsinfo, name="politicssinfo"),
    path("head/", views.head, name="head"),
    path("employee/", views.empdata, name="empdata"),
    path("input/", views.studentinputview, name="studentinputview"),
    path("student/", views.feedbackview, name="feedbackview"),
    path("custom1/", views.feedbackview2, name="feedbackview2"),
    path("custom/", views.feedbackview1, name="feedbackview1"),
    path("custom2/", views.feedbackview3, name="feedbackview3"),
    path("pass/", views.feedbackview4, name="feedbackview4"),
    path("session/", views.session, name="session"),
    path("check/", views.check_View, name="check_view"),
    path("session1/", views.session1, name="session1"),

    path("check1/", views.check1_View, name="check1_view"),

]
