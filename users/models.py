from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Organization(models.Model):
  users = models.ManyToManyField(User)
  title = models.CharField('Organization', max_length=64, unique=True) 
