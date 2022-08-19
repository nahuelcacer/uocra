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
<<<<<<< HEAD
=======

def Contacto(request):
    return render(request, 'contacto.html')
>>>>>>> 80101d84cfc6d06b9781cf61d0f6674d1d77650b
