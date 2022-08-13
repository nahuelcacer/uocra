from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def Index(request):
    return render(request, 'index.html')
    

