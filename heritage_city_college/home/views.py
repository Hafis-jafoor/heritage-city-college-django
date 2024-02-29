from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import contacts
from django.contrib import messages

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

# def contact(request):
#     return render(request, 'contact.html')



# def contact(request):
#     if request.method == 'POST':
#         contact_name = request.POST.get('name')
#         contact_email = request.POST.get('email')
#         contact_phone = request.POST.get('phone')
#         contact_subject = request.POST.get('subject')
#         contact_message = request.POST.get('message')

#         # Create and save the contact object
#         contact = contacts.objects.create(
#             contact_name=contact_name,
#             contact_email=contact_email,
#             contact_phone=contact_phone,
#             contact_subject=contact_subject,
#             contact_message=contact_message,
#         )
#     return render(request, 'contact.html')


# def contact(request):
#     if request.method == 'POST':
#         contact_name = request.POST.get('name')
#         contact_email = request.POST.get('email')
#         contact_phone = request.POST.get('phone')
#         contact_subject = request.POST.get('subject')
#         contact_message = request.POST.get('message')

#         # Check if the email already exists
#         if contacts.objects.filter(contact_email=contact_email).exists():
#             messages.error(request, 'Email already exists.')
#             return redirect('contact')
    
#         # Create and save the contact object
#         contact = contacts.objects.create(
#             contact_name=contact_name,
#             contact_email=contact_email,
#             contact_phone=contact_phone,
#             contact_subject=contact_subject,
#             contact_message=contact_message,
#         )
#         messages.success(request, 'Your message has been sent successfully.')
#         return redirect('contact')

#     return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_phone = request.POST.get('phone')
        contact_subject = request.POST.get('subject')
        contact_message = request.POST.get('message')

        # Check if the email already exists
        if contacts.objects.filter(contact_email=contact_email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'contact.html', {'name': contact_name, 'email': contact_email, 'phone': contact_phone, 'subject': contact_subject, 'message': contact_message})

        # Create and save the contact object
        contact = contacts.objects.create(
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            contact_subject=contact_subject,
            contact_message=contact_message,
        )
        messages.success(request, 'Your message has been sent successfully.')
        return redirect('contact')

    return render(request, 'contact.html')
