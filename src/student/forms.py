from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import student

class UserForm(UserCreationForm):
    class Meta:
        model =User
        fields =["username","password1","password2"]
        help_text ={
            'username':'same as your registration no'
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=student
        fields=[
            'name',
            'cpi',
            'gender',
        ]

