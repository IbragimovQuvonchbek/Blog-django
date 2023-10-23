from django.shortcuts import render
from django.views.generic import ListView,DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class BlogPostViwes(ListView):
    model = Post
    template_name = 'home.html'

class FullPostViews(DeleteView):
    model = Post
    template_name = 'full_post.html'

class CreatPostViews(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'author', 'body']
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')