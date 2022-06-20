"""
blog app configuration
"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Standard config for auto incrementing.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
