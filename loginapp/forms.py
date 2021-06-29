from django import forms

from django.contrib.auth.models import User

from . models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('facebook_url', 'profile_pic')