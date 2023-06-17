from django.db import models
from django.contrib.auth.models import User

class APIKey(models.Model):
    key = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
