from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime , date

class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.title + ' | '  + str(self.author)

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)),)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    