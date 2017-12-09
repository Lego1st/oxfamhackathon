# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def postimage(request):
    im = request.POST.image
    pos = request.POST.location
    print(pos)
    return render(request, 'index.html')