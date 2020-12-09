
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    return render(request, 'contact-us.html', {})

def about(request):
    return render(request, 'about-us.html', {})

def blog(request):
    return render(request, 'blog_posts.html', {})

def service(request):
    return render(request, 'testimonial.html', {})

def service(request):
    return render(request, 'project.html', {})

def service(request):
    return render(request, 'service.html', {})
   