from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import generic
from . import models
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg

# Create your views here.
class ListBookView(LoginRequiredMixin,generic.ListView):
    template_name = "book/book_list.html"
    model = models.Book

class DetailBookView(LoginRequiredMixin,generic.DetailView):
    template_name = "book/book_detail.html"
    model = models.Book

class CreateBookView(LoginRequiredMixin,generic.CreateView):
    template_name = "book/book_create.html"
    model = models.Book
    fields = ("title","text","category","thumbnail",)
    success_url = reverse_lazy("book:list-book")

    def form_valid(self,form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class DeleteBookView(LoginRequiredMixin,generic.DeleteView):
    template_name = "book/book_delete.html"
    model = models.Book
    success_url = reverse_lazy("book:list-book")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj

class UpdateBookView(LoginRequiredMixin,generic.UpdateView):
    template_name = "book/book_update.html"
    model = models.Book
    fields = ("title","text","category","thumbnail",)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj
    
    def get_success_url(self):
        return reverse("book:detail-book",kwargs={"pk":self.object.id})

def index(request):
    object_list = models.Book.objects.order_by("-id")
    ranking_list = models.Book.objects.annotate(avg_rating=Avg("review__rate")).order_by("-avg_rating")
    return render(request,"book/index.html",{"object_list":object_list,"ranking_list":ranking_list})

class CreateReviewView(LoginRequiredMixin,generic.CreateView):
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