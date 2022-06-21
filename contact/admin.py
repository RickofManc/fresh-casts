"""
blog Admin Configuration
"""
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Displays the fields and values
    for Contact Model in admin panel.
    """
    list_display = (
        'name', 'email', 'subject',
        'message', 'date_submitted', 'contact_status'
        )
    search_fields = [
        'name', 'subject', 'message',
        'date_submitted', 'contact_status'
        ]
    list_filter = (
        'name', 'date_submitted', 'contact_status'
        )
