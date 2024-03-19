from django.urls import path
from crud import views, views1


urlpatterns =[
    path("list/", views.BeerListView.as_view(), name="list"),
    path("detail/<pk>", views.BeerDetailView.as_view(), name="detail"),
    path("create/", views.BeerCreateView.as_view()),
    path("update/<pk>", views.BeerUpdateView.as_view(), name='update'),
    path("delete/<pk>", views.BeerDeleteView.as_view(), name='delete'),
    path("shows/", views1.show_view, name="show_view"),
    path("insert/", views1.insert_view, name="insert_view"),
    path("delete1/<pk>", views1.delete_view, name="delete_view"),
    path("update1/<str:pk>", views1.update_view, name="update_view")

]