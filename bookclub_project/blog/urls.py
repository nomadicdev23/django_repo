from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

