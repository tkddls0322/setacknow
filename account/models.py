from django.db import models

from django.contrib.auth.models import User


class NowUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pn = models.CharField(max_length=20, blank=True)

# Create your models here.
