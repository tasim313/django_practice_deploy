from django import forms
from . models import *


class UserForm_1(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserInfoForm_1(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('facebook_url', 'profile_pic')