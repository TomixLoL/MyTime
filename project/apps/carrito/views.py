from django.shortcuts import render, HttpResponse, redirect
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
    return redirect("carrito:carrito")

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

    return render(request, "carrito.html", {'productos': productos, 'total_carrito': total_carrito})