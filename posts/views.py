from django.shortcuts import render
from .serializers import PostSerializer, UserSerializer
from .models import Posts
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model

# Create your views here.
user = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

# class PostList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer

# class UserList(generics.ListCreateAPIView):
#     queryset = user.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = user.objects.all()
#     serializer_class = UserSerializer