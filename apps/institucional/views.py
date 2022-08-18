from django.shortcuts import render
from .models import Autoridades, Cargo

# Create your views here.

def ListarAutoridades(request):
    autoridades = Autoridades.objects.all()
    cargo  = Cargo.objects.all()
    context = {
        'autoridades':autoridades,
        'cargo': cargo,
    }
    return render(request,'institucional.html',context)