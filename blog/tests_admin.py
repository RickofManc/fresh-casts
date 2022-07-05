""" Django automated testing """
from django.test import TestCase
from django.urls import reverse
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
            message="test comment for test blog post"
        )

    def test_approve_posts(self):
        """ test approving blog posts """
        User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='543210'
        )
        self.client.login(username='admin', password='543210')
        # count how many of the current posts are approved
        published = Post.objects.filter(status=0).count()
        self.assertEqual(self.post.status, 1)
        # provide an action to approve a post
        data = {'actions': 'approve_post',
                '_selected_action': [self.post.title, ]}
        change_url = reverse('admin:blog_post_changelist')
        response = self.client.post(change_url, data, follow=True)

        self.assertEqual(response.status_code, 200)
        # count number of approved posts to assess if 1 has been approved
        self.assertEqual(
            Post.objects.filter(status=1).count(), published+1)

    def test_approve_comments(self):
        """ test approving blog comments """
        User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='543210'
        )
        self.client.login(username='admin', password='543210')
        # count how many of the current comments are approved
        approved = Comment.objects.filter(approved=True).count()
        self.assertFalse(self.comment.approved)

        data = {
            'action': 'approve_comment',
            '_selected_action': [self.comment.id, ]}
        change_url = reverse('admin:blog_comment_changelist')
        response = self.client.post(change_url, data, follow=True)

        self.assertEqual(response.status_code, 200)

        # check number of approved comments has increased by one
        self.assertEqual(
            Comment.objects.filter(approved=True).count(), approved+1)