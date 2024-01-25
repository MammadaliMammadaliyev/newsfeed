from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<h1>hello world</h1>")