from django.db import models
from django.utils import timezone


class Contact(models.Model):
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
    contact_status = models.CharField(max_length=15, choices=FORM_STATUS, default=1)
