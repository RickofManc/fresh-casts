"""
URL mapping file
"""
from django.urls import path, re_path
from . import views
from .views import ContactView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('', ContactView.as_view(), name='contact'),
]
