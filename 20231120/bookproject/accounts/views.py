from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm


# Create your views here.

class SignupView(generic.CreateView):
    template_name = "accounts/signup.html"
    model = User
    form_class = SignupForm
    success_url = reverse_lazy("book:index")