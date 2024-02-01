from django.shortcuts import render, redirect, reverse
from babel.numbers import format_currency
import locale

from productos.models import Producto

def carrito(request):
    ids_productos = request.COOKIES.get('carrito', '').split('%2C')
    cantidades = request.COOKIES.get('cantidades', '').split('%2C')
    modelos = request.COOKIES.get('modelos', '').split('%2C')
    validacion = False

    if ids_productos != ['']:
        validacion = True
        if len(ids_productos) == len(cantidades) == len(modelos):
            productos_carrito = []

            for id_producto, cantidad, modelo in zip(ids_productos, cantidades, modelos):
                producto = Producto.objects.get(id=id_producto)
                
                
                if not modelo:
                    modelo = "Unico"

                
                productos_carrito.append({
                    'producto': producto,
                    'cantidad': cantidad,
                    'modelo': modelo,
                })

                
            return render(request, 'carrito.html', {'productos_carrito': productos_carrito, 'validacion': validacion})
        else:
            return render(request, 'carrito.html', {'validacion': validacion})
    else:
        return render(request, 'carrito.html', {'validacion': validacion})