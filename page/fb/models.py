from django.db import models

# Create your models here.
# models.py

from django.db import models

class UserProfile(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
