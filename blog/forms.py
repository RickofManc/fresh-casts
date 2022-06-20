"""
Form configuration for blog app
"""
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Uses Django form to enable users
    to add comments to blog posts
    within Post Detail view.
    """
    class Meta:
        model = Comment
        fields = ("message",)


class EditProfileForm(UserChangeForm):
    """
    Uses Django form to enable users
    to update their own profile details.
    """
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")


class PasswordChangingForm(PasswordChangeForm):
    """
    Uses Django form to enable users
    to update their account password.
    """
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control",
                                   "type": "password"})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control",
                                   "type": "password"})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control",
                                   "type": "password"})
    )

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")
