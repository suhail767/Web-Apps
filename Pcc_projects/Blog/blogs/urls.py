"""Defines url patterns for blogs"""

from django.urls import path

from . import views


app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all posts.
    path('posts/', views.posts, name='posts'),

    # Page for adding a new post
    path('new_post/', views.new_post, name='new_post'),
]
