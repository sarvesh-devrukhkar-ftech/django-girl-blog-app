from django.shortcuts import render


def post_listing(request):
    return render(request, "DjangoGirlBlogApp/post_listing.html", {})
