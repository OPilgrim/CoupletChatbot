from django.db import models

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=48)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    avatar = models.ImageField(upload_to='../avatar/')

class Corpus(models.Model):
    uuid = models.CharField(max_length=36)
    userid = models.CharField(max_length=16)
    timestamp = models.TimeField(auto_now=True)
    first_couplet = models.CharField(max_length=16)
    second_couplet = models.CharField(max_length=16)
    quality = models.BooleanField(auto_created=True)
    status = models.BooleanField(auto_created=False)
