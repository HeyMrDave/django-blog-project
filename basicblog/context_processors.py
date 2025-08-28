from .models import Categoria, Articulo

def get_categorias(request):
    categorias = Categoria.objects.all()
    
    return {
        'categorias':categorias
    }

# def get_articulos(request):
#     articulos = Articulo.objects.all()

#     return {
#         'articulos': articulos
#     }