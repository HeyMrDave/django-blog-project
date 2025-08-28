from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="inicio"),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('mostrar_articulo/', views.mostrar_articulo, name='mostrar_art'),
    path('crear_categoria/', views.crear_categoria, name='crear_cat'),
    path('articulo/<int:id>', views.detalles_art, name='detalles_art'),
    path('articulo/actualizar/<int:id>', views.act_articulo, name='act_artcl'),
    path('articulo/eliminar/<int:id>', views.eliminar_art, name='eliminar_art'),
    path('categoria/detalles/<int:id>', views.detalles_cat, name='detalles_cat'),
    path('categoria/editar/<int:id>', views.editar_cat, name='editar_cat'),
    path('categoria/eliminar/<int:id>', views.eliminar_cat, name='eliminar_cat'),
    path('articulo/buscar/', views.buscar_ar, name='buscar_ar'),
    path('categoria/mostrar_articulos/<int:id_cat>', views.mostrar_art_cat, name='mostrar_art_cat')

]