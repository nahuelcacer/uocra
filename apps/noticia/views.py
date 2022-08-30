from multiprocessing import context
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from .models import Noticia, Categoria
from .forms import AgregarCategoria
from apps.comentario.models import Comentario
from apps.comentario.forms import ComentarioForm
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

# vista de edicion generica basada en clase
class AddNoticia(SuccessMessageMixin,CreateView):

    model = Noticia
    fields = ['titulo', 'texto', 'resumen','categoria', 'activo', 'imagen']
    template_name = 'noticia/addNoticia.html'
    success_url = reverse_lazy('apps.noticia:listarNoticia2')
    success_message =  "Noticia creada con exito"
    
# vista de edicion generica basada en funciones
# class AddCategoria(SuccessMessageMixin, CreateView):		
#     model = Categoria
#     fields = ['nombre']
#     template_name = 'noticia/addCategoria.html'
#     success_url = reverse_lazy('apps.noticia:listarNoticia2')
#     success_message = 'Categoria: "%(nombre)s" agregada con exito'
class AddCategoria(View):
    def get(self,request,*args, **kwargs):
        categorias = Categoria.objects.all()
        form = AgregarCategoria()
        context = {
            'form':form,
            'categorias':categorias
        }
        return render(request, 'noticia/listarCategorias.html', context)

    def post(self,request,*args, **kwargs):
        form = AgregarCategoria(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apps.noticia:listarCategoria',)    
        

def ListarNoticia(request):
    noticia    = Noticia.objects.all()
    categoria  = Categoria.objects.all()
    context = {
        'noticia':noticia,
        'categoria': categoria,
    }
    return render(request,'noticia/listarNoticia2.html',context)

def ListarNoticiaPorCategoria(request, categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    categoria = Categoria.objects.get(nombre=categoria)
    noticia = Noticia.objects.filter(categoria = categoria2[0].id)
    context = { 
        'noticia': noticia,
        'categoria': categoria
    }
    return render(request,'noticia/listarPorCategoria.html', context)


def ListarCategoria(request):
    form = Categoria(request.POST)
    context = {
        'categoria': Categoria.objects.all(),
        'form': form
    }
    return render(request, 'noticia/listarCategorias.html',context)


def noticias(request):
    noticias = Noticia.objects.get(all)
    return render(noticias)

def ExistePost(id):
    for i in noticias:
        if i.id == id:
            return i
    return None

def ReadPost(request, id):
    try:
        noticias   = ExistePost(id)
    except Exception:
        noticias   = Noticia.objects.get(id=id)
    comentarios = Comentario.objects.filter(noticia=id)
    

    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            aux =  form.save(commit=False)
            aux.noticia = noticias
            aux.user = request.user
            aux.save()
            form = ComentarioForm()
        else:
            return redirect('usuario:login')
    
    context = {
        'titulo': 'noticia',
        'posts': noticias,
        'form': form,
        'comentarios': comentarios,
    }
    return render(request,'noticia/post.html', context)