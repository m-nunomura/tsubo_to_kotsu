from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from . import forms
# Create your views here.

class SignupView(generic.CreateView):
    template_name = "accounts/signup.html"
    model = User
    form_class = forms.SignupForm
    success_url = reverse_lazy("book:index")