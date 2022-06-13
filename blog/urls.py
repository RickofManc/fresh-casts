"""
URL mapping file
"""
from django.urls import path
from django_filters.views import FilterView
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('accessibility_statement/', views.get_accessibility_statement, name='accessibility_statement'),
    path('copyright_statement/', views.get_copyright_statement, name='copyright_statement'),
    path('category/', FilterView.as_view(), name='category'),
]
