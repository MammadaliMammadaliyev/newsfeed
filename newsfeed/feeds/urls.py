from django.urls import path
from .views import home, feed_details


urlpatterns = [
    path("", home, name="home"),
    path("xeber/<int:pk>/", feed_details, name="xeber_detal")
]


"""
127.0.0.1:8000/feeds/home
127.0.0.1:8000/feeds/haqqimizda
127.0.0.1:8000/feeds/kontaktlar

"""

