from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def elements(request):
    return render(request, 'elements.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def blogpost(request):
    return render(request, 'blog-post.html', {})

def recept(request):
    return render(request, 'receipe-post.html', {})

def about(request):
    return render(request, 'about.html', {})
