from multiprocessing import context
from django.shortcuts import render
from apps.carrousel.models import Carrousel


def Index(request):
    return render(request, 'index.html')