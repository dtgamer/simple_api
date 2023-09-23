from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=255, unique=True)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)
