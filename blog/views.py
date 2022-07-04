"""
Django imports to support Views
"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import CommentForm, PostForm, UpdateForm

# Global Variables
User = get_user_model()


class PostList(generic.ListView):
    """
    Displays detailed single page view of blog post.
    Additionally features to add a like or comment.
    Features dependent on user login status.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDetail(CreateView):
    """
    Displays detailed single page view of blog post.
    Additionally features to add a like or comment.
    Features dependent on user login status.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Retrieves and displays all blog post detail.
        If statement assesses whether user has already
        liked the post.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Allow authenticated users to comment on posts.
        If statement to check user is logged in.
        Validation checks performed on input before saving.
        Success message as user feedback.
        Retains user on same page after commenting.
        """
        if request.user.is_authenticated:
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, slug=slug)
            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                comment_form.instance.username = request.user
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                messages.success(request, 'Thank you for your comment \
                    - Fresh Casts will review and publish asap!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostLike(View):
    """
    Displays view to like/unlike blog post.
    Retrieves user information to pre-populate.
    Retains user on same page after liking/un-liking.
    """
    def post(self, request, slug):
        """ If/Else Post statement to perform action. """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class AddPostView(CreateView):
    """
    Displays Add Post page.
    gets : requested template by name
    returns : rendered view of the html template
    Returns user to homepage on form submission.
    """
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UpdatePostView(UpdateView):
    """
    Displays Edit Post page.
    gets : requested template by name
    returns : rendered view of the html template
    Returns user to homepage on form submission.
    """
    model = Post
    template_name = "update_post.html"
    form_class = UpdateForm
    success_url = reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class DeletePostView(DeleteView):
    """
    Displays Delete Post page.
    gets : requested template by name
    returns : rendered view of the html template
    Returns user to homepage on form submission.
    """
    model = Post
    template_name = "delete_post.html"
    fields = "title"
    success_url = reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class CategoryView(generic.ListView):
    """
    Displays Category page - content depending
    on which category has been selected by the user.
    gets : requested list of posts with matching category
    returns : rendered view of the html template
    """
    model = Post
    template_name = "categories.html"
    paginate_by = 8

    def get(self, request, cats, *args, **kwargs):
        """Retrieves posts filtered by requested category."""
        category = Category.objects.get(name__iexact=cats)
        category_posts = Post.objects.filter(category=category)

        return render(
            request,
            self.template_name,
            {"cats": cats.title(),
             "category_posts": category_posts},
        )

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class About(CreateView):
    """
    Displays About Us page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(About, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AccessibilityStatement(CreateView):
    """
    Displays Accessibility Statement page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = "accessibility_statement.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(
            AccessibilityStatement, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class CopyrightStatement(CreateView):
    """
    Displays Copyright Statement page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = "copyright_statement.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(
            CopyrightStatement, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UserAgreement(CreateView):
    """
    Displays User Agreement page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = "user_agreement.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def get_context_data(self, *args, **kwargs):
        """Provides podcast categories in nav-menu."""
        cat_menu = Category.objects.all()
        context = super(UserAgreement, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
