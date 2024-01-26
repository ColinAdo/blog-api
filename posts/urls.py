from django.urls import path

from .views import ListPost, DetailPost

urlpatterns = [
    path('<str:pk>/', DetailPost.as_view(), 'detail_post'),
    path('', ListPost.as_view(), 'list_post'),
]