from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import student,Faculty,choice

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

class choices(forms.Form):
    choice1= forms.ModelChoiceField(queryset=Faculty.objects.all(),empty_label="-- Select order--")
    choice2= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice3= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice4= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice5= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice6= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice7= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice8= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice9= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice10= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice11= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice12= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice13= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice14= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice15= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice16= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice17= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice18= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice19= forms.ModelChoiceField(queryset=Faculty.objects.all())
    choice20= forms.ModelChoiceField(queryset=Faculty.objects.all())