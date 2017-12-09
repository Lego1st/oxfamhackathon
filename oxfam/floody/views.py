# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from .forms import *
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password, password_validators_help_texts, get_default_password_validators, ValidationError
from .models import *
from PIL import Image
import pickle
import requests
import numpy as np
from io import BytesIO
import base64
# from StringIO import StringIO

def index(request):
    return render(request, 'index.html')

def postimage(request):
    im = request.POST.image
    pos = request.POST.location
    print(pos)
    return render(request, 'index.html')

@api_view(['POST'])
def camimage(request):
    if request.method == 'POST':
        image = request.data.get("image")
        location =  request.data.get('location').split()
        print(location)
        image = Image.open(BytesIO(base64.b64decode(image)))
        data = np.array(image,dtype=np.float32)
        url = "http://localhost:5050/classify"
        print("post file")
        r = requests.post(url,data=pickle.dumps(data[:,:,:3]))
        a = r.content.decode("utf-8")
        if a == "Flood":
            loc_x = float(location[0])
            loc_y = float(location[1])
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
