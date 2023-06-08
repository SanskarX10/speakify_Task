from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from phone_field import PhoneField

class User(AbstractUser):
    username = None
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=256)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    phone = PhoneField(blank=True)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    interests = ArrayField(models.CharField(max_length=20))
    is_online = models.BooleanField(default=False)
    websocket = models.TextField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []