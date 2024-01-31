from django.shortcuts import render, redirect, reverse
from babel.numbers import format_currency
import locale

from carrito.Carrito import Carrito
from productos.models import Producto

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "carrito.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer or reverse('carrito:carrito'))

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito:carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito:carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito:carrito")


def tienda(request):
    productos = Producto.objects.all()
    carrito = Carrito(request)

    locale.setlocale(locale.LC_NUMERIC, 'es_AR')

    # Calcula el total del carrito
    total_carrito = carrito.calcular_total()
    total_carrito = format_currency(total_carrito, 'ARS', locale='es_AR')

    return render(request, "carrito.html", {'productos': productos, 'total_carrito': total_carrito,})


def ver_carrito(request):
    ids_productos = request.COOKIES.get('carrito', '').split(',')

    productos_carrito = Producto.objects.filter(id__in=ids_productos)
    print(ids_productos)

    return render(request, 'ver_carrito.html', {'productos_carrito': productos_carrito})
