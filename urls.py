from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrarUsuario, ModificarUsuario, DeleteUsuario
from django.contrib.auth import views as auth_views

#from .views import
app_name = 'apps.usuario'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="usuario/login.html"), name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('addUsuario/', RegistrarUsuario.as_view() ,name="addUsuario"),
    path('modificarUsuario/<str:pk>', ModificarUsuario.as_view() ,name="modificarUsuario"),
    path('eliminarUsuario/<int:pk>', DeleteUsuario.as_view() ,name="eliminarUsuario"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name ='password_reset_complete')
]