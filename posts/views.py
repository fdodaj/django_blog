from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView , UpdateView, DeleteView# ListView - Allows me to list a query set into the database, detailView - brings one record only
from .models import Post
from django.urls import reverse_lazy

#class views
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__' # allows me to put all as fileds

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'body']

class DeletePost(DeleteView):
    model= Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
