from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("book/",views.ListBookView.as_view(),name="list-book"),
    path("book/<int:pk>/detail/",views.DetailBookView.as_view(),name="detail-book"),
]