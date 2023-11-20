from typing import Any
from django.shortcuts import render
from .models import Book,BookReview
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
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
    success_url = reverse_lazy("book:list-book")

class DeleteBookView(DeleteView):
    template_name = "book/book_delete.html"
    model = Book
    success_url = reverse_lazy("book:list-book")

class UpdateBookView(UpdateView):
    template_name = "book/book_update.html"
    model = Book
    fields = ("title","text","category")
    success_url = reverse_lazy("book:list-book")

def index_view(request):
    object_list = Book.objects.order_by("-id")
    return render(request,"book/index.html",{"object_list":object_list})

class CreateReviewView(CreateView):
    template_name = "book/review_form.html"
    model = BookReview
    fields = ("book_info","review_title","review_text","review_rate")

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["BookID"] = Book.objects.get(pk=self.kwargs["syoseki_id"])
        return context

    


