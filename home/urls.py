from django.conf.urls.static import static
from django.urls import path

from config import settings
from .views import *
urlpatterns = [
    path('',home, name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('articles/',blog, name='blog'),
    path('blogsingle/<int:pk>/',blog_single, name='blog_single'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)