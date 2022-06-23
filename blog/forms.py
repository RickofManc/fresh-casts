"""
Form configuration for blog app
"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class PostForm(forms.ModelForm):
    """
    Uses Django forms and AddPostView
    to enable users to add blog posts
    """
    class Meta:
        model = Post
        fields = ("title", "category", "author", "content", "podcast_url",
                  "featured_image")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'form-control'}),
            'podcast_url': forms.URLInput(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """
    Uses Django form to enable users
    to add comments to blog posts
    within Post Detail view.
    """
    class Meta:
        model = Comment
        fields = ("message",)


class RegisterUserForm(UserCreationForm):
    """
    Uses Django form to enable site visitors
    to register for a user account.
    """
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username",
                  "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class LoginForm(forms.ModelForm):
    """
    Uses Django form to enable
    users to login to their user account.
    """
    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


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
        fields = ("first_name", "last_name", "username", "email", "password")


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

