from django.urls import path
from account import views

urlpatterns = [
    path('', views.post_index, name='post_index'),
]
