from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("post/new", views.NewPost.as_view(), name="new_post"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]