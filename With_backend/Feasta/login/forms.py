from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    name = forms.CharField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['name','password']