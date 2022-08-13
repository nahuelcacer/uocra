#from django.contrib.auth.models import User
from pyexpat.errors import messages
from pkg_resources import require
from .models import Usuario
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegistroUsuarioFrom(UserCreationForm):
    class Meta:
        model = Usuario
        fields =  ['username','password1','password2','first_name','last_name','email', 'imagen']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_superuser = False
        user.is_staff = False
        user.save()
        return user