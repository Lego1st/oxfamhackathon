# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from annoying.fields import AutoOneToOneField
from django.db.models import signals
from django.urls import reverse
import datetime
# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='gallery/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    timeCreate = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.owner.username


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author = models.ForeignKey(User, related_name='user_comments')
    text = models.TextField(default="")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

