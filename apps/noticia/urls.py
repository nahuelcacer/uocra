from django.urls import path, re_path
from . import views
app_name = 'apps.noticia'

urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view(),name="addNoticia"),
    path('listarNoticia2/', views.ListarNoticia, name="listarNoticia2"),
    path('listarPorCategoria/<str:categoria>',views.ListarNoticiaPorCategoria, name='listarPorCategoria'),
    path('readpost/<int:id>', views.ReadPost, name="readpost"),
    path('addCategoria/', views.AddCategoria.as_view( ),name="addCategoria"),

]