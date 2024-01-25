from django.shortcuts import render, HttpResponse
from .models import Feed


# writing Feed APIs
def home(request):
    feeds = Feed.objects.all()
    context = {
        "feeds": feeds
    }
    return render(request, "feeds/home.html", context)