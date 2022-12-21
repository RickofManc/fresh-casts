"""
member app URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('password/',
         views.PasswordsChangeView.as_view(),
         name='change-password'),
]
