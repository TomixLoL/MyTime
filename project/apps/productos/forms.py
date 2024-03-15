from django import forms
from .models import Producto, ProductoCategoria, ImagenProducto, Opcion
from django.forms.widgets import ClearableFileInput
from django.utils.html import format_html
from django import forms
from .models import ImagenProducto

class CustomClearableFileInput(ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Renderizar el selector de archivo
        html = super().render(name, value, attrs)

        # Si hay un archivo adjunto actualmente, renderizar el botón de eliminar
        if value and hasattr(value, 'url'):
            html += format_html(
                '<button type="button" class="btn btn-danger" onclick="removeFile(\'id_{0}-clear_id\')">Eliminar</button>',
                name,
            )
        return html

class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = ProductoCategoria
        fields = "__all__"

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }

class ImagenProductoForm(forms.ModelForm):
    class Meta:
        model = ImagenProducto
        fields = ['imagenes']
        widgets = {
            'imagenes': CustomClearableFileInput,
        }

ImagenProductoFormSet = forms.inlineformset_factory(Producto, ImagenProducto, form=ImagenProductoForm, extra=1)

class OpcionForm(forms.ModelForm):
    class Meta:
        model = Opcion
        fields = ['opciones']
        widgets = {
            'opciones': forms.TextInput(attrs={'class': 'form-control'}),
        }

OpcionFormSet = forms.inlineformset_factory(Producto, Opcion, form=OpcionForm, extra=1)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'precio', 'descripcion', 'imagen_producto', 'destacado']

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['imagen_producto'].required = False
