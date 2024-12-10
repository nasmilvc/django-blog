from django.http.response import HttpResponse, Http404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blogging.models import Post, User, Category
from rest_framework import permissions, viewsets
from blogging.serializers import PostSerializer, UserSerializer, CategorySerializer


def stub_view(request, *args, **kwargs):  # allows it to manage all parameters received
    body = "Stub View\n\n"
    if args:
        body += "Args: /n"
        body += "/n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Keyword args: \n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):
    model = Post
    template_name = "blogging/list.html"

    # returns the value of the queryset attribute, but we can use it to add more logic
    def get_queryset(self):
        return Post.objects.exclude(published_date__exact=None).order_by(
            "-published_date"
        )


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
