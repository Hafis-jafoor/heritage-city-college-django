from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('pysiotherapy/', views.pysiotherapy, name='pysiotherapy'),
    path('occupational/', views.occupational, name='occupational'),
    path('admission/', views.admission, name='admission'),
    path('departments/', views.departments, name='departments'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    # path('contact/create/', views.contact, name='contact'),
]
