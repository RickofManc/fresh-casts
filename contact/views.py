from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email_address"],
                "subject": form.cleaned_data["subject"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, [], ["freshcastsapp@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(request, "contact.html", {})

    form = ContactForm()
    return render(request, "contact.html", {})


def form_invalid(self, form):
    messages.error(
        self.request, "Something went wrong with your submission. Please try again."
    )
    return HttpResponseRedirect("")
