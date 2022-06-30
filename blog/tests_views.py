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

    # Test retrieval of correct views to templates
    def test_get_post_list_view(self):
        """ test homepage retrieval and template usage """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'index.html')

    def test_get_post_detail_view(self):
        """ test Blog Post Detail retrieval and template usage """
        response = self.client.get(
            reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_get_add_post_view(self):
        """ test Add Blog Post retrieval and template usage """
        self.client.login(username='testdummy', password='543210')
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'add_post.html')

    def test_get_update_post_view(self):
        """ test Edit Blog Post retrieval and template usage """
        self.client.login(username='testdummy', password='543210')
        response = self.client.get(
            reverse('update_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'update_post.html')

    def test_get_delete_post_view(self):
        """ test Delete Blog Post retrieval and template usage """
        self.client.login(username='testdummy', password='543210')
        response = self.client.get(
            reverse('delete_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'delete_post.html')

    def test_get_category_view(self):
        """ test Category page retrieval and template usage """
        response = self.client.get(
            reverse('category', args=[self.category.name]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'categories.html')

    def test_get_about_view(self):
        """ test About page retrieval and template usage """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'about.html')

    def test_get_accessibility_statement_view(self):
        """ test Accessibility Statement page retrieval and template usage """
        response = self.client.get(reverse('accessibility_statement'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'accessibility_statement.html')

    def test_get_copyright_statement_view(self):
        """ test Copyright Statement page retrieval and template usage """
        response = self.client.get(reverse('copyright_statement'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'copyright_statement.html')

    def test_get_user_agreement_view(self):
        """ test Copyright Statement page retrieval and template usage """
        response = self.client.get(reverse('user_agreement'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'user_agreement.html')

    # Test user features and functionality
    def test_post_like_view(self):
        """ 
        test Post Liking feature by adding a 'like'
        and checking it has been counted
        """
        self.client.login(username='testdummy', password='543210')
        number_of_likes = self.post.likes.count()
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]))
        self.assertRedirects(
            response, reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(self.post.likes.count(), number_of_likes+1)
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]))
        self.assertRedirects(
            response, reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(self.post.likes.count(), number_of_likes)

    def test_post_comment_view(self):
        """
        test Post Commenting feature by adding a 'Comment'
        successfully
        """
        self.client.login(username='testdummy', password='543210')
        response = self.client.post(
                    reverse('post_detail',
                            args=[self.post.slug]),
                    data={'message': 'new_comment'})
        self.assertRedirects(
            response, reverse('post_detail', args=[self.post.slug]))

    def test_context(self, *args, **kwargs):
        """
        test passing additional information to the template
        """
        context = super(self.category, self).get_context_data(*args, **kwargs)
        response = self.client.get(Category.objects.all())
        self.assertIsNone(response.context['cat_menu'])
        self.assertIsNone(response.context['PostDetail'])


