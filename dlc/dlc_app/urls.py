from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('recept/', views.recept, name="recept"),
]
