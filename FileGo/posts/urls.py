from django.urls import path
from . import views


app_name = 'posts'


urlpatterns = [
    path('post-creation/', views.PostCreator.as_view(), name='post_creation'),
    path('post/<slug:post_slug>', views.ShowPost.as_view(), name='post'),
]
