""" Django automated testing """
from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Tests fields on Comment Form
    as part of Blog Posts
    """
    def test_message_field_is_required(self):
        """ Tests that value is valid """
        form = CommentForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())

    def test_fields_are_explicit_in_form_metaclass(self):
        """ Tests that fields on the form align to Comment Form class """
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('message',))
