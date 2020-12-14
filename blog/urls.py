from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('users/', include('django.contrib.auth.urls')), # takes care of log in / log out etc
    path('users', include('users.urls')), # does the url above first then this
]
