from django.shortcuts import render
from .models import Feed


# writing Feed APIs
def home(request):
    sort_by_view = request.GET.get("sort_by_view_count")
    by_latest = request.GET.get("by_latest")
    by_oldest = request.GET.get("by_oldest")

    feeds = Feed.objects.all()

    if sort_by_view:
        feeds = Feed.objects.order_by("-views_count")

    if by_latest:
        feeds.order_by("-published_at")

    if by_oldest:
        feeds.order_by("published_at")

    context = {
        "feeds": feeds
    }
    return render(request, "feeds/home.html", context)


def feed_details(request, pk): # primary_key, id
    feed = Feed.objects.get(pk=pk)
    feed.views_count += 1
    feed.save()
    context = {
        "feed": feed
    }
    return render(request, "feeds/feed_details.html", context)