"""
Django imports to support Views
"""
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import EditProfileForm, PasswordChangingForm
from .forms import RegisterUserForm, LoginForm


# Global Variables
User = get_user_model()


class SignUpView(SuccessMessageMixin, CreateView):
    """
    Displays SignUp page.
    gets : requested template by name
    returns : rendered view of the html template
    Returns user to homepage on form submission.
    """
    model = User
    form_class = RegisterUserForm
    template_name = "sign_up.html"
    success_url = reverse_lazy("home")
    success_message = "Thank you for joining our community! \
                       You can now like and add blog posts"

    def get_object(self, queryset=None):
        """Returns user object"""
        return self.request.user


class LoginView(SuccessMessageMixin, View):
    """
    Displays Login page.
    gets : requested template by name
    returns : rendered view of the html template
    Returns user to homepage on form submission.
    """
    model = User
    form_class = LoginForm
    template_name = "login.html"
    success_url = reverse_lazy("home")
    success_message = "Welcome back to Fresh Casts"

    def get_object(self):
        """Returns user object"""
        return self.request.user


class UserEditView(SuccessMessageMixin, UpdateView):
    """
    Displays Edit Profile page.
    gets : requested template by name
    returns : rendered view of the html template
    Returns user to homepage on form submission.
    """
    form_class = EditProfileForm
    template_name = "edit_profile.html"
    success_url = reverse_lazy("home")
    success_message = "Your profile has been successfully updated"

    def get_object(self, queryset=None):
        """Returns user object"""
        return self.request.user


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    """
    Displays User Agreement page.
    gets : requested template by name
    returns : rendered view of the html template
    Returns user to homepage on form submission.
    """
    form_class = PasswordChangingForm
    template_name = "change-password.html"
    success_url = reverse_lazy("home")
    success_message = "Your password has been successfully updated"
