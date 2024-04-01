from django import forms
from .models import Producto, ProductoCategoria, ImagenProducto, Opcion, Estampado
from django import forms
from .models import ImagenProducto

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

ImagenProductoFormSet = forms.inlineformset_factory(Producto, ImagenProducto, form=ImagenProductoForm, extra=1, can_delete=False)

class OpcionForm(forms.ModelForm):
    class Meta:
        model = Opcion
        fields = ['opciones']
        widgets = {
            'opciones': forms.TextInput(attrs={'class': 'form-control'}),
        }

OpcionFormSet = forms.inlineformset_factory(Producto, Opcion, form=OpcionForm, extra=1, can_delete=False)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'precio', 'descripcion', 'imagen_producto', 'destacado']

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['imagen_producto'].required = True

class EstampadoForm(forms.ModelForm):
    class Meta:
        model = Estampado
        fields = '__all__'
