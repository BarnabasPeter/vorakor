from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def service(request):
    return render(request, 'service.html', {})
   

