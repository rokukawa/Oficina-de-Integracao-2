from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from datetime import datetime

# Create your models here.


class Caneta(models.Model):
    modelo = models.CharField(max_length=45, validators=[MinLengthValidator(4)], null=False)
    cor = models.CharField(max_length=45, validators=[MinLengthValidator(4)], null=False)
    ponta = models.CharField(max_length=45, validators=[MinLengthValidator(4)], null=False)

    def str(self):
        return f'{self.modelo}, {self.cor}, {self.ponta}'

class Lote(models.Model):
    codigo_maquina = models.CharField(max_length=45, null=False)
    data_fabricação = models.DateField(null=False)
    quantidade = models.IntegerField(null=False)
    caneta = models.ForeignKey(Caneta, on_delete=CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=CASCADE)

    def _str_(self):
        return self.codigo_maquina        
