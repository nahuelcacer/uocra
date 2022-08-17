from django.urls import path
from . import views

app_name="apps.comentarios"

urlpatterns = [
    path('addcomentario/', views.AddComentario, name="addComentario"),
    path('comentario/', views.Comentarios, name="comentario")
]