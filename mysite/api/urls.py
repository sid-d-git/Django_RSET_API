from django.urls import path
from .views import BlogPostListCreate, BlogPostRetrieveUpdateDestory, BlogPostList, default_view

urlpatterns = [
    path('', default_view, name='default-view'),  # Default view at /api/
    path('blogpost/', BlogPostListCreate.as_view(), name='blogpost-list-create'),
    path('blogpost/<int:pk>/', BlogPostRetrieveUpdateDestory.as_view(), name='blogpost-update-destroy'), 
    path('blogposts/', BlogPostList.as_view(), name='blogpost-list'),  
]
