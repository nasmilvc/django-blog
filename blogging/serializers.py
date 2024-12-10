from django.contrib.auth.models import User
from blogging.models import Post, Category
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "text",
            "author",
            "created date",
            "modified_date",
            "published_date",
        ]
        # created and modified dates might be removed if issue


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "description", "posts"]
