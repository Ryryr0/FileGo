from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request): # HttpRequest
    return HttpResponse("<h1>You are on Welcome page<h2>")


def categories(request):
    return HttpResponse("<h1>Categories</h1>")
