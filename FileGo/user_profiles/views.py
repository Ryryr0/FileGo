from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView

from .forms import ProfileSettingsForm
from posts.models import Post


class ProfilePage(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'user_profiles/profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user.get_username()

        try:
            context['title'] = User.objects.filter(id=self.kwargs['author_post_user'])[0]
            context['is_owner'] = False
        except KeyError:
            context['title'] = self.request.user.get_username()
            context['is_owner'] = True

        return context

    def get_queryset(self):
        try:
            return Post.published.filter(author=self.kwargs['author_post_user'])
        except KeyError:
            return Post.objects.filter(author=self.request.user)


class ProfileSettings(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileSettingsForm
    template_name = 'user_profiles/profile_settings.html'
    extra_context = {'title': 'Profile settings'}

    def get_success_url(self):
        return reverse_lazy('user_profiles:profile')

    def get_object(self, queryset=None):
        return self.request.user
