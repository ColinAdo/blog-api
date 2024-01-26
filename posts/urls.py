from django.urls import path

from .views import ListPost, DetailPost

urlpatterns = [
    path('<str:pk>/', DetailPost.as_view(), name='detail_post'),
    path('', ListPost.as_view(), name='list_post'),
]