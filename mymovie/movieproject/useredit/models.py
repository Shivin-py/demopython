from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm


# Create your models here.
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
#     username = models.CharField(max_length=50, default='')
#     last_name = models.CharField(max_length=50, default='')
#     password1 = models.CharField(max_length=50, default='')
#     password2 = models.CharField(max_length=50, default='')