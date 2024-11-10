from django.urls import path, re_path, register_converter
from . import views, converters


app_name = 'main'
register_converter(converters.ForDigitYearConvertor, "year4")


urlpatterns = [
    path('', views.index, name='home'),
    path('welcome/', views.welcome_page, name='welcome-page'),

    path('about/', views.about, name='about'),
    path('add-post/', views.add_post, name='add_post'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
]