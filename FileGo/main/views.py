import os

from django.conf import settings
from django.db.models import Q, Count
from django.http import HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
from django.views.generic import ListView

from posts.models import Post

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


class NewsLine(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        file_path = os.path.join(settings.BASE_DIR, 'utils', 'strings', 'search_elim_words_en.text')
        with open(file_path, 'r') as file:
            search_elim_words = file.read().splitlines()

        if query:
            queryset = (Post.published.filter(Q(title__icontains=query) | Q(author__username__icontains=query)))
            if queryset:
                return queryset

            search_terms = query.split()
            query_object = Q()
            for term in search_terms:
                if term not in search_elim_words:
                    query_object |= Q(title__icontains=term) | Q(content__icontains=term) | Q(author__username__icontains=term)

            queryset = (
                Post.published.filter(query_object)
                .annotate(match_count=Count('id'))
                .order_by('-match_count')
            )
            return queryset
        return Post.published.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['user_name'] = self.request.user.get_username()
        context['search_field'] = self.request.GET.get('q', '')
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1><p>404</p>")
