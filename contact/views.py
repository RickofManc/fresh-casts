"""
Django imports to support Views
"""
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm


def contact(request, *args, **kwargs):
    """
    Displays Contact Us page.
    Uses Post method to send contact form.
    Validation checks performed on input before saving.
    Email sent externally to Fresh Casts Gmail.
    Retains user on same page after commenting.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data['email', ''],
                "subject": form.cleaned_data['subject', ''],
                "message": form.cleaned_data['message', ''],
            }
            message = "\n".join(body.values())
            try:
                messages.success(request, 'Thank you for your contacting \
                    - Fresh Casts will reply within 24 hours!')
                send_mail(subject, message, 'email', ["freshcastsapp@gmail.com"], fail_silently=False)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(request, "contact.html", {})

    form = ContactForm()
    return render(request, "contact.html", {})


def form_invalid(self):
    """
    Displays error to user if contact form
    has not been successfully submitted.
    """
    messages.error(
        self.request, "Something went wrong with your submission.\
                       Please try again."
    )
    return HttpResponseRedirect("")
