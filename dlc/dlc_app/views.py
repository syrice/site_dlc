from django.shortcuts import render
from.models import Foods

def index(request):
    foods=Foods.objects.all().order_by("-created_at")[:7]
    return render(request, 'index.html',{"foods":foods})

def test(request):
    all_elements = Foods.objects.all()
    element_by_id = Foods.objects.get(pk=2)
    element_by_field = Foods.objects.get(pk=2)
    filtered_elements = Foods.objects.all().filter(image='recept')
    ordered_elements = Foods.objects.all().order('-created_at')
    return render(request, 'elements.html', {})

def elements(request):
    foods=Foods.objects.all()[:3]
    return render(request, 'elements.html',{"foods":foods})

def contact(request):
    return render(request, 'contact.html', {})

def blogpost(request):
    return render(request, 'blog-post.html', {})

def recept(request):
    return render(request, 'receipe-post.html', {})

def about(request):
    return render(request, 'about.html', {})
