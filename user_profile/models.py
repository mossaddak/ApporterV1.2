from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomeUserManager


class User(AbstractUser):

    email = models.EmailField( max_length=150,unique=True,error_messages={"unique":"The email must be unique."})
    REQUIRES_FIELDS = ["email"]
    objects = CustomeUserManager()

    def __str__(self):
        return str(self.pk) + "." + self.username







    