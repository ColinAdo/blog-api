from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import PostSerializer
from .models import Post

class ListPost(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
