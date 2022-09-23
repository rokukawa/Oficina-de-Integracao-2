from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    username = models.CharField(max_length=30, unique=False, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    telefone_celular = models.CharField(max_length=20, blank=True)
    telefone_residencial = models.CharField(max_length=20, blank=True)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}, {self.email}'