from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView # ListView - Allows me to list a query set into the database, detailView - brings one record only
from .models import Post

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

