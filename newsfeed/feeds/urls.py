from django.urls import path
from .views import home


urlpatterns = [
    path("", home),
]


"""
127.0.0.1:8000/feeds/home
127.0.0.1:8000/feeds/haqqimizda
127.0.0.1:8000/feeds/kontaktlar

"""

