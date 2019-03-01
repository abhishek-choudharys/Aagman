from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_startup = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    name = models.CharField(default="",max_length=100)
    number=models.IntegerField(null=True)
    address = models.CharField(default="", max_length=100)
    dipp = models.IntegerField(null=True)
    description = models.CharField(default="", max_length=200)
    picture = models.ImageField(upload_to='profilepic/',null = True, blank=True)
