from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import generic
from . import models
from django.urls import reverse_lazy,reverse

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

class UpdateBookView(generic.UpdateView):
    template_name = "book/book_update.html"
    model = models.Book
    fields = ("title","text","category",)
    success_url = reverse_lazy("book:list-book")

def index(request):
    object_list = models.Book.objects.order_by("category")
    return render(request,"book/index.html",{"object_list":object_list})

class CreateReviewView(generic.CreateView):
    template_name = "book/review_form.html"
    model = models.Review
    fields = ("book","title","text","rate",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = models.Book.objects.get(pk=self.kwargs["book_id"])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("book:detail-book",kwargs={"pk":self.object.book.id})