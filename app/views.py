from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post

class Index(ListView):
  model = Post
  
class Detail(DetailView):
  model = Post
  
class Create(CreateView):
  model = Post
  fields = ['title', 'body', 'category', 'tags']
  
  success_url = '/'
  
class Update(UpdateView):
  model = Post
  fields = ['title', 'body', 'category', 'tags']
  
  success_url = '/'

class Delete(DeleteView):
  model = Post
  
  success_url = '/'

