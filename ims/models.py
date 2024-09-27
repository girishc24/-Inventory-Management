from django.db import models
from django.contrib.auth.models import User 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, unique=True, null=False) 
    company = models.CharField(max_length=50,  null=True, blank=True) 
    designation = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    emp_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.User.username

class Item(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name