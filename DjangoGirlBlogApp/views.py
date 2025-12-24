from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_listing(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now().order_by("published_date")
    )
    return render(request, "DjangoGirlBlogApp/post_listing.html", {posts})
