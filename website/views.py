
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def service(request):
    return render(request, 'contact_us.html', {})

def service(request):
    return render(request, 'about_us.html', {})

def service(request):
    return render(request, 'blog_posts.html', {})

def service(request):
    return render(request, 'testimonial.html', {})

def service(request):
    return render(request, 'project.html', {})
   

