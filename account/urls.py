from django.urls import path
from account import views

urlpatterns = [
    path('', views.post_index, name='post_index'),
    path('post_index', views.post_index, name='post_index'),
    path('sign_up', views.post_sign_up, name='sign_up'),
]
