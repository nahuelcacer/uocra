from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Cargo(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    def __str__(self):
        return self.nombre

class Autoridades(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    email = models.CharField(max_length=250,null=True)
    imagen = CloudinaryField(null=True, blank=True , verbose_name='Imagen')
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
