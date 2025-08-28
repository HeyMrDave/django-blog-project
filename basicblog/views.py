from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Articulo, Categoria
from .forms import ArticuloForm, CategoriaForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

# Creear Categorias


def crear_categoria(request):
    if request.method == "GET":
        return render(request, 'crear_categoria.html', {
            'form': CategoriaForm
        })
    else:
        try:
            form = CategoriaForm(request.POST)
            new_cat = form.save(commit=False)
            new_cat.save()
            return redirect('crear_articulo')
        except ValueError:
            return render(request, "crear_categoria.html", {
                'error': "Datos ingresados incorrectamente",
                'form': CategoriaForm
            })


# Crear Articulo
def crear_articulo(request):
    if request.method == 'GET':
        return render(request, 'crear_articulo.html', {
            'form': ArticuloForm
        })
    else:
        try:
            form = ArticuloForm(request.POST, request.FILES)
            new_artcl = form.save(commit=False)
            new_artcl.save()
            return redirect("mostrar_art")

        except ValueError:
            return render(request, 'crear_articulo.html', {
                'error': "Hubo un error al crear el articulo, por favor, coloque bien los datos",
                'form': ArticuloForm
            })

# Listar Articulos


def mostrar_articulo(request):
    articulos = Articulo.objects.all()
    return render(request, 'mostrar_articulo.html', {
        'articulos': articulos
    })

# Detalles articulo


def detalles_art(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    return render(request, 'detalles_art.html', {
        'articulo': articulo
    })

# Actualizar articulo


def act_articulo(request, id):
    try:
        if request.method == "GET":
            articulo = get_object_or_404(Articulo, id=id)
            form = ArticuloForm(instance=articulo)
            return render(request, 'act_articulo.html', {
                'form': form,
                'articulo': articulo
            })
        else:
            articulo = get_object_or_404(Articulo, id=id)
            form = ArticuloForm(request.POST,request.FILES, instance=articulo)
            articulo.fecha_modificacion = timezone.now()
            articulo.save()
            form.save()
            return redirect('mostrar_art')

    except ValueError:
        return render(request, 'act_articulo.html', {
            'error': "Los valores que ha ingresado son incorrectos",
            'form': form,
            'articulo': articulo
        })

# Eliminar articulo


def eliminar_art(request, id):
    articulo = get_object_or_404(Articulo, id=id)

    if request.method == "GET":
        articulo.delete()
        return redirect('mostrar_art')


# Detalles. categoria

def detalles_cat(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    return render(request, 'mostrar_cat.html', {
        'categoria': categoria
    })


# Editar categoria

def editar_cat(request, id):
    if request.method == "GET":
        categoria = get_object_or_404(Categoria, id=id)
        form = CategoriaForm(instance=categoria)
        return render(request, 'editar_cat.html', {
            'categoria': categoria,
            'form': form
        })
    else:
        try:
            categoria = get_object_or_404(Categoria, id=id)
            form = CategoriaForm(request.POST, instance=categoria)
            form.save()
            return redirect('detalles_cat', id=id)
        except ValueError:
            return render(request, 'editar_cat.html', {
                'error': "Valores ingresados incorrectamente",
                'categoria': categoria,
                'form': form
            })
        
#Eliminar categoria

def eliminar_cat(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == "GET":
        categoria.delete()
        return redirect('inicio')

#Buscar articulos por nombre

def buscar_ar(request):
    titulo = request.GET['titulo']
    articulos = []
    
    if titulo:
        articulos = Articulo.objects.filter(titulo__icontains = titulo)

    return render(request, 'buscar_articulo.html', {
        'titulo': titulo,
        'articulos' : articulos
    })

#Mostrar articulos por categoira

def mostrar_art_cat(request, id_cat):
    if request.method == 'GET':
        articulos = Articulo.objects.filter(categoria_art = id_cat)
        categorias_n = get_object_or_404(Categoria, id=id_cat)
        return render(request, 'mostrar_art_cat.html', {
            'articulos': articulos,
            'categorias_n': categorias_n
        })


