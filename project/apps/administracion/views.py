from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from productos.forms import ProductoForm


# Create your views here.
@login_required
def administracion(request):
    formProducto = ProductoForm()

    return render(request, "administracion.html",  { 'formProducto': formProducto })