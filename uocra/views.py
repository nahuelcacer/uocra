from multiprocessing import context
from django.shortcuts import render
from apps.carrousel.models import Carrousel
from apps.noticia.models import Noticia


def Index(request):
    carrousel = Carrousel.objects.all()
    noticia  = Noticia.objects.all()

    context = {
        'carrousel':carrousel,
        'noticia': noticia,
    }
    return render(request, 'index.html', context)


def Contacto(request):
    return render(request, 'contacto.html')

