"""
Django imports to support Views
"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import CommentForm, EditProfileForm, PasswordChangingForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
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
        if request.user.is_authenticated:
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, slug=slug)
            comment_form = CommentForm(data=request.POST)
            # comments = post.comments.filter(approved=True).order_by("-created_on")
            # liked = False
            # if post.likes.filter(id=self.request.user.id).exists():
                # liked = True        

            if comment_form.is_valid():
                comment_form.instance.username = request.user
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                messages.success(request, 'Thank you for your comment !')
            # else:
            #     comment_form = CommentForm()
            # return render(
            #     request,
            #     "post_detail.html",
            #     {
            #         "post": post,
            #         "comments": comments,
            #         "commented": True,
            #         "liked": liked,
            #         "comment_form": CommentForm(),
            #     },
            # )
        # User HttpResponseRedirect here instead of render to ensure comment
        # is not re-submitted on page re-load
        return HttpResponseRedirect(reverse('hike_detail', args=[slug]))

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class AddPostView(CreateView):
    model = Post
    template_name = "add_post.html"
    fields = ("title", "category", "author", "content", "podcast_url", "featured_image")

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ("title", "category", "content", "podcast_url", "featured_image")

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    fields = "title"
    success_url = reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class CategoryView(View):
    model = Post
    template_name = "categories.html"

    def get(self, request, cats, *args, **kwargs):
        category_posts = Post.objects.filter(
            category__name__contains=cats.replace("-", " ")
        )
        return render(
            request,
            self.template_name,
            {"cats": cats.title().replace("-", " "), "category_posts": category_posts},
        )

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = "edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserEditView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = "change-password.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PasswordsChangeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class About(View):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(About, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AccessibilityStatement(View):
    template_name = "accessibility_statement.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AccessibilityStatement, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class CopyrightStatement(View):
    template_name = "copyright_statement.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CopyrightStatement, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UserAgreement(View):
    template_name = "user_agreement.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserAgreement, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context