from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def pysiotherapy(request):
    return render(request, 'pysiotherapy.html')

def occupational(request):
    return render(request, 'occupational.html')

def admission(request):
    return render(request, 'admission.html')

def departments(request):
    return render(request, 'departments.html')
    
def testimonials(request):
    return render(request, 'testimonials.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')
