from django.db import models
from django.conf import settings
from apps.usuario.models import Usuario
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class Categoria(models.Model):
    nombre = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.nombre

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = RichTextField(null=True)    
    resumen = models.CharField(max_length=250, null=False, default=" ")
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = CloudinaryField(null=True, blank=True , verbose_name='Imagen')
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo