from django import forms
from .models import Articulo, Categoria

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'imagen_art', 'autor', 'categoria_art']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ingrese un titulo'}),
            'contenido': forms.Textarea(attrs={'placeholder': 'Ingrese su contenido'}),
            'autor': forms.TextInput(attrs={'placeholder': 'Ingrese el autor'}),
        }
        labels = {
            'imagen_art': 'Subir Imagen',
            'categoria_art': 'Elegir Categoria'
        }

    def clean(self):
        cleaned_data = super().clean()
        for field, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[field] = value.strip()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        w = self.fields['imagen_art'].widget

        if isinstance(w, forms.ClearableFileInput):
            w.clear_checkbox_label = "Quitar Imagen Actual"
            w.initial_text = "Actual"
            w.input_text = "Cambiar Imagen"




class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ingrese el titulo'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Ingrese la descripcion'})
        }

