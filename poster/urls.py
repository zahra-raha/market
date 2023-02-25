from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("posts/my-posts", views.MyPostList.as_view(), name="my_posts"),
    path("post/new", views.NewPost.as_view(), name="new_post"),
    path('post/cat/<int:cat>/', views.CatPostList.as_view(),
         name='cat_posts'),
    path('post/edit/<slug:slug>/', views.EditPost.as_view(),
         name='post_update'),
    path('post/buy/<slug:slug>/', views.BuyPost.as_view(),
         name='buy'),
    path('post/customers/<slug:slug>/', views.Customers.as_view(),
         name='view_customers'),
    path('post/status/<slug:slug>/', views.PostSold.as_view(),
         name='post_status'),
    path('post/delete/<slug:slug>/', views.DeletePost.as_view(),
         name='post_delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
