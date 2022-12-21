""" Django automated testing """
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment, Category


# Global Variables
User = get_user_model()


class TestViews(TestCase):
    """
    Independent test for Blog/Views
    """
    @classmethod
    def setUpTestData(self):
        """ Create test data """
        self.user = User.objects.create(username='testdummy')
        self.user.set_password('543210')
        self.user.save()

        self.category = Category.objects.create(
            name=1
        )

        self.post = Post.objects.create(
            title='Test Blog Post',
            slug='test-blog-post',
            author=self.user,
            category_id=1,
            content='test content for test blog post',
            excerpt='an excerpt for testing purposes',
            podcast_url='www.testurl.com',
            featured_image='test_img.jpeg',
            status=1
        )

        self.comment = Comment.objects.create(
            post=self.post,
            username=self.user,
            message='test comment for test blog post'
        )

    # Test string methods for Comments
    def test_comment_str(self):
        """
        test the __str__ method used for
        adding Blog Post Comments
        """
        self.assertEqual(
            str(self.comment),
            f'Comment {self.comment.message} by {self.user}')

    # Test default field values for Post and Comment approval
    def test_post_approved(self):
        """
        test default value working
        for Comment approved field
        """
        self.assertFalse(self.post.status == 0)

    def test_comment_approved(self):
        """
        test default value working
        for Comment approved field
        """
        self.assertFalse(self.comment.approved)
