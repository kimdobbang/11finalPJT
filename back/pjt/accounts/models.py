from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    age = models.IntegerField()
    money = models.IntegerField()
    salary = models.IntegerField()
