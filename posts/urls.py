"""
from django.urls import path

from .views import ListPost, DetailPost, ListUser, DetailUser

urlpatterns = [
    path('users/', ListUser.as_view(), name='list_user'),
    path('users/<str:pk>/', DetailUser.as_view(), name='detail_user'),
    path('<str:pk>/', DetailPost.as_view(), name='detail_post'),
    path('', ListPost.as_view(), name='list_post'),
]
"""
from rest_framework.routers import SimpleRouter

from .views import PostViewset, UserViewset

router = SimpleRouter()
router.register("users", UserViewset, basename="users")
router.register("", PostViewset, basename="posts")

urlpatterns = router.urls