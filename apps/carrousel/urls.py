from django.urls import path, re_path
from . import views
app_name = 'apps.carrousel'

urlpatterns = [
    path('listarCarrousel/', views.ListarCarrousel ,name="listarCarrousel"),
]