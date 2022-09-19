from django.db import models
from datetime import datetime

# Create your models here.


class Caneta(models.Model):
    modelo = models.CharField(max_length=45, null=False)
    cor = models.CharField(max_length=45, null=False)
    ponta = models.CharField(max_length=45, null=False)

    def str(self):
        return self.modelo
