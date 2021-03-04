from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('test/', views.test, name="test"),
    path('recept/', views.recept, name="recept"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('elements/', views.elements, name="elements"),
    path('blogpost/', views.blogpost, name="blogpost"),
]
