from django.contrib import admin
from .views import HomeView, PostDetail, AddPost
from django.urls import path

urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   path('posts/<int:pk>', PostDetail.as_view(), name='post-detail'),
   path('add_post/', AddPost.as_view(), name='add_post'),
]
