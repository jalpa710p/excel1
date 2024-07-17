from django.db import models
from django.contrib.auth.models import AbstractUser


class MyModel(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    email_otp = models.CharField(max_length=4, default='0000')  # Default value for email_otp
    mobile_otp = models.CharField(max_length=4, default='0000')
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)


class Lgform(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=60)




