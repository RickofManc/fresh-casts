"""
blog app URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("post/<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("like/<slug:slug>", views.PostLike.as_view(), name="post_like"),
    path("add_post/", views.AddPostView.as_view(), name="add_post"),
    path("post/edit/<slug:slug>", views.UpdatePostView.as_view(), name="update_post"),
    path("post/remove/<slug:slug>", views.DeletePostView.as_view(), name="delete_post"),
    path("category/<str:cats>/", views.CategoryView.as_view(), name="category"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("edit_profile/", views.UserEditView.as_view(), name="edit_profile"),
    path("password/", views.PasswordsChangeView.as_view(), name="change-password"),
    path("about/", views.About.as_view(), name="about"),
    path("accessibility_statement/", views.AccessibilityStatement.as_view(), name="accessibility_statement",),
    path("copyright_statement/", views.CopyrightStatement.as_view(), name="copyright_statement",),
    path("user_agreement/", views.UserAgreement.as_view(), name="user_agreement"),
]
