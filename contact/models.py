"""
Standard Django database models
Standard Django timezone for date stamping
"""
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """
    Models the fields for the Contact Form.
    Additional admin feature to change status
    of forms as processed.
    """
    FORM_STATUS = (
        ('Open', 'Open'),
        ('Responded', 'Responded'),
        ('Complete', 'Complete')
    )

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
    date_submitted = models.DateTimeField(default=timezone.now)
    contact_status = models.CharField(
        max_length=15, choices=FORM_STATUS, default=1)
