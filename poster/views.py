from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Category
from .forms import CategoryForm, PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=0).filter(
        approved=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=0)
        post = get_object_or_404(queryset, slug=slug)
        category = post.category

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "category": category,
            },
        )


class NewPost(View):
    def get(self, request, *args, **kwargs):
        queryset = Category.objects.order_by('-created_on')

        return render(
            request,
            "new_post.html",
            {
                "post_form": PostForm
            },
        )


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.order_by('-created_on')
    template_name = 'category.html'
    paginate_by = 6
