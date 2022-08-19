from math import fabs
from pyexpat import model
from django.db import models

# Create your models here.
class Cargo(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    def __str__(self):
        return self.nombre

class Autoridades(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    email = models.CharField(max_length=250,null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='institucional', default='institucional/default.png')
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
