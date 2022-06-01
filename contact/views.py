from django.core.mail import send_mail, BadHeaderError
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm


class ContactView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')

    def get(self, request):
        form_class = ContactForm
        success_message = "Your message was submitted successfully!"
        if request.method == 'GET':
            form_class = ContactForm()
        else:
            form_class = ContactForm(request.POST)
            if form_class.is_valid():
                subject = form_class.cleaned_data['subject']
                email = form_class.cleaned_data['email']
                message = form_class.cleaned_data['message']
                try:
                    send_mail(subject, message, email, ['freshcastsapp@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return success_message            
        return render(request, 'contact.html', {'form': form_class})
    
    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong with your submission. Please try again.')
        return HttpResponseRedirect('')