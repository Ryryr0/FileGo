from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from .forms import ProfileSettingsForm


@login_required
def profile(request):
    data = {
        'title': 'Profile',
        'user_name': request.user.username,
        'profile_img': '',
    }
    return render(request, 'user_profiles/profile.html', context=data)


class ProfilePage(CreateView, LoginRequiredMixin):
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
