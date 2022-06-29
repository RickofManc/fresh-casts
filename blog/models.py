"""
Standard Django database models
Standard Django authentication model
Standard Django reverse url model
Cloudinary model to support image repository
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField



# Global Variables
STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    Models the fields for Post Categories.
    This enables separate views of posts
    by category value.
    Choice of 5 categories assigned when adding a post.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    """
    Models the fields for a blog Post.
    """
    title = models.CharField(max_length=255, unique=True, primary_key=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=False
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=5000)
    excerpt = models.TextField(max_length=180, blank=True)
    podcast_url = models.URLField(max_length=255)
    featured_image = CloudinaryField("image", default="placeholder")
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="blogpost_like", blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        Counts number of blog post likes
        Returns number of blog post likes
        """
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("home")


class Comment(models.Model):
    """
    Models the fields for adding Post Comments.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_comments")
    message = models.TextField(help_text="Add your comment here")
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.message} by {self.username}"
