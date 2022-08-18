from multiprocessing import context
from django.shortcuts import render
from apps.carrousel.models import Carrousel


def Index(request):
    carrousel = Carrousel.objects.all()
    context = {
        'carrousel':carrousel
    }
    return render(request, 'index.html', context)

def Contacto(request):
    return render(request, 'contacto.html')