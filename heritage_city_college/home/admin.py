from django.contrib import admin

from . models import contacts
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_name', 'contact_email', 'contact_phone', 'contact_subject', 'contact_message')
    
admin.site.register(contacts, ContactAdmin)
