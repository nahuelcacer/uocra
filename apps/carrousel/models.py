from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
class Carrousel(models.Model):
    imagen = CloudinaryField(null=True, blank=True , verbose_name='Imagen')
    title = models.CharField(max_length=150, default="titulo")

    def __str__(self):
        return self.title