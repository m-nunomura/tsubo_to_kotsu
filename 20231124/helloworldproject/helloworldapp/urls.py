from django.urls import path
from . import views

urlpatterns = [
    path("helloworldapp/",views.helloworldfunc),
]