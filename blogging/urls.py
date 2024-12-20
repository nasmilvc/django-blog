# from django.conf.urls import url
from django.urls import path
from blogging.views import PostListView, PostDetailView, stub_view

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
]
