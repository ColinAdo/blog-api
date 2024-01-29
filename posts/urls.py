from django.urls import path

from .views import ListPost, DetailPost, ListUser, DetailUser

urlpatterns = [
    path('users/', ListUser.as_view(), name='list_user'),
    path('users/<str:pk>/', DetailUser.as_view(), name='detail_user'),
    path('<str:pk>/', DetailPost.as_view(), name='detail_post'),
    path('', ListPost.as_view(), name='list_post'),
]