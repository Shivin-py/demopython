# from django.db import models
# from movieapp.models import Category
# from django.utils import timezone
#
#
# # Create your models here.
#
#
# class Item(models.Model):
#     title = models.CharField(max_length=100)
#     poster = models.ImageField(upload_to='user_movies', blank=True)
#     desc = models.TextField(blank=True)
#     release_date = models.DateField(default=timezone.now)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     actors = models.TextField(blank=True)
#     trailer_link = models.TextField(blank=True)
