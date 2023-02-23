from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic, View

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import CategoryForm, PostForm
from django.template.defaultfilters import slugify
import cloudinary


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=0).filter(
        approved=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category'] = Category.objects.order_by('-created_on')
        return context


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        category = post.category
        return render(
            request,
            "post/post_detail.html",
            {
                "post": post,
                "category": category,
            },
        )


class MyPostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=0).filter(
        approved=True).order_by('-created_on')
    template_name = 'post/my_posts.html'
    paginate_by = 6

    def get_queryset(self):
        return self.model.objects.filter(seller=self.request.user)


class NewPost(View):
    def get(self, request):
        return render(
            request,
            "post/new_post.html",
            {
                "post_form": PostForm
            },
        )

    def post(self, request):
        post_form = PostForm(data=request.POST, files=request.FILES)

        if post_form.is_valid():
            post_form.instance.seller = request.user
            post = post_form.save(commit=False)
            post.slug = slugify(post_form.cleaned_data['title'])
            post.save()
            category = post.category
            return render(
                request,
                "post/post_detail.html",
                {
                    "post": post,
                    "category": category,
                },
            )
        else:
            post_form = PostForm()
            return render(
                request,
                "post/new_post.html",
                {
                    "post_form": PostForm
                },
            )


class EditPost(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        post_form = PostForm(instance=post)
        return render(
            request,
            "post/edit_post.html",
            {
                "post_form": post_form
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        post_form = PostForm(data=request.POST, files=request.FILES,
                             instance=post)

        if post_form.is_valid():
            epost = post_form.save(commit=False)
            epost.slug = slugify(post_form.cleaned_data['title'])
            epost.save()
            category = epost.category
            return render(
                request,
                "post/post_detail.html",
                {
                    "post": epost,
                    "category": category,
                },
            )
        else:
            post_form = PostForm()
            return render(
                request,
                "post/new_post.html",
                {
                    "post_form": PostForm
                },
            )


class PostSold(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        post.status = not post.status
        post.save()
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = "/posts/my-posts"


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.order_by('-created_on')
    template_name = 'category.html'
    paginate_by = 6
