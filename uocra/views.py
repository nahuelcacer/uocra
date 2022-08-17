from multiprocessing import context
from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def Index2(request):
    return render(request, 'contacto/contac.html')
    

