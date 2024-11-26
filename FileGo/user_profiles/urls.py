from django.urls import path
from . import views


app_name = 'user_profiles'


urlpatterns = [
    path('', views.profile, name='profile'),
    path('settings/', views.ProfileSettings.as_view(), name='profile_settings'),
]
