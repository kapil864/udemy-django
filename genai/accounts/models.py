from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=10, blank=False)
    country_code = models.CharField(max_length=3, blank=False)
