from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string


menu = [
    {'title': 'About FileGo', 'url_name': 'about'},
    {'title': 'Add post', 'url_name': 'add_post'},
    {'title': 'Contact', 'url_name': 'contact'},
    {'title': 'Log in', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'title 1', 'content': 'content 1', 'is_published': True},
    {'id': 2, 'title': 'title 2', 'content': 'content 2', 'is_published': False},
    {'id': 3, 'title': 'title 3', 'content': 'content 3', 'is_published': True},
]


def index(request):
    data = {
        'title': 'FileGo main page',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'main/index.html', context=data)


def about(request):
    return render(request, 'main/about.html', {'title': 'About FileGo', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f'Showing article with id = {post_id}')


def add_post(request):
    return HttpResponse("Adding post")


def contact(request):
    return HttpResponse("Contacting")


def login(request):
    return HttpResponse("Log in")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1><p>404</p>")
