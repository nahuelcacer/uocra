from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Usuario
from .forms import RegistroUsuarioFrom

"""class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = Usuario
		#fields = UserCreationForm.Meta.fields + ('imagen')
		template_name = 'usuario/registrar.html'"""

class RegistrarUsuario(CreateView):
	model = Usuario
	form_class = RegistroUsuarioFrom
	template_name = 'usuario/registrar.html'
	success_url   = reverse_lazy('index')

class ModificarUsuario(UpdateView):
	model = Usuario
	form_class = RegistroUsuarioFrom
	template_name = 'usuario/modificar.html'
	success_url   = reverse_lazy('index')

class DeleteUsuario(DeleteView):
	model = Usuario
	template_name = 'usuario/usuario_confirm_delete.html'
	success_url = reverse_lazy('index')