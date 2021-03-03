from django.shortcuts import render


def index(request):
    return render(request, 'index.html',{})
def recept(request):
    return render(request, 'receipe-post.html',{})
