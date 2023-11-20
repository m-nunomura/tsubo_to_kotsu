from django.shortcuts import render
from .models import Book
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


# Create your views here.
class ListBookView(ListView):
    template_name = "book/book_list.html"
    model = Book

class DetailBookView(DetailView):
    template_name = "book/book_detail.html"
    model = Book

class CreateBookView(CreateView):
    template_name = "book/book_create.html"
    model = Book
    fields = ("title","text","category")
    success_url = reverse_lazy("book_app:list-book")

class UpdateBookView(UpdateView):
    template_name = "book/book_update.html"
    model = Book
    fields = ("title","text","category")
    success_url = reverse_lazy("book_app:list-book")

class DeleteBookView(DeleteView):
    template_name = "book/book_delete.html"
    model = Book
    success_url = reverse_lazy("book_app:list-book")

def index(request):
    object_list = Book.objects.order_by("category")
    return render(request,"book/index.html",{"object_list":object_list})

class CreateReviewView(CreateView):
    template_name = "book/review_form.html"
    