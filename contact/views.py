from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm


class ContactView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'contact.html'
    success_message = "Your message was submitted successfully!"
    
    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong with your submission. Please try again.')
        return HttpResponseRedirect('')