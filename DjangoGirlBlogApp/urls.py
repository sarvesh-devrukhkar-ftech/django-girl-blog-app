from django.urls import path
from . import views

urlpatterns = [path("", views.post_listing, name="post_listing")]
