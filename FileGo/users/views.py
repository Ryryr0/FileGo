from django.contrib.auth import logout
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    authentication_form = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Authorization'}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Registration'}
    success_url = reverse_lazy('users:login')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
