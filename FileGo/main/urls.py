from django.urls import path, re_path, register_converter
from . import views, converters


app_name = 'main'


urlpatterns = [
    path('', views.NewsLine.as_view(), name='home'),
    path('<str:q>', views.NewsLine.as_view(), name='search_home'),
    path('welcome', views.welcome_page, name='welcome_page'),
]
