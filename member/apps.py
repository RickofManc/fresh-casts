"""
Member app configuration
"""
from django.apps import AppConfig


class MemberConfig(AppConfig):
    """ Member app configuration """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'member'
