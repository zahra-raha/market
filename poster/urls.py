from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("posts/my-posts", views.MyPostList.as_view(), name="my_posts"),
    path("post/new", views.NewPost.as_view(), name="new_post"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]