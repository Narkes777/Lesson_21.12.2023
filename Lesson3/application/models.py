from django.db import models

# Create your models here.

class Ad(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(null=True, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=50)
    published = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)