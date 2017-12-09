# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import *
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password, password_validators_help_texts, get_default_password_validators, ValidationError
from models import *

def index(request):
    return render(request, 'index.html')

def loggin_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        error = ""
    else:
        error = "Authentication Failed"
        messages.success(request, error)
    return HttpResponseRedirect(reverse('floody:index'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('floody:index'))

def register_complete(request):
    form = RegisterForm(request.POST or None)

    context = {
        "form": form,
        "error": None,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']
            try:
                validate_password(password)
                User.objects.create_user(username=username, first_name=first_name, password=password)
                return HttpResponseRedirect(reverse('floody:index'))
            except ValidationError:
                print(password_validators_help_texts(
                    get_default_password_validators()))
                context['error'] = password_validators_help_texts(
                    get_default_password_validators())
