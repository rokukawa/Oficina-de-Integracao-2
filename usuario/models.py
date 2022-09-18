from ast import fix_missing_locations
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(max_length=255, unique=True)
    telefone_celular = models.CharField(max_length=20, null=True, blank=True)
    telefone_residencial = models.CharField(max_length=20, null=True, blank=True)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []
