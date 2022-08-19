from django.urls import path, re_path
from . import views
app_name = 'apps.institucional'

urlpatterns = [
    path('institucional/', views.ListarAutoridades ,name="institucional")
]