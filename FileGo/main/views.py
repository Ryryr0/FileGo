from django.http import HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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


# @login_required(login_url='main:welcome_page')
def index(request):
    data = {
        'title': 'FileGo main page',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'main/index.html')


def welcome_page(request):
    return render(request, 'main/welcome_page.html')


class NewsLine(LoginRequiredMixin):
    pass


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1><p>404</p>")
