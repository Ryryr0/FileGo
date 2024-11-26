from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import ProfileSettingsForm


test_data = {
    'title': 'Profile',
    'profile_img': '',
    'user_name': 'Artem',
}


def profile(request):
    return render(request, 'user_profiles/profile.html', context=test_data)


class ProfileSettings(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileSettingsForm
    template_name = 'user_profiles/profile_settings.html'
    extra_context = {'title': 'Profile settings'}

    def get_success_url(self):
        return reverse_lazy('user_profiles:profile_settings')

    def get_object(self, queryset=None):
        return self.request.user
