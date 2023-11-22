from django.shortcuts import render
from django.views import generic
from . import models
from django.urls import reverse_lazy

# Create your views here.
class ListBookView(generic.ListView):
    template_name = "book/book_list.html"
    model = models.Book

class DetailBookView(generic.DetailView):
    template_name = "book/book_detail.html"
    model = models.Book

class CreateBookView(generic.CreateView):
    template_name = "book/book_create.html"
    model = models.Book
    fields = ("title","text","category",)
    success_url = reverse_lazy("book:list-book")

class DeleteBookView(generic.DeleteView):
    template_name = "book/book_delete.html"
    model = models.Book
    success_url = reverse_lazy("book:list-book")