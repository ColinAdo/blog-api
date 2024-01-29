from django.contrib.auth import get_user_model
from rest_framework import generics # permissions => view level permissions

from .serializers import PostSerializer, UserSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly  # => custom  permissions


class ListPost(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,) => view level permissions
    permission_classes = (IsAuthorOrReadOnly,)  # => custom  permissions
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ListUser(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
