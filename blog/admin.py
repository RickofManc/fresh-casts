""" Provides functionality for Django admin """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Displays the fields and values
    for Post Model in admin panel.
    """
    list_display = ('title', 'slug', 'author', 'category', 'created_on')
    search_fields = ['title', 'content', 'author', 'category']
    list_filter = ('status', 'author', 'category', 'created_on')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Displays the fields and values
    for Comment model in admin panel.
    """
    list_display = ('username', 'message', 'post', 'created_on', 'approved')
    search_fields = ['username', 'created_on']
    list_filter = ('created_on', 'approved')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        """ Function to approve user comments """
        queryset.update(approved=True)


admin.site.register(Category)
