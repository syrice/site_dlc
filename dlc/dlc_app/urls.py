from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('test/', views.test, name="test"),
    path('recept/', views.recept, name="recept"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('elements/', views.elements, name="elements"),
    path('blogpost/', views.blogpost, name="blogpost"),
    path('blog_2/', views.blog_2, name="blog_2"),
]
