from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        max_length=150, widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    subject = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    message = forms.CharField(
        max_length=2000, widget=forms.Textarea(attrs={"class": "form-control"})
    )
    contact_status = forms.CharField(label="", widget=forms.CheckboxInput())

    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message")
