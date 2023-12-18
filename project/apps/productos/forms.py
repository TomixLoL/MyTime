from django import forms
from .models import Producto, ProductoCategoria

class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = ProductoCategoria
        fields = "__all__"

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"