from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView

from .forms import ProfileSettingsForm
from posts.models import Post


@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user)
    data = {
        'title': 'Profile',
        'user_name': request.user.get_username(),
        'profile_img': '',
        'posts': posts,
    }

    return render(request, 'user_profiles/profile.html', context=data)


class ProfilePage(ListView, LoginRequiredMixin):
    pass


class ProfileSettings(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileSettingsForm
    template_name = 'user_profiles/profile_settings.html'
    extra_context = {'title': 'Profile settings'}

    def get_success_url(self):
        return reverse_lazy('user_profiles:profile_settings')

    def get_object(self, queryset=None):
        return self.request.user
