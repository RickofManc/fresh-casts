"""
Form configuration for member app
"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

# Global Variables
User = get_user_model()


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


class LoginForm(AuthenticationForm):
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
