"""
Form configuration for blog app
"""
from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Comment, Post


class PostForm(forms.ModelForm):
    """
    Uses Django forms and AddPostView
    to enable users to add blog posts
    """
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Add a title for the show here, \
                    maybe with the episode number'})),
    slug = forms.SlugField(
        max_length=255, widget=forms.TextInput(
            attrs={'class': 'form-control'})),
    category = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'})),
    author = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'})),
    content = forms.CharField(
        widget=forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Add a description of the show, and why \
                        you are sharing it here'})),
    excerpt = forms.CharField(
        max_length=180, widget=forms.TextInput(
            attrs={'class': 'form-control'})),
    podcast_url = forms.URLInput(
        attrs={'class': 'form-control',
               'placeholder': 'Paste the website \
                               address where we can listen to the show'}),
    featured_image = CloudinaryFileField()

    class Meta:
        model = Post
        fields = ("title", "category", "author", "content",
                  "excerpt", "podcast_url", "featured_image")


class CommentForm(forms.ModelForm):
    """
    Uses Django form to enable users
    to add comments to blog posts
    within Post Detail view.
    """
    class Meta:
        model = Comment
        fields = ("message",)


class UpdateForm(forms.ModelForm):
    """
    Uses Django forms and UpdatePostView
    to enable users to edit their own blog posts
    """
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Add a title for the show here, \
                    maybe with the episode number'})),
    category = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'})),
    content = forms.CharField(
        widget=forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Add a description of the show, and why \
                        you are sharing it here'})),
    excerpt = forms.CharField(
        max_length=180, widget=forms.TextInput(
            attrs={'class': 'form-control'})),
    podcast_url = forms.URLInput(
        attrs={'class': 'form-control',
               'placeholder': 'Paste the website \
                               address where we can listen to the show'}),
    featured_image = CloudinaryFileField()

    class Meta:
        model = Post
        fields = ("title", "category", "content",
                  "excerpt", "podcast_url", "featured_image")
