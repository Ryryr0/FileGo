from django.urls import path, re_path, register_converter
from . import views, converters


app_name = 'main'
register_converter(converters.ForDigitYearConvertor, "year4")


urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('home', views.index, name='home'),
]
