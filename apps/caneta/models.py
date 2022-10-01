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
