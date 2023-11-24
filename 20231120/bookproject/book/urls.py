"""
URL configuration for bookproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("",views.index,name="index"),
    path("book/",views.ListBookView.as_view(),name="list-book"),
    path("book/<int:pk>/detail/",views.DetailBookView.as_view(),name="detail-book"),
    path("book/create/",views.CreateBookView.as_view(),name="create-book"),
    path("book/<int:pk>/delete/",views.DeleteBookView.as_view(),name="delete-book"),
    path("book/<int:pk>/update/",views.UpdateBookView.as_view(),name="update-book"),
    path("book/<int:book_id>/review/",views.CreateReviewView.as_view(),name="review"),
]