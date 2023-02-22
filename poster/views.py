from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=0).filter(
        approved=True).order_by('-cleated_on')
    template_name = 'index.html'
    paginate_by = 6