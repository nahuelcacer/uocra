from django.db import models
from apps.usuario.models import Usuario
from apps.noticia.models import Noticia
# Create your models here.

class Comentario(models.Model):

    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    texto = models.TextField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, null=True, on_delete= models.SET_NULL)

    class Meta:
        ordering = ('-fecha',)  # muestra comentarios en orden

    def __str__(self):
        return 'comentario de {} en {}'.format(self.usuario.username, self.noticia)