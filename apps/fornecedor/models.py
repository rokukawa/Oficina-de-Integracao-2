from ast import fix_missing_locations
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=45)
    celular = models.CharField(max_length=20, null=False, blank=True)
    comercial = models.CharField(max_length=20, null=False, blank=True)
    residencial = models.CharField(max_length=20, null=False, blank=True)
    rua = models.CharField(max_length=45, null=False, blank=True)
    numero = models.CharField(max_length=45, null=False, blank=True)
    cidade = models.CharField(max_length=45, null=False, blank=True)
    cep = models.CharField(max_length=45,  null=False, blank=True)
    bairro = models.TextField(max_length=45,  null=False, blank=True)
    complemento = models.TextField(max_length=45, null=True, blank=True)

    def __str__(self):
        return f'{self.nome_fornecedor}'    


