from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView , CreateView , UpdateView, DeleteView  # ListView - Allows me to list a query set into the database, detailView - brings one record only
from .models import Post, Comment
from django.urls import reverse_lazy, reverse
from .forms import PostForm , CommentForm
from django.http import HttpResponseRedirect

#class views

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data()
        current_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = current_post.total_likes()

        liked = False
        if current_post.likes.filter(id=self.request.user.id).exists():
            liked = True 


        context['total_likes'] = total_likes
        context['liked'] = liked 
        return context                    
            

    

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
    success_url = reverse_lazy('home')
   

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form) 
       
       

    
    
