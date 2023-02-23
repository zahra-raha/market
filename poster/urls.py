from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("posts/my-posts", views.MyPostList.as_view(), name="my_posts"),
    path("post/new", views.NewPost.as_view(), name="new_post"),
    path('post/edit/<slug:slug>/', views.EditPost.as_view(),
         name='post_update'),
    path('post/delete/<slug:slug>/', views.DeletePost.as_view(),
         name='post_delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
