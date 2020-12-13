from django.shortcuts import render
from django.views.generic import ListView, DetailView # ListView - Allows me to list a query set into the database, detailView - brings one record only
from .models import Post
# def home(request):
#     return render(request, 'home.html', {})

#class views
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
