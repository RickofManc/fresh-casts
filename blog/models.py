"""
Standard Django for database models
Standard Django Authentication model
Cloudinary as cloud based image repository
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Global Variables
STATUS = (
    (0, 'Draft'),
    (1, 'Published')
    )
PODCAST_CATEGORY = (
        (0, 'Latest'),
        (1, 'Life'),
        (2, 'Music'),
        (3, 'News'),
        (4, 'Sport'),
        (5, 'Technology')
        )


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, primary_key=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")
    category = models.IntegerField(choices=PODCAST_CATEGORY, default=0,)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=180, blank=True)
    podcast_url = models.URLField(max_length=200, help_text="Please add the \
                                  podcasts web address")
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_like',
                                   blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        """
        Counts number of blog post likes
        Returns number of blog post likes
        """
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(help_text="Add your comment here")
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='comment_likes', 
                                   blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.message} by {self.username}'
    
    def number_of_likes(self):
        """
        Counts number of comment likes
        Returns number of comment likes
        """
        return self.likes.count()
