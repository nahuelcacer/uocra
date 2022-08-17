from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Noticia, Categoria
from apps.comentario.models import Comentario
from apps.comentario.forms import ComentarioForm
# Create your views here.

# vista de edicion generica basada en clase
class AddNoticia(CreateView):
    model = Noticia
    fields = ['titulo', 'texto', 'categoria', 'activo', 'imagen']
    template_name = 'noticia/addNoticia.html'
    success_url = reverse_lazy('index')

# vista de edicion generica basada en funciones
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
    noticia = Noticia.objects.filter(categoria = categoria2[0].id)
    context = { 
		'noticia': noticia,
    }
    return render(request,'noticia/listarPorCategoria.html', context)

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
		posts   = ExistePost(id)
	except Exception:
		posts   = Noticia.objects.get(id=id)
	comentarios = Comentario.objects.filter(noticia=id)
    

	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		if request.user.is_authenticated:
			aux =  form.save(commit=False)
			aux.noticia = posts
			aux.user = request.user
			aux.save()
			form = ComentarioForm()
		else:
			return redirect('usuario:login')
	
	context = {
		'titulo': 'post',
		'posts': posts,
		'form': form,
		'comentarios': comentarios,
	}
	return render(request,'noticia/post.html', context)