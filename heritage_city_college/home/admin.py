from django.contrib import admin

from . models import contacts, admissions
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_name', 'contact_email', 'contact_phone', 'contact_subject', 'contact_message')

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'admission_name', 'admission_number', 'admission_email', 'admission_state', 'admission_city', 'admission_pincode', 'admission_department')

admin.site.register(contacts, ContactAdmin)

admin.site.register(admissions, AdmissionAdmin)
