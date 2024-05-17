from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Fixed
from products.models import Installment

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=100, unique=True)
    profile_img = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    age = models.IntegerField()
    money = models.IntegerField()
    salary = models.IntegerField()
    fixed = models.ManyToManyField(Fixed, related_name='member')
    installment = models.ManyToManyField(Installment, related_name='member')
