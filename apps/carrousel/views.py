from multiprocessing import context
from django.shortcuts import render
from apps.carrousel.models import Carrousel

# Create your views here.

def ListarCarrousel(request):
    carrousel = Carrousel.objects.all()
    context = {
        'carrousel':carrousel
    }
    return render(request,'carrousel/listarCarrousel.html', context)
