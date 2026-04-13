from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)  # Add email field


    def __str__(self):
        return self.name