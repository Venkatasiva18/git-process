from django.contrib import admin
from django.urls import include, path
from .import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),

]