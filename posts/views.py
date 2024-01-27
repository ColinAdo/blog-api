from rest_framework import generics # permissions => view level permissions

from .serializers import PostSerializer
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
