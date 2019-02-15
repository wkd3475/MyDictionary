from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=30, unique=True)
    user_password = models.CharField(max_length=128)

    def __str__(self):
        return self.user_name
