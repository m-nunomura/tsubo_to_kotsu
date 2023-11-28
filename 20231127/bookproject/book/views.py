from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.


class ListBookView(generic.ListView):
    template_name = "book/book_list.html"
    model = models.Book
    