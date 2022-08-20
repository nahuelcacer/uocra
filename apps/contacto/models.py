from typing_extensions import Self
from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.Charfield(max_leng=50)
    correo = models.EmailField()
    mensaje = models.TextField()

def __str__ (self):
    return self.nombre