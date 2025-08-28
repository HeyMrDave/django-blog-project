from django.contrib import admin
from .models import Articulo, Categoria
# Register your models here.
class ArtAdm(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', )

admin.site.register(Articulo, ArtAdm)
admin.site.register(Categoria)