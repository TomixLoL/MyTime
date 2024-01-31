from django.shortcuts import render, redirect, reverse
from babel.numbers import format_currency
import locale

from carrito.Carrito import Carrito
from productos.models import Producto

def carrito(request):
    ids_productos = request.COOKIES.get('carrito', '').split(',')
    validacion = False

    if ids_productos != ['']:
        validacion = True
        ids_productos = list(map(int, ids_productos))
        productos_carrito = Producto.objects.filter(id__in=ids_productos)
        return render(request, 'carrito.html', {'productos_carrito': productos_carrito, 'validacion': validacion})
    else:
        return render(request, 'carrito.html', {'validacion': validacion})