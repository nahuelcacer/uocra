from email import message
from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Usuario
from .forms import RegistroUsuarioFrom
from django.contrib.auth.forms import UserCreationForm


# class CustomUserCreationForm(UserCreationForm):
# 	class Meta(UserCreationForm.Meta):
# 		model = Usuario
# 		#fields = UserCreationForm.Meta.fields + ('imagen')
# 		template_name = 'usuario/registrar.html'
		
		

class RegistrarUsuario(CreateView):
	model = Usuario
	form_class = RegistroUsuarioFrom
	template_name = 'usuario/registrar.html'
	success_url = reverse_lazy('login')
	
class ModificarUsuario(UpdateView):
	model = Usuario
	form_class = RegistroUsuarioFrom
	template_name = 'usuario/modificar.html'

class DeleteUsuario(DeleteView):
	model = Usuario
	success_url = reverse_lazy('index')

