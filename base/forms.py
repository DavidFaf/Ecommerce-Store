# from django.contrib.auth.forms import UserCreationForm
# from .models import *


# class MyUserCreationForm(UserCreationForm):
#     class Meta:
#         model = UserModel
#         fields = ['firstname', 'lastname', 'email', 'password1', 'password2']

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserModel
from django import forms

class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Firstname'})
    )

    last_name = forms.CharField(
    label='',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Lastname'})
    )

    email = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'})
    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Password'})
    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Password again'})
    )

        
    class Meta:
        model = UserModel
        fields = ('email','first_name','last_name')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = ('email','first_name','last_name')
