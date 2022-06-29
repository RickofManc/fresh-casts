"""
Django imports to support Views
"""
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from blog.models import Category
from .forms import EditProfileForm, PasswordChangingForm
from .forms import RegisterUserForm, LoginForm


User = get_user_model()


class SignUpView(CreateView):
    """
    Displays SignUp page.
    gets : requested template by name
    returns : rendered view of the html template
    Returns user to homepage on form submission.
    """
    model = User
    form_class = RegisterUserForm
    template_name = "signup.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        """Returns user object"""
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(SignUpView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class LoginView(View):
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

    def get_object(self):
        """Returns user object"""
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(LoginView).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UserEditView(UpdateView):
    """
    Displays Edit Profile page.
    gets : requested template by name
    returns : rendered view of the html template
    Returns user to homepage on form submission.
    """
    form_class = EditProfileForm
    template_name = "edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        """Returns user object"""
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(UserEditView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PasswordsChangeView(PasswordChangeView):
    """
    Displays User Agreement page.
    gets : requested template by name
    returns : rendered view of the html template
    Returns user to homepage on form submission.
    """
    form_class = PasswordChangingForm
    template_name = "change-password.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(
            PasswordsChangeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
