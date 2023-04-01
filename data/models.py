from django.db import models

# Create your models here.


class user(models.Model):
    name = models.SlugField(max_length=100)
    msg = models.TextField(max_length=1000)


class group(models.Model):
    name = models.SlugField(max_length=100)
    msg = models.TextField(max_length=1000)
    