from django.contrib import admin
from .views import HomeView, PostDetail, AddPost, UpdatePost, DeletePost, AddComment
from django.urls import path

urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   path('posts/<int:pk>', PostDetail.as_view(), name='post-detail'),
   path('add_post/', AddPost.as_view(), name='add_post'),
   path('posts/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
   path('posts/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    path('add_post/<int:pk>/comment', AddComment.as_view(), name='add_comment'),
]
