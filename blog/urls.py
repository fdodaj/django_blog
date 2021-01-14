from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('users/', include('django.contrib.auth.urls')), # takes care of log in / log out etc
    path('users', include('users.urls')), # does the url above first then this
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
