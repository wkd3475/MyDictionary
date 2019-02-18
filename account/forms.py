from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password",)
