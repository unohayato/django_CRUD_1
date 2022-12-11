from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
# Create your views here.

class Index(ListView):
  model = Post
  
class Detail(DetailView):
  model = Post
  
class Create(CreateView):
  model = Post
  fields = ['title', 'body', 'category', 'tags']
  
  success_url = "/"

class Update(UpdateView):
  model = Post
  fields = ["title", "body", "category", "tags"]
  
  success_url = "/"

class Delete(DeleteView):
  model = Post
  
  success_url = "/"
  
  
  
  
