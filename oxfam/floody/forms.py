# -*- coding: UTF-8 -*-
from django import forms
from .models import *
# from django import models

class EditProfileForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.CharField(label='Phone', max_length=15)

class PostForm(forms.ModelForm):
    class Meta(object):
        model = Post
        fields = ('image','location',)

class RegisterForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ('username', 'first_name', 'password')

class CommentForm(forms.ModelForm):
    class Meta(object):
        model = Comment
        fields = ('text',)
