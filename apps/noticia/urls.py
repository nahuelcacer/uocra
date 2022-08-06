from django.urls import path

from . import views
app_name = 'apps.noticia'

urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view()),
    path('listarNoticia/', views.mostrarNoticia.as_view()),
    path('listarNoticia2/', views.ListarNoticia),
    path('listarCategoria/<str:categoria>', views.ListarNoticiaPorCategoria, name="listarCategoria"),
]