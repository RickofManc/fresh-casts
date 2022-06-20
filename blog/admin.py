"""
blog Admin Configuration
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Displays the fields and values
    for Post Model in admin panel.
    """
    list_display = ('title', 'slug', 'author', 'created_on')
    search_fields = ['title', 'content', 'author']
    list_filter = ('status', 'author', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['approve_post']

    def approve_post(self, request, queryset):
        """ Function to approve user posts """
        queryset.update(approved=True)


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
