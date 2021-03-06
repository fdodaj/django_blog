from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime , date
from django import forms
from django.db.models import Count


class Post(models.Model):
    title = models.CharField(max_length=225)
    post_image = models.ImageField(null=True, blank=True,  upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | '  + str(self.author)

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)),)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class Report(models.Model):
    post = models.ForeignKey(Post, related_name='reports', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
   

  

    