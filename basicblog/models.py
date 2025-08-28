from django.db import models

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.titulo}"

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen_art = models.ImageField(upload_to='static/articulos_img/', blank=True, null=True)
    autor = models.CharField(max_length=150)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    categoria_art = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} creado por {self.autor}"


