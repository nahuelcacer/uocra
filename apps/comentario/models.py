from django.db import models
from apps.noticia.models import Noticia
# Create your models here.

class Comentario(models.Model):

    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    comentario = models.TextField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-fecha',)  # muestra comentarios en orden

    def __str__(self):
        return 'comentario de {} en {}'.format(self.nombre, self.noticia)