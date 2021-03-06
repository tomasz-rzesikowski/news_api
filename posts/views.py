from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly
from posts.serializers import PostSerializer, UserSerializer


class PostViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



# Authotization: Basic