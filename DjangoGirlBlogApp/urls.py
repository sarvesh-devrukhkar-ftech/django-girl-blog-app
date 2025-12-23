from django.urls import path
from . import views

urlsPatterns = [
    path('', views.post_listing, name='post_listing')
]

