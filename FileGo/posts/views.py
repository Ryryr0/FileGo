from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView


class PostCreator(CreateView, LoginRequiredMixin):
    form_class = PostCreationForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Registration'}
