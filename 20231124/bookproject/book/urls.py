from django.urls import path
from . import views

appname = "book"

urlpatterns = [
    path("book/",views.ListBookView.as_view(),name="list-book"),
]