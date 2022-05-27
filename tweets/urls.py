from django.contrib import admin
from django.urls import path, include
from . import views

"""
CLIENT
Base ENDPOINT /api/tweets/
"""

urlpatterns = [
    path('', views.tweet_list_view, name="tweet-list-view"),
    path('action/', views.tweet_action_view, name='tweet-action-view'),
    path('create/', views.tweet_create_view, name="tweet-create-view"),
    path('<int:pk>/', views.tweet_detail_view, name="tweet-detail-view"),
    path('<int:pk>/delete/', views.tweet_delete_view, name='tweet-delete-view'),
]
