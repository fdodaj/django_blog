from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView , UpdateView, DeleteView# ListView - Allows me to list a query set into the database, detailView - brings one record only
from .models import Post, Comment
from django.urls import reverse_lazy
from .forms import PostForm , CommentForm

#class views
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['post_date']

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__' 
    success_url = reverse_lazy('home')

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')

class DeletePost(DeleteView):
    model= Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form) 

    success_url = reverse_lazy('home')
    
