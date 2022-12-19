""" Enabling categories to be available site wide """
from blog.models import Category


def extras(request):
    """ Function to display category names in Nav on all pages """
    categories = Category.objects.all()
    return {'categories': categories}
